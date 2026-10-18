import numpy as np

def punto_fijo(f, g, aprox_actual, tolerancia=1e-6, max_iteraciones=100, raiz_exacta=None):
    historial = [] # Almacena el historial de errores k-esimos para las graficas

    for i in range(1, max_iteraciones + 1): 
        try: # Tenemos que probar primero casos para que la aproximacion no se vaya al infinito o se indetermine, por eso ocupamos try
            nueva_aprox = g(aprox_actual)

            if np.isnan(nueva_aprox) or np.isinf(nueva_aprox) or np.abs(nueva_aprox) > 1e10:
                return None, i, np.array(historial), False
            
        except (OverflowError, ZeroDivisionError, ValueError): # Caso en el que una de las operaciones realizadas sea demasiado grande 
            return None, i, np.array(historial), False

        if raiz_exacta is not None: # Calculamos el error
            diferencia = np.abs(nueva_aprox - raiz_exacta)
        else:
            diferencia = np.abs(nueva_aprox - aprox_actual)

        historial.append(diferencia)

        try: # Testemaos el valor nuevo en la funcion y tenemos la precaucion si es que es muy grande
            y_nueva = f(nueva_aprox)
        except Exception:
            y_nueva = np.inf

        if np.abs(y_nueva) < tolerancia or diferencia < tolerancia: # Criterio de parada
            return nueva_aprox, i, np.array(historial), True

        aprox_actual = nueva_aprox

    return nueva_aprox, max_iteraciones, np.array(historial), False
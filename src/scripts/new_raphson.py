import numpy as np

def newton_raphson(f, df, aprox_actual, tolerancia=1e-6, max_iteraciones=100, raiz_exacta=None):
    historial = [] # Almacena el historial de errores k-esimos para las graficas

    for i in range(1, max_iteraciones + 1):
        y = f(aprox_actual)
        dy = df(aprox_actual)

        if np.abs(dy) < 1e-14: # Caso en el que la derivada es 0 o casi 0
            return None, i, np.array(historial), False

        nueva_aprox = aprox_actual - (y / dy)
        y_nueva = f(nueva_aprox)

        if raiz_exacta is not None: # Calculamos el error
            diferencia = np.abs(nueva_aprox - raiz_exacta)
        else:
            diferencia = np.abs(nueva_aprox - aprox_actual)

        historial.append(diferencia)

        if np.abs(y_nueva) < tolerancia or diferencia < tolerancia: # Criterio de parada
            return nueva_aprox, i, np.array(historial), True

        aprox_actual = nueva_aprox

    return nueva_aprox, max_iteraciones, np.array(historial), False
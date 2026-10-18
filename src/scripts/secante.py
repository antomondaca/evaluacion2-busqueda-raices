import numpy as np

def secante(f, aprox_antigua, aprox_actual, tolerancia=1e-6, max_iteraciones=100, raiz_exacta=None):
    historial = []  # Almacena el historial de errores k-esimos para las graficas

    y_antiguo = f(aprox_antigua) # Simplifica uso de funcion (aclaracion para mas adelante)
    y_actual = f(aprox_actual) 

    for i in range (1, max_iteraciones + 1): 
        desnivel = y_actual - y_antiguo
        
        if np.abs(desnivel) < 1e-14:  # Evita la division por cero
            return None, i, np.array(historial), False
        
        nueva_aprox = aprox_actual - y_actual * (aprox_actual - aprox_antigua) / desnivel
        y_nueva = f(nueva_aprox)

        if raiz_exacta is not None: # Calculamos el error
            distancia = np.abs(nueva_aprox - raiz_exacta)
        else: 
            distancia = np.abs(nueva_aprox - aprox_actual) 

        historial.append(distancia)

        if np.abs(y_nueva) < tolerancia or distancia < tolerancia: # Criterio de parada
            return nueva_aprox, i, np.array(historial), True
        
        aprox_antigua = aprox_actual
        y_antiguo = y_actual
        aprox_actual = nueva_aprox
        y_actual = y_nueva

    return nueva_aprox, max_iteraciones, np.array(historial), False
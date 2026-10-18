import numpy as np

def biseccion(f, limite_izq, limite_der, tolerancia=1e-6, max_iteraciones=100, raiz_exacta=None):
    fa = f(limite_izq)
    fb = f(limite_der)

    if fa * fb >= 0: # Teorema de Bolzano
        return None, 0, [], False
    
    historial = [] # Almacena el historial de errores k-esimos para las graficas
    c_ant = limite_izq # Valor referencial inicial para calcular el error absoluto

    for k in range(1, max_iteraciones + 1):  
        punto_medio = (limite_izq + limite_der) / 2 # Dividimos el intervalo a la mitad osea, punto medio
        fc = f(punto_medio)

        if raiz_exacta is not None: # Calculamos el error absoluto
            error = np.abs(punto_medio - raiz_exacta)
        else:
            error = np.abs(punto_medio - c_ant) if k > 1 else abs(limite_der - limite_izq)

        historial.append(error)

        if np.abs(fc) < tolerancia or error < tolerancia: # Criterio de parada
            return punto_medio, k, np.array(historial), True # Retarna: raiz, iteraciones, erorres, exito
        
        if fa * fc < 0: # Reduccion de intervalo
            limite_der = punto_medio # Si esta entre a y c, acotamos el intervalo por la derecha, por lo tanto b = c
            fb = fc
        else:
            limite_izq = punto_medio # Si esta entre c y b, acotamos el intervalo por la izquierda, por lo tanto a = c
            fa = fc
            
        c_ant = punto_medio # Se guarda el punto medio actual
        
    return punto_medio, max_iteraciones, np.array(historial), False # Aca vamos a ocupar el np.array porque es mas facil de ocupar despues en el matplotlib (aclaracion para mas adelante)
        
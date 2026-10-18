import numpy as np

def falsa_posicion(f, limite_izq, limite_der, tolerancia=1e-6, max_iteraciones=100, raiz_exacta=None):
    fa = f(limite_izq)
    fb = f(limite_der)

    if fa * fb >= 0: # Teorema de Bolzano
        return None, 0, np.array([]), False
    
    historial = [] # Almacena el historial de errores k-esimos para las graficas
    c_ant = limite_izq # Valor referencial para el error absoluto

    for k in range(1, max_iteraciones + 1):
        denominador = fb - fa
        if np.abs(denominador) < 1e-14: # Evita la division por cero
            return None, k, np.array(historial), False

        punto_medio = (limite_izq * fb - limite_der * fa) / denominador # Formula de la falsa posicion
        fc = f(punto_medio)

        if raiz_exacta is not None: # Calculamos el error
            error = np.abs(punto_medio - raiz_exacta)
        else:
            error = np.abs(punto_medio - c_ant) if k > 1 else np.abs(limite_der - limite_izq)
            
        historial.append(error)

        if np.abs(fc) < tolerancia or error < tolerancia: # Criterio de parada
            return punto_medio, k, np.array(historial), True # Retorna: raiz, iteraciones, errores, exito
        
        if fa * fc < 0: # Reduccion de intervalo
            limite_der = punto_medio 
            fb = fc
        else:
            limite_izq = punto_medio
            fa = fc
            
        c_ant = punto_medio # Se guarda el punto medio actual
        
    return punto_medio, max_iteraciones, np.array(historial), False
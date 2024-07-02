import numpy as np

# Estados
estados = ['A', 'B', 'C']

# Matriz de transición
matriz_transicion = np.array([
    [0.1, 0.6, 0.3],  
    [0.4, 0.3, 0.3],  
    [0.2, 0.5, 0.3]   
])

# Función que realiza simulación, modelo de Markov
def simulacion_markov(matriz_transicion, estados, estado_inicial, num_pasos):
    estado_actual = estado_inicial
    indice_estado = estados.index(estado_actual)
    secuencia_estados = [estado_actual]

    for _ in range(num_pasos):
        proximo_indice_estado = np.random.choice(range(len(estados)), p=matriz_transicion[indice_estado])
        proximo_estado = estados[proximo_indice_estado]
        secuencia_estados.append(proximo_estado)
        indice_estado = proximo_indice_estado

    return secuencia_estados

# Parámetros 
estado_inicial = 'A'
num_pasos = 10

# Ejecución
resultado_simulacion = simulacion_markov(matriz_transicion, estados, estado_inicial, num_pasos)
print("Secuencia de estados simulada:", resultado_simulacion)

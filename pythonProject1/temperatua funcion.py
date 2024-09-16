# Edison Remache

# estudiante de primer semestre paralelo E

import numpy as np

# Definimos las constantes
ciudades = ['QUITO', 'RIOBAMBA', 'BABAHOYO']
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = 4  # Número de semanas

# Creamos una matriz 3D con temperaturas fijas (ejemplo)
# Formato: [ciudad][día][semana]
temperaturas = np.array([
    [
        [20, 21, 19, 22],  # Quito
        [23, 24, 22, 21],
        [18, 19, 20, 21],
        [25, 26, 24, 23],
        [27, 28, 26, 25],
        [30, 31, 29, 28],
        [22, 21, 20, 19]
    ],
    [
        [15, 16, 14, 15],  # Riobamba
        [17, 18, 16, 15],
        [14, 15, 14, 13],
        [19, 20, 18, 17],
        [21, 22, 20, 19],
        [24, 25, 23, 22],
        [16, 15, 14, 13]
    ],
    [
        [30, 31, 29, 30],  # Babahoyo
        [32, 33, 31, 30],
        [29, 30, 28, 27],
        [35, 36, 34, 33],
        [37, 38, 36, 35],
        [40, 41, 39, 38],
        [32, 31, 30, 29]
    ]
])

# Función para calcular el promedio de temperatura por ciudad durante un periodo de semanas
def calcular_promedio_temperaturas(Ciudades, Temperaturas, Semanas):
    for i, ciudad in enumerate(Ciudades):
        print(f"\nPromedio de temperaturas para {ciudad}:")
        for semana in range(semanas):
            promedio = np.mean(temperaturas[i, :, semana])
            print(f"  Semana {semana + 1}: {promedio:.2f} °C")

# Llamada a la función para calcular el promedio
calcular_promedio_temperaturas(ciudades, temperaturas, semanas)

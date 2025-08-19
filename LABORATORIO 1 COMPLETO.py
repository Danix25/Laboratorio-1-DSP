import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

# === CARGAR SEÑAL DE PHYSIONET ===
x = loadmat(r'C:\Users\DELL\Desktop\intento 2 lab 1\100m.mat')
ecg = (x['val'][0]) / 200  # Escalar señal

# === FUNCIONES DESDE CERO ===

def calcular_media(ecg):
    suma = 0
    for valor in ecg:
        suma += valor
    return suma / len(ecg)

def calcular_desviacion_estandar(ecg):
    media = calcular_media(ecg)
    suma = 0
    for valor in ecg:
        suma += (valor - media) ** 2
    return (suma / len(ecg)) ** 0.5

def calcular_coeficiente_variacion(ecg):
    media = calcular_media(ecg)
    desv = calcular_desviacion_estandar(ecg)
    return desv / media

def calcular_histograma(ecg, bins=10):
    minimo = min(ecg)
    maximo = max(ecg)
    ancho = (maximo - minimo) / bins
    frecuencias = [0] * bins
    for valor in ecg:
        indice = int((valor - minimo) / ancho)
        if indice == bins:
            indice -= 1
        frecuencias[indice] += 1
    bordes = [minimo + i * ancho for i in range(bins + 1)]
    return frecuencias, bordes

def calcular_funcion_probabilidad(ecg, bins=10):
    frecuencias, bordes = calcular_histograma(ecg, bins)
    total = sum(frecuencias)
    probabilidades = [f / total for f in frecuencias]
    return probabilidades, bordes

def calcular_curtosis(ecg):
    media = calcular_media(ecg)
    desv = calcular_desviacion_estandar(ecg)
    suma = 0
    for valor in ecg:
        suma += ((valor - media) / desv) ** 4
    return suma / len(ecg)

# === GRAFICAR SEÑAL ORIGINAL ===
fs = 360  # frecuencia de muestreo
ts = 1/fs
t = np.linspace(0, len(ecg)*ts, len(ecg))

plt.figure(figsize=(10, 4))
plt.plot(t, ecg)
plt.title("Señal ECG original")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()

# === GRAFICAR HISTOGRAMA ===
frecuencias, bordes = calcular_histograma(ecg, bins=20)
centros = [(bordes[i] + bordes[i+1]) / 2 for i in range(len(frecuencias))]

plt.figure(figsize=(8, 4))
plt.bar(centros, frecuencias, width=(bordes[1] - bordes[0]), edgecolor='black')
plt.title("Histograma de la señal")
plt.xlabel("Amplitud")
plt.ylabel("Frecuencia")
plt.grid(True)
plt.show()

# === GRAFICAR FUNCIÓN DE PROBABILIDAD ===
probabilidades, bordes = calcular_funcion_probabilidad(ecg, bins=20)
centros = [(bordes[i] + bordes[i+1]) / 2 for i in range(len(probabilidades))]

plt.figure(figsize=(8, 4))
plt.plot(centros, probabilidades, marker='o', linestyle='-')
plt.title("Función de probabilidad (estimada)")
plt.xlabel("Amplitud")
plt.ylabel("Probabilidad")
plt.grid(True)
plt.show()

# === MOSTRAR RESULTADOS NUMÉRICOS ===
print("Estadísticos descriptivos (desde cero):")
print("Media:", calcular_media(ecg))
print("Desviación estándar:", calcular_desviacion_estandar(ecg))
print("Coeficiente de variación:", calcular_coeficiente_variacion(ecg))
print("Curtosis:", calcular_curtosis(ecg))

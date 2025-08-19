import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kurtosis, gaussian_kde

# ==== 1) Cargar datos ====
ruta = "C:\\Users\\DELL\\Downloads\\RigolDS0.txt"
tiempo, voltaje = np.loadtxt(ruta, delimiter=",", skiprows=1, unpack=True)

# ==== 2) Graficar señal (morada) ====
plt.figure(figsize=(10,4))
plt.plot(tiempo, voltaje, color='purple')
plt.title("Señal fisiológica")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (V)")
plt.grid(True)
plt.show()

# ==== 3) Estadísticos desde cero ====
N = len(voltaje)
media = sum(voltaje) / N
desviacion = (sum((x - media)**2 for x in voltaje) / (N - 1))**0.5
coef_var = desviacion / media
curt = kurtosis(voltaje)

print(f"Media: {media}")
print(f"Desviación estándar: {desviacion}")
print(f"Coeficiente de variación: {coef_var}")
print(f"Curtosis: {curt}")

# ==== 4) Histograma (morado) ====
plt.figure(figsize=(6,4))
plt.hist(voltaje, bins=30, density=True, color='purple', edgecolor='black')
plt.title("Histograma de la señal")
plt.xlabel("Amplitud (V)")
plt.ylabel("Frecuencia relativa")
plt.show()

# ==== 5) Función de probabilidad (KDE en morado) ====
kde = gaussian_kde(voltaje)
x_vals = np.linspace(min(voltaje), max(voltaje), 500)
pdf_vals = kde(x_vals)

plt.figure(figsize=(6,4))
plt.plot(x_vals, pdf_vals, color='purple')
plt.title("Función de probabilidad estimada (KDE)")
plt.xlabel("Amplitud (V)")
plt.ylabel("Densidad de probabilidad")
plt.grid(True)
plt.show()


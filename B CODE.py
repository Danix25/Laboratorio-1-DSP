import matplotlib.pyplot as plt
import numpy as np
from scipy.io import loadmat
from scipy.stats import kurtosis, gaussian_kde


x = loadmat(r'C:\Users\DELL\Desktop\intento 2 lab 1\100m.mat')
ecg = (x['val'][0]) / 200

fs = 360  # Frecuencia de muestreo
ts = 1 / fs
t = np.linspace(0, len(ecg) * ts, len(ecg))

plt.figure(figsize=(10, 4))
plt.plot(t, ecg, color='red')
plt.title('Señal ECG')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [mV]')
plt.grid(True)
plt.tight_layout()
plt.show()

# -----------------------------------------
# 2. ESTADÍSTICOS DESCRIPTIVOS 
# -----------------------------------------

media = np.mean(ecg)
desviacion = np.std(ecg)
cv = desviacion / media
curt = kurtosis(ecg, fisher=False)  # Curtosis normal = 3

# -----------------------------------------
# 3. HISTOGRAMA
# -----------------------------------------

plt.figure(figsize=(8, 4))
plt.hist(ecg, bins=50, color='red', edgecolor='black')
plt.title('Histograma de la señal ECG')
plt.xlabel('Amplitud [mV]')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.tight_layout()
plt.show()

# -----------------------------------------
# 4. FUNCIÓN DE PROBABILIDAD 
# -----------------------------------------

kde = gaussian_kde(ecg)
x_vals = np.linspace(min(ecg), max(ecg), 1000)
pdf_vals = kde(x_vals)

plt.figure(figsize=(8, 4))
plt.plot(x_vals, pdf_vals, color='red')
plt.title('Función de Probabilidad Estimada (KDE)')
plt.xlabel('Amplitud [mV]')
plt.ylabel('Densidad')
plt.grid(True)
plt.tight_layout()
plt.show()

# -----------------------------------------
# 5. MOSTRAR RESULTADOS
# -----------------------------------------

print("\n--- RESULTADOS ESTADÍSTICOS DESCRIPTIVOS ")
print(f"Media: {media:.4f}")
print(f"Desviación estándar: {desviacion:.4f}")
print(f"Coeficiente de variación: {cv:.4f}")
print(f"Curtosis: {curt:.4f}")


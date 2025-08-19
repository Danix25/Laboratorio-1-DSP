import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# === 1. Cargar señal desde archivo CSV ===
archivo = r"C:\Users\DELL\Downloads\RigolDS0.csv"  # Cambia si está en otra ruta
df = pd.read_csv(archivo, skiprows=19)

# === 2. Extraer señal y tiempo ===
df.columns = ['Tiempo', 'Voltaje']
df.dropna(inplace=True)
tiempo = df['Tiempo'].values
senal = df['Voltaje'].values

# === 3. Función para calcular SNR ===
def calcular_snr(senal_original, senal_ruidosa):
    ruido = senal_ruidosa - senal_original
    potencia_senal = np.mean(senal_original**2)
    potencia_ruido = np.mean(ruido**2)
    snr = 10 * np.log10(potencia_senal / potencia_ruido)
    return snr

# === 4. Añadir ruido gaussiano ===
np.random.seed(0)
ruido_gauss = np.random.normal(0, 0.1, len(senal))
senal_gauss = senal + ruido_gauss
snr_gauss = calcular_snr(senal, senal_gauss)

# === 5. Añadir ruido impulsivo ===
prob_impulso = 0.01
impulsos = np.random.choice([0, 1], size=len(senal), p=[1 - prob_impulso, prob_impulso])
magnitud = np.random.normal(0, 2, len(senal))
ruido_impulso = impulsos * magnitud
senal_impulso = senal + ruido_impulso
snr_impulso = calcular_snr(senal, senal_impulso)

# === 6. Añadir ruido tipo artefacto ===
fs = 1 / np.mean(np.diff(tiempo))
frecuencia_artefacto = 220

artefacto = 0.2 * np.sin(2 * np.pi * frecuencia_artefacto * tiempo)
senal_artefacto = senal + artefacto
snr_artefacto = calcular_snr(senal, senal_artefacto)

# === 7. Mostrar SNRs ===
print("SNR - Gaussiano:     ", round(snr_gauss, 2), "dB")
print("SNR - Impulsivo:     ", round(snr_impulso, 2), "dB")
print("SNR - Artefacto:     ", round(snr_artefacto, 2), "dB")

# === 8. Gráfica SOLO de la señal original ===
plt.figure(figsize=(10, 4))
plt.plot(tiempo, senal, label='Señal original')
plt.title('Señal original')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
plt.grid(True)
plt.tight_layout()
plt.savefig('senal_original.png')  # Guarda la imagen
plt.show()

# === 9. Gráfica de señales con ruido ===
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(tiempo, senal_gauss)
plt.title('Señal con ruido gaussiano')

plt.subplot(3, 1, 2)
plt.plot(tiempo, senal_impulso)
plt.title('Señal con ruido impulsivo')

plt.subplot(3, 1, 3)
plt.plot(tiempo, senal_artefacto)
plt.title('Señal con ruido tipo artefacto')

plt.tight_layout()
plt.savefig('senal_con_ruidos.png')  # Guarda la imagen
plt.show()

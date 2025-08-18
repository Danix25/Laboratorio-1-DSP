# Laboratorio 1 PROCESAMIENTO DIGITAL DE SEÑALES 

# TABLA DE CONTENIDOS
1. Objetivos y metodología del experimento.
2. Diagrama de flujo.
3. Adquisición de la señal.
4. Análisis de resultados.
5. Conclusiones.
6. Aplicaciones biomédicas.

# 1. Objetivos y metodología del experimento.

La presente práctica, tiene como objetivo general el identificar los estadisticos que describen una señal fisiológica y obtenerlos a partir de algoritmos de programación para mostrarlos, empleando técnicas como el cálculo de la media de la señal, la desviación estándar, el coeficiente de variación, histogramas y función de probabilidad. 
Además, se estudio la relación señal ruido (SNR), el cual se basa en la relación entre la información deseada y la potencia de un ruido de fondo. Esto es un parámetro de medición que se mide en decibelios (dB) y es ampliamente usado en ciencias e ingeniería.
Recordemos que histogramas representa el rango de amplitudes de una señal, el coeficiente de variación es la relación entre la desviación estándar y la media; mide la variabilidad relativa.

# 2. Diagrama de flujo.

Parte A

<img width="761" height="878" alt="image" src="https://github.com/user-attachments/assets/bdd01da1-afaa-4ac5-ba25-123f65668f6d" />

Parte B

<img width="367" height="882" alt="image" src="https://github.com/user-attachments/assets/49cd3f1c-6cd6-4eae-b737-9fdc12f2984a" />

Parte C

<img width="783" height="642" alt="image" src="https://github.com/user-attachments/assets/efc3bfbc-dbab-4bfc-aa3d-8cbdf16f2e2d" />



# 3. Adquisición de la señal.
La señal electrocardiográfica (ECG) fue adquirida primeramente importando una señal de 'Physionet' en python, para luego graficar sus datos y obtener sus valores estadísticos. En segundo lugar, se capturó la señal en tiempo real, usando un generador de señale fisiológicas para luego guardarla en un archivo de texto e importarla al programa de código.

# 4. Análisis de resultados.

# Parte A

Para la señal importada de 'Physionet', se obtuvo la siguiente señal, corriespondiente a una de Electrocardiografía:

<img width="921" height="412" alt="image" src="https://github.com/user-attachments/assets/f6dbc81b-711a-49d6-a593-51effcf6efcc" />

Luego de ello, se aplicaron las formulas estadísticas sin usar las funciones pre-escritas por Python, en donde se obtuvo una media de datos de -0.2031, con una desviación de 0.1225, un coeficiente de variación de -0.6030 y una curtosis de 23.7665. Estos valores representan los valores normales para un ECG y para visualizar mejor los datos, se calculó el histograma y la función de probabilidad, obteniendo los siguientes datos.

<img width="921" height="494" alt="image" src="https://github.com/user-attachments/assets/fa330b8e-17af-476b-9b77-e9e44960a0a9" />
<img width="921" height="525" alt="image" src="https://github.com/user-attachments/assets/3f94a9cf-04fa-4d7a-a00e-c92e68ecf854" />

Para corroborar los datos calculados previamente, se usaron las funciones pre-escritas por Python, en las cuales se evidencia una mayor precisión. Para la media se obtuvo un valor de -0.2032, una desviación de 0.1225, un coeficiente de variación de -0.6030 y una curtosis de 20.7665. En cuanto al histograma y la función de probabilidad se evidenciaron ciertas diferencias con las primeras gráficas obtenidas, siendo estas ultimas mucho más precisas.

Para el histograma, en la primera gráfica hubo un pico de frecuencia de 1400 Hz a una amplitud de -0.2 mV. Para la segunda, se obtuvo un pico de 600 Hz a una amplitud próxima de -0.2 mV, ssiendo esta mucho más precisa.

En cuanto a la función de probabilidad, primero se obtuvo una probabilidad de 0.4 en una amplitud de -0.2 mV y para la siguiente, se evidencia una densidad de 6 a la misma amplitud. Esto nos muestra que al aplicar las funciones pre-escritas, nos genera más precisión y confianza a la hora de calcular datos estadísticos. 

<img width="921" height="454" alt="image" src="https://github.com/user-attachments/assets/7446cef9-93b5-4d0f-975c-086eadde41fb" />
<img width="921" height="457" alt="image" src="https://github.com/user-attachments/assets/df43bb42-599d-48ab-a4c6-e67f91dae86b" />

# Parte B

<img width="921" height="421" alt="image" src="https://github.com/user-attachments/assets/ef35e52d-b425-498e-8310-a8a35afea10f" />

Para la señal capturada por el generador de señales fisiológicas se obtuvo una gráfica más idealizada, asumiendo que sus datos serán más exactos. Para esta señal, se obtuvo una media de -0.5453, una desviación de 0.2639, un coeficiente de variación de -0.4840) y una curtosis de 19.1881. Luego de ello, se hizo el histograma y la gráfica de la función de probabilidad, obteniendo lo siguiente:

<img width="908" height="655" alt="image" src="https://github.com/user-attachments/assets/93d9e76b-bff5-4b12-a6fc-4eb9fce21d9a" />
<img width="888" height="656" alt="image" src="https://github.com/user-attachments/assets/398a7c7a-f1e2-4fcf-a524-66c3b39f8755" />

# Parte C

Por ultimo, con la señal previamente capturada, se le agregaron una serie de ruidos para conocer la relación señal - ruido (SNR). En primer lugar se agregó un ruido gaussiano, el cual se pasa principalmente en agregar valores aleatorios sobre la gráfica, que tienden a agruparse alrededor de un valor medio y por tal razón, se evidencia un ruido sobre los valores medios de la señal. La relacion señal - ruido (SNR) fue de 15.65 dB

Seguido de esto, se agregó un ruido impulso a la señal original, basado principalmente en picos repentinos y que se caracterizan principalmente por tener  una amplitud alta, en comparación con la señal original. Por esto, se evidencia en la gráfica mucho ruido y con gran dificultad para interpretar la señal original. El SNR para esta señal fue de 9.63 dB

Finalmente, se agrega un ruido de tipo artefacto a la señal original, la cual consiste en la manifestación de ondulaciones regulares a una frecuencia de línea. Dicho ruido se puede ver en la señal, ya que se evidencias ciertas ondulaciones sobre ella y con un SNR de 12.93 dB

<img width="921" height="632" alt="image" src="https://github.com/user-attachments/assets/f8b498bf-f0bf-46c7-bf23-ffa2f961d9b3" />

# 5. Conclusiones.

Parte A – Señal descargada
La señal fisiológica importada physionet permitió calcular estadísticos descriptivos que reflejan sus características fundamentales. La media y desviación estándar fueron consistentes entre el cálculo de la programación de  las formulas desde cero; y las librerías, validando la implementación. El histograma mostraron la distribución de amplitudes con una curtosis propia de señales.

Parte B – Señal adquirida
La señal capturada por medio del generador de señales y el osciloscopio reprodujo el patrón esperado, aunque presentó ligeras variaciones respecto a la señal de base de datos. Los estadísticos descriptivos de la señal propia fueron comparables a los de la señal descargada, evidenciando coherencia en la metodología. No obstante, se observaron pequeñas diferencias atribuibles al hardware de adquisición y al ruido intrínseco del entorno.

Comparación A vs B
El análisis comparativo demostró que, pese a las diferencias en origen, ambas señales comparten propiedades estadísticas similares. Esto valida la práctica de usar señales sintéticas o adquiridas como representaciones de fenómenos fisiológicos para el aprendizaje y análisis de DSP biomédico.

Parte C – Contaminación y SNR
La introducción de ruido gaussiano, impulsivo y artefactos permitió evidenciar cómo disminuye la relación señal-ruido (SNR). El ruido gaussiano afectó de manera global la amplitud, el impulsivo generó picos que distorsionan los estadísticos, y el artefacto de línea desplazó la forma de onda. La medición de SNR cuantificó estas diferencias y evidenció la vulnerabilidad de las señales fisiológicas a distintos tipos de contaminación.

Conclusión general
Se cumplió el objetivo de aplicar estadística descriptiva, adquisición y análisis de señales fisiológicas. Se comprobó la importancia del preprocesamiento, la estimación de SNR y la documentación en GitHub.


# 6. Aplicaciones biomédicas
El calculo de valores estadísticos en señales fisiológicas, son muy útiles para su análisis, ya que nos permiten extraer información para entender el comportamiento y distribución de las señales. Esto se puede evidenciar en los siguiente casos:

- ECG (Electrocardiografía): Para este tipo de señales, los estadísticos nos permiten: normalizar la señal, visualizar la variabilidad de la señal y detectar latidos anormales-
- EMG (Electromiografía): En estas señales, los calculos estadísticos nos permiten cuantificar la acción muscular, diferenciar entre contracciones normales y movimientos anormales, además de detectar enfermedades como Parkinson.
- Presión arterial: Aquí, se puede visualizar la variación de la presión arterial, siendo importante para el diagnostico de hipertensión.

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

<img width="708" height="892" alt="image" src="https://github.com/user-attachments/assets/7f2861cd-c260-4066-aa4d-898e1d654db3" />


# 3. Adquisición de la señal.
La señal electrocardiográfica (ECG) fue adquirida primeramente importando una señal en Physionet, para luego mostrar en python la gráfica 
# 4. Análisis de resultados.
# Parte A
Señal importada

<img width="921" height="412" alt="image" src="https://github.com/user-attachments/assets/f6dbc81b-711a-49d6-a593-51effcf6efcc" />

Aplicando las formulas

<img width="921" height="494" alt="image" src="https://github.com/user-attachments/assets/fa330b8e-17af-476b-9b77-e9e44960a0a9" />
<img width="921" height="525" alt="image" src="https://github.com/user-attachments/assets/3f94a9cf-04fa-4d7a-a00e-c92e68ecf854" />

Aplicando las funciones de código

<img width="921" height="454" alt="image" src="https://github.com/user-attachments/assets/7446cef9-93b5-4d0f-975c-086eadde41fb" />
<img width="921" height="457" alt="image" src="https://github.com/user-attachments/assets/df43bb42-599d-48ab-a4c6-e67f91dae86b" />

# Parte B
Señal capturada

<img width="921" height="421" alt="image" src="https://github.com/user-attachments/assets/ef35e52d-b425-498e-8310-a8a35afea10f" />
calculos:
<img width="908" height="655" alt="image" src="https://github.com/user-attachments/assets/93d9e76b-bff5-4b12-a6fc-4eb9fce21d9a" />
<img width="888" height="656" alt="image" src="https://github.com/user-attachments/assets/398a7c7a-f1e2-4fcf-a524-66c3b39f8755" />

# Parte C
Señal contaminada

<img width="921" height="632" alt="image" src="https://github.com/user-attachments/assets/f8b498bf-f0bf-46c7-bf23-ffa2f961d9b3" />
Podemos ver  el ruido gausiano es un tipo de interfernecia estatica que afecta a toda la señal o es ruido aleatorio y normalmente sigue la curva gaussiana conocida como la curva de campana,  en el ruido impulsivo son interferencias que son rapidas y de forma "inesperadas" y se puede comparar como si fueran salpicadoras y por ultimo el tipo artefacto  se observa como una patron ondulatorio el  cual se puede ver en la imagen donde sube y baja en forma senoidal.

# 5. Conclusiones.
El  histograma  muestra  la  distribución  de  amplitud  con  una  curvatura  típica  de  las  señales.

 Parte  B  –  Señal  adquirida
 La  señal  capturada  por  el  generador  de  señales  y  el  osciloscopio  reprodujo  el  patrón  esperado,  a  pesar  de  ligeras
 Variaciones  de  la  señal  de  la  base  de  datos. 
 comparables  a  los  de  la  señal  descargada,  lo  que  demuestra  la  consistencia  de  la  metodología.  Sin  embargo,  se  observaron  ligeras  diferencias.
 Se  observaron  ruidos  atribuibles  al  equipo  de  adquisición  y  al  ruido  ambiental.

 Comparación  A  vs  B
 El  análisis  comparativo  demostró  que,  a  pesar  de  sus  diferencias  en  el  origen  (base  de  datos  o  señal  adquirida),  la
 Dos  señales  comparten  propiedades  estadísticas  similares.

 Parte  C  –  Contaminación  y  relación  señal ruido  (SNR)
 La  introducción  de  ruido  gaussiano,  impulsivo  y  artefactual  reveló  la  disminución  de  la  relación  señal ruido  (SNR).
 El  ruido  gaussiano  afectó  la  amplitud  general,  el  ruido  impulsivo  generó  picos  que  distorsionaron  las  estadísticas  y  el  artefacto
 La  línea/línea  base  alteró  la  forma  de  onda.  Las  mediciones  de  SNR  cuantificaron  estas  diferencias  y
 demostró  la  vulnerabilidad  de  las  señales  fisiológicas  a  diferentes  tipos  de  contaminación.

 Conclusión  general

 Se  ha  logrado  el  objetivo  de  aplicar  estadística  descriptiva,  adquisición  y  análisis  de  señales  fisiológicas.  La  importancia
 Se  ha  demostrado  el  preprocesamiento,  la  estimación  de  SNR  y  la  documentación  de  GitHub.
# 6. Aplicaciones biomédicas


 Diagnóstico  médico  asistido  por  computadora  (CAD)
 El  análisis  estadístico  (media,  desviación  estándar,  curtosis)  permite  detectar  anomalías  en  señales  como  ECG,  EEG  o  EMG.
 La  curtosis  alta  en  el  EEG  puede  estar  asociada  con  actividad  convulsiva.

 Monitoreo  en  tiempo  real.
 En  las  unidades  de  cuidados  intensivos,  la  estimación  estadística  rápida  puede  identificar  cambios  repentinos  en  la  frecuencia  cardíaca  o  la  respiración.
 La  monitorización  de  la  relación  señal ruido  (SNR)  es  esencial  para  garantizar  que  las  alarmas  no  se  activen  por  artefactos  de  ruido.

 Investigación  en  neurociencia  y  rehabilitación.
 En  EMG  o  EEG,  la  relación  señal ruido  determina  la  detección  de  movimientos  voluntarios  o  motores.
 intenciones.  Esto  es  esencial  para  prótesis  controladas  neuronalmente  o  sistemas  de  interfaz  cerebrocomputadora.

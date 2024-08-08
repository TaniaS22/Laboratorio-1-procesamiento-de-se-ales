# Laboratorio 1 Procesamiento  Digital de Señales: Análisis estadístico de la señal 
Autores: Fabián Alberto López Lemus y Tania Angélica Sandoval Ramírez
## Introducción
El propósito del presente laboratorio es profundizar las técnicas estadísticas utilizadas en el análisis de señales biomédicas, aprendiendo a buscar señales biomédicas en repositorios como physionet con el fin de tener señales las cuales no solo pertenecen al campo de interés, sino que también permiten observar él antes y después de realizar un procesamiento a la señal. En este caso se escogió una señal de un ECG hecho a pacientes con apnea, cada registro usado incluye una señal de ECG digitalizada continua, un conjunto de anotaciones de apnea (derivadas por expertos humanos sobre la base de la respiración registrada simultáneamente y señales relacionadas) y un conjunto de anotaciones QRS generadas por máquina; En resumen, señales de esfuerzo respiratorio torácico y abdominal obtenidas mediante pletismografía de inductancia.<br>
<br>
Para cumplir con todos los objetivos se utilizó el lenguaje de programación Python, en el cual se realizó la importación, muestra y tratamiento de los datos mencionados anteriormente(**para terceros se recomienda usar el software "Anaconda Navigator con su herramienta "Spider"**), al final de este repositorio se encontraran las instrucciones para poder usar el código de manera adecuada.

## Procesamiento de la señal
## Análisis estadístico
Una vez se decidió la señal que sería usada("a03"), se descargó de [Physionet](https://physionet.org/content/apnea-ecg/1.0.0/) teniendo en cuenta que se tienen que descargar 2 archivos que se llamen igual, pero que tengan las extensiones .hea y .dat, una vez con estos archivos se hizo uso de la librería llamada "Waveform Database" o por sus siglas wfdb para poder importar los datos de la señal a Python y poder obtener sus valores y la longitud del arreglo, de la siguiente manera: 

```python
import wfdb
signal = wfdb.rdrecord('a03')
valores = signal.p_signal
tamaño = signal.sig_len
```
<br>
Una vez obtenida la señal era momento de mostrarla para poder observar lo que se denominó "señal original", esto se hizo usando la librería "Matplotlib" obteniendo la siguiente señal:
<br>
<br>

![Senal original](https://drive.google.com/uc?export=view&id=1Nq-gbisaOD_8Kpf-NBYKOK_pXGg7xiUb)

Una vez se confirmó que la señal se importó de manera correcta a Python, se procedió con la primera parte del laboratorio la cual se basa en el estudio estadístico de la señal, en el cual se realizan diferentes medidas estadísticas tanto por fórmula como por comando de librerías de Python; para esta parte es crucial importar las siguientes librerías: Matplotlib, NumPy, math y SciPy.


### Media estadística
Como su nombre lo dicta es el valor promedio en el que se mantiene la señal(en este caso en unidades de la escala de Voltios), para la parte con fórmula se usó la siguiente fórmula y se implementó en el código de la siguiente manera:
<br>
<br>
![media](https://quicklatex.com/cache3/e9/ql_529238be61b9b711ea08fd55cd745ee9_l3.png)

```python
media = np.mean(valores)
print("La media de la señal es:", media)
```

En ambos casos se obtuvo un valor de **0.00102** aproximadamente

### Desviación estándar

La desviación estándar indica la dispersión o variación del conjunto de datos que se tiene, para encontrarla se utiliza la siguiente fórmula y se implementó por código así:
<br>
<br>
![Desviacion estandar](https://quicklatex.com/cache3/c9/ql_35e276e65637c4608038eba6cea6e8c9_l3.png)

```python
desviacion_estandar = np.std(valores)
print("La desviacion estandar de la señal es:", desviacion_estandar)
```
<br>

En ambos casos se obtuvo un valor de **0.4449** aproximadamente

### Coeficiente de variación 
El coeficiente de variación indica que tanto cambia una variable en función de la otra, en este caso que tanto cambia la amplitud respecto al tiempo, para la parte con fórmula se usó la siguiente fórmula y se implementó en el código de la siguiente manera:
<br>
<br>
![Coeficiente de variacion](https://quicklatex.com/cache3/94/ql_1e34d0d4e0591516687ef56b0dd03694_l3.png)

```python
C_variacion = variation(valores)
print("El coeficiente de variacion de la señal es:", C_variacion)
```
<br>

En ambos casos se obtuvo un valor de **435.4675** aproximadamente
<br>
### Histograma y Función de probabilidad
El histograma y la función de probabilidad están interconectados, por eso se decidió unir los resultados en una sola parte. Estos se realizaron por fórmula; sin embargo, es más simple para el usuario mostrar los resultados obtenidos, ya que en el código se encuentra indicado en que parte se hacen las modificaciones a los mismos:
<br>
<br>
![Histograma](https://drive.google.com/uc?export=view&id=1gH-x2WzdD5oh5uOKuq1KVC9wJTtaKf6D) ![Funcion de probabilidad](https://drive.google.com/uc?export=view&id=1m2sgsltka0-iiEm1dLqA9y7J9f3RD_0r)

## Relación señal ruido (SNR)
La Relación señal ruido es la relación entre la potencia de una señal útil y la potencia del ruido de fondo. Se utiliza para medir la calidad de la señal; un SNR más alto indica una señal más clara y menos afectada por el ruido; se utiliza la siguiente fórmula:
<br>
<br>
![SNR](https://quicklatex.com/cache3/2f/ql_51d12e518023d4d41be035e9f8e68f2f_l3.png)

### Ruido gaussiano 
El ruido gaussiano es un tipo de ruido que tiene una distribución de probabilidad normal (gaussiana), caracterizada por su media y desviación estándar; debido a esto dependiendo de cierto valor que será mencionado después, los valores de SNR cambian dependiendo de cuanta desviación estándar se le coloque a la ecuación(En este casi **0.5**), los resultados obtenidos fueron: 
<br>
<br>
![Gaussiano](https://drive.google.com/uc?export=view&id=1dRuoYXGvYfdgrtF0axQyYVFrbrICOPhz)

### Ruido tipo impulso
El ruido tipo impulso es un tipo de ruido que se manifiesta como picos repentinos y breves en la señal, debido a eventos esporádicos o fallos en el sistema; para este caso se tuvo que implementar el nivel del ruido y la probabilidad de que ocurriera un impulso, ambos son valores que se pueden manipular para afectar no solo la señal sino también el nivel del SNR, en este caso con un nivel de ruido de **0.8** y una probabilidad de impulso del **0.05** se obtuvo la siguiente gráfica:
<br>
<br>
![impulso](https://drive.google.com/uc?export=view&id=1zL0GFKqSwFlB2ru0pAaJDoY7_orEz9uj)

### Ruido tipo artefacto 
El ruido tipo artefacto es un ruido no deseado en una señal que se origina por defectos o interferencias en el sistema de medición o procesamiento, como fallos en el hardware o errores en la adquisición de datos; este tipo de ruido es aleatorio, por lo que se usa una función que genere una onda aleatoria, la cual también usa una desviación estándar de **0.5**, obteniendo así la siguiente gráfica:
<br>
<br>
![impulso](https://drive.google.com/uc?export=view&id=1CTO9oftJyyHk6YvR-k4NEci5NUXMdHsO)

# Instrucciones para el usuario 
Para evitar problemas se le recomienda al usuario usar la versión 3.10 de Python y no modificar nada de lo que no se mencione en los siguientes pasos, ya que el código generara las demás cosas de manera automática. Además, se recomienda usar datos de una dimensión o un vector (si no se tienen de esa forma convertirlos a un solo vector)

1. importar las siguientes librerías luego de instalarlas previamente
   
```python
import wfdb 
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import variation
```
2. Descargar los archivos .hea y .dat de una señal de la página web [Physionet](https://physionet.org/about/database/)
3. Cargar los datos descargados anteriormente de la siguiente forma (línea 21 de código)
```python
signal = wfdb.rdrecord('nombre_de_sus_archivos')
```
4. Una vez teniendo esto se obtienen automáticamente las siguientes cosas: los valores de la señal, la longitud(o tamaño) del arreglo, se muestra la gráfica de sus datos, La media, la desviación estándar y el coeficiente de variación.
5. para el histograma y la función de probabilidad se usa algo llamado "bins", que se podría decir que son los intervalos en los que se agrupan los datos, a menor número de bins menor número de barras y viceversa, estos se modifican en la línea 84, 104 y 138; donde se muestra(**_del usuario depende cuantos bins colocar en cada uno de estos, ya que dependerá de la señal utilizada_**):
```python
#histograma por formula(linea 84)
num_bins = "numero deseado de bins sin comillas"

#histograma por codigo(linea 104)
plt.hist(valores, bins="numero deseado de bins sin comillas")

#funcion de probabilidad por codigo(linea 138)
count, bins = np.histogram(valores, bins="numero deseado de bins sin comillas", density=True)
```
6. Para la parte de los ruidos, el valor de SNR depende de la variación estándar que se le quiera permitir a la señal del ruido, ya que esta se normaliza o estandariza de forma automática
<br>
   a. Para el ruido gaussiano (linea 162)
   
 ```python
noise_level = np.std(valores)*"valor de desviacion estandar que se desea sin comillas"
```
   b. Para el ruido impulso se debe poner el nivel del ruido que se desea y la probabilidad que ocurra un impulso(línea 235 y línea 249/251)
```python
#linea 235
def add_impulse_noise(signal, noise_level="nivel de ruido deseado sin comillas", impulse_probability="probabilidad de que un impulso ocurra sin comillas"):
#lineas 249 y 251
noise_level = "nivel de ruido deseado sin comillas"

impulse_probability = "probabilidad de que un impulso ocurra sin comillas"
```
   c. Para ruido artefacto también se modifica la desviación estándar, que es con un tipo de tolerancia que tiene la onda para producir el ruido (línea 313)
```python
ruido = np.random.normal(0, "valor de desviacion estandar que se desea sin comillas", tamaño)  
```
### Uso 
Por favor, cite este artículo:
<br>
Goldberger, A., Amaral, L., Glass, L., Hausdorff, J., Ivanov, P. C., Mark, R., ... & Stanley, H. E. (2000). PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals. Circulation [Online]. 101 (23), pp. e215–e220
### Informacion de contacto
est.fabiana.lopez@unimilitar.edu.co
<br>
est.tania.sandoval@unimilitar.edu.co

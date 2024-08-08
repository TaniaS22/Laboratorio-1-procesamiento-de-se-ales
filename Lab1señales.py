# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 15:29:12 2024

@author: Tania Sandoval y Fabian Lopez
"""
#importar paquete wfdb para leer "records" de physionet

import wfdb 

import matplotlib.pyplot as plt

import numpy as np

import math

from scipy.stats import variation

#cargar la informacion (hay que tener los archivos .dat y .hea)

signal = wfdb.rdrecord('a03')

#obtener los valores de Y en la señal

valores = signal.p_signal

tamaño = signal.sig_len #numero de muestras

print(valores)

plt.plot(valores,label='Señal de ECG-APNEA')

plt.title('Señal de ECG-APNEA obtenida de physionet')

plt.xlabel('Muestras (t en s)')

plt.ylabel('Amplitud (mV)')

plt.legend()
# calculo de la media estadistica de la señal por medio de formula 

sumita = sum(valores)

media_formula = sumita/tamaño

print("La media por formula de la señal es:", media_formula)

# calculo de la media estadistica por comando es

media = np.mean(valores)

print("La media de la señal es:", media)

# calculo de la desviacion estandar de la señal por medio de formula 

suma_de_cuadrados = sum((x - media_formula)**2 for x in valores)

varianza = suma_de_cuadrados/(tamaño-1)

desviacion_estandar_formula = math.sqrt(varianza)

print("La desviacion estandar por formula de la señal es:", desviacion_estandar_formula)

# calculo de la desviacion estandar por comando es

desviacion_estandar = np.std(valores)

print("La desviacion estandar de la señal es:", desviacion_estandar)

# calculo de el coeficiente de variacion de la señal por medio de formula 

C_variacion_formula = (desviacion_estandar_formula/media_formula)

print("El coeficiente de variacion por formula de la señal es:", C_variacion_formula)

# calculo de el coeficiente de variacion de la señal

C_variacion = variation(valores)

print("El coeficiente de variacion de la señal es:", C_variacion)

#histograma por formula

num_bins = 50  

hist_values, bin_edges = np.histogram(valores, bins=num_bins)

bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

plt.figure(figsize=(10, 6))

plt.bar(bin_centers, hist_values, width=bin_edges[1] - bin_edges[0], edgecolor='k', alpha=0.7)

plt.title('Histograma por formula')

plt.xlabel('Muestras (t en s)')

plt.ylabel('Amplitud (mV)')

plt.show()

#histograma por codigo 

plt.hist(valores, bins=100)  

plt.title("Histograma por codigo")

plt.xlabel('Muestras (t en s)')

plt.ylabel('Amplitud (mV)')

plt.show()

#funcion de probabilidad por formula 

bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

bin_width = bin_edges[1] - bin_edges[0]

pdf_values = hist_values / (sum(hist_values) * bin_width)

plt.figure(figsize=(10, 6))

plt.plot(bin_centers, pdf_values, marker='o', linestyle='-', color='b', label='funcion de probabilidad')

plt.title('Función de Densidad de Probabilidad por formula')

plt.xlabel('Muestras (t en s)')

plt.ylabel('Amplitud (mV)')

plt.legend()

plt.show()

#funcion de probabilidad por codigo

count, bins = np.histogram(valores, bins=100, density=True)

bin_centers = 0.5 * (bins[:-1] + bins[1:])

plt.plot(bin_centers, count, label='funcion de probabilidad')

plt.title('Función de probabilidad por codigo')

plt.xlabel('Muestras (t en s)')

plt.ylabel('Amplitud (mV)')

plt.legend()

plt.show()

#Ruido gausiano
 
def ruidoG(signal, noise_level):
    
    ruidito = np.random.normal(0, noise_level, signal.shape)
    
    return signal + ruidito

noise_level = np.std(valores)*0.5

valores_contaminados = ruidoG(valores, noise_level)

def SNR(signal, noise_level):
    
    Pseñal = np.mean(signal**2)
    
    Pruido = noise_level**2
    
    snr = 10 * np.log10(Pseñal / Pruido)
    
    return snr

snr = SNR(valores, noise_level)

print("el SNR obtenido por ruido gaussiano es:", snr)

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)

plt.plot(valores, color='blue', label='señal original')

plt.title('Señal Original')

plt.xlabel('Muestras (t en s)')

plt.ylabel('Amplitud (mV)')

plt.legend()

plt.subplot(2, 1, 2)

plt.plot(valores_contaminados, color='red', label='señal contaminada con ruido gaussiano')

plt.title('Señal Contaminada con Ruido Gaussiano')

plt.xlabel('Muestras (t en s)')

plt.ylabel('Amplitud (mV)')

plt.tight_layout()

plt.legend()

plt.show()

plt.figure(figsize=(12, 6))

plt.plot(valores, label='Señal Original', color='r')

plt.plot(valores_contaminados, label='Señal Contaminada(Gaussiano)', alpha=0.7)

plt.title('Comparación de la Señal Original y la Señal Contaminada(Gaussiano)')

plt.xlabel('Muestras (t en s)')

plt.ylabel('Amplitud (mV)')

plt.legend()

plt.show()

#Ruido impulso

if valores.ndim == 2 and valores.shape[1] == 1:
    
    valores = valores.flatten()

tamaño = len(valores) 


def add_impulse_noise(signal, noise_level=0.8, impulse_probability=0.05):
    
    noisy_signal = signal.copy()
    
    num_impulses = int(len(signal) * impulse_probability)
    
    impulse_indices = np.random.choice(len(signal), num_impulses, replace=False)
    
    impulses = np.random.normal(0, noise_level, num_impulses)
    
    noisy_signal[impulse_indices] += impulses
    
    return noisy_signal

noise_level = 0.8

impulse_probability = 0.05

noisy_signal = add_impulse_noise(valores, noise_level, impulse_probability)

signal_power = np.mean(valores ** 2)

noise_power = np.mean((noisy_signal - valores) ** 2)

SNR = 10 * np.log10(signal_power / noise_power)

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)

plt.plot(valores, label='Señal Original')

plt.title('Señal Original')

plt.xlabel('Muestras (t en s)')

plt.ylabel('Amplitud (mV)')

plt.legend()

plt.subplot(2, 1, 2)

plt.plot(noisy_signal, label='Señal con Ruido Impulsivo', color='r')

plt.title('Señal con Ruido Impulsivo')

plt.xlabel('Muestras (t en s)')

plt.ylabel('Amplitud (mV)')

plt.tight_layout()

plt.legend()

plt.show()

plt.figure(figsize=(12, 6))

plt.plot(valores, label='Señal Original', color='r')

plt.plot(noisy_signal, label='Señal Contaminada(Impulso)', alpha=0.7)

plt.title('Comparación de la Señal Original y la Señal Contaminada(Impulso)')

plt.xlabel('Muestras (t en s)')

plt.ylabel('Amplitud (mV)')

plt.legend()

plt.show()

print("el SNR obtenido por ruido impulso es:", SNR)

#ruido tipo artefacto 

np.random.seed(0) 

ruido = np.random.normal(0, 0.5, tamaño)  

señal_contaminada = valores + ruido

varianza_senal = np.var(valores)

varianza_ruido = np.var(ruido)

SnR = 10 * np.log10(varianza_senal / varianza_ruido)

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)

plt.plot(valores, label='Señal Original')

plt.title('Señal Original')

plt.xlabel('Muestras (t en s)')

plt.ylabel('Amplitud (mV)')

plt.legend()

plt.subplot(2, 1, 2)

plt.plot(señal_contaminada, label='Señal con Ruido tipo artefacto', color='r')

plt.title('Señal con Ruido Artefacto')

plt.xlabel('Muestras (t en s)')

plt.ylabel('Amplitud (mV)')

plt.tight_layout()

plt.legend()

plt.show()

plt.figure(figsize=(12, 6))

plt.plot(valores, label='Señal Original', color='r')

plt.plot(señal_contaminada, label='Señal Contaminada(Artefacto)', alpha=0.7)

plt.title('Comparación de la Señal Original y la Señal Contaminada(Artefacto)')

plt.xlabel('Muestras (t en s)')

plt.ylabel('Amplitud (mV)')

plt.legend()

plt.show()

print("el SNR obtenido por ruido artefacto es:", SnR)
import numpy as np 

import matplotlib.pyplot as plt

import scipy.fft as sft

import os

import librosa as lb

import random

import sounddevice as sd


def fourier_transform(x):
    N = len(x)
    X = np.zeros(N, dtype=np.complex128)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X

def getfft(x):
    xf = []
    for dt in x:
       df = sft.fft(dt)
       xf.append(df)
    return xf

def get_Mag(x):
    xMag = []
    for i in x:
        xMag.append(np.sqrt(np.real(i)**2 + np.imag(i))) 
    return xMag


def get_filepaths():
    list = []
    filePs = os.listdir('All_Audio_Files')
    for file in filePs:
        path = "All_Audio_Files/" + file
        list.append(path)

    return list     

def load_Audio_files(fileP):
    yts = []
    #srO = 0
    for file in fileP:
        y,_ = lb.load(file)
        yts.append(y)
    return yts


def plot_Signal(yt):
    plt.plot(np.arange(len(yt)),yt,color='k')
    plt.figure()
    plt.show()


paths = get_filepaths()

yts = load_Audio_files(paths)
print(yts)
random.shuffle(paths)
yts2 = load_Audio_files(paths[:10])

for i in yts2:
    i = np.array(i)
    sd.play(i,30000)
    sd.wait()


list_of_yfs = getfft(yts2)

maleC = 0
femaleC = 0

for yf in list_of_yfs:
    yfMag = get_Mag(abs(yf))
    print("The mean value is : ", np.mean(yfMag))
    if np.mean(yfMag[17000:22500]) > 7:
        femaleC += 1
    else:
        maleC += 1 

categories = ['Male', 'Female']
count = []
count.append(maleC)
count.append(femaleC)

# Plot
plt.bar(categories, count, color=['blue', 'pink'])
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Comparison of Male and Female Counts')
plt.figure()

lst = [1,2,3,4]
lstF = fourier_transform(lst)
plt.plot(np.arange(len(lstF)), lstF)
plt.figure()
lst = np.fft.fft(lst)
plt.plot(np.arange(len(lst)), lst)
plt.show()

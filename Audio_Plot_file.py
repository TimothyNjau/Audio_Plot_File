import wave #library for WAV 
import numpy as np #library for  Python numerical arrays. 
import  matplotlib.pyplot as plt # library to plot values from array



# PART ONE
wav = wave.open('beeSound.wav','r') 
#-----------------------------------------------------------
num_channels= wav.getnchannels()
print(num_channels)
#-----------------------------------------------------------
num_frames1=wav.getnframes()
print(num_frames1)
#-----------------------------------------------------------
raw = wav.readframes(-1)
raw = np.frombuffer(raw,"int16")

sampleRate = wav.getframerate()
print(sampleRate)
#-----------------------------------------------------------
sampleWidth = wav.getsampwidth()
print(sampleWidth)
#-----------------------------------------------------------
time = np.linspace(0,len(raw)/sampleRate,num=len(raw))

fig = plt.figure()
axis = fig.add_subplot(111)
fig.suptitle('Waveform of WAV file')
axis.plot(time,raw,color='red',linewidth=0.2)
plt.ylabel ('Amplitude')
plt.show()


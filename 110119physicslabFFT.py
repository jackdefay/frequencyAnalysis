import matplotlib.pyplot as plt
import numpy as np
import scipy
import projectlabMax as max

from scipy.fftpack import fft
from scipy.io import wavfile # get the api
fs, data = wavfile.read('384 - 1.wav') # load the data

a = data.T[0] # this is a two channel soundtrack, I get the first track
b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)

# print(fs//10) #fs is the sample rate in Hz, samples per second. So if we want a .05 second slice then we want fs/20 data points

#iterate through slices and perform fft's. add to a list
i=1
sliceList = []
while(i<len(b)//(fs/10)):
    slice = fft(b[(i-1)*(fs//10):(i)*(fs//10)])
    sliceList.append(abs(slice[:round(len(slice)/2)]))
    i+=1

#set up the xscaler from index number to frequency
k = scipy.arange(len(slice)/2)
T = len(slice)/(2*fs)  # where fs is the sampling frequency
frqLabel = k/T
listFrqLabel = np.ndarray.tolist(frqLabel)

#create a 2d list of the xscaler so it matches the dimensions of the fft list
#apply Max's program to find the peaks of each fft, compile to a separate list
twoDimListFrqLabel = []
peaks = []
for i in range(len(sliceList)):
    twoDimListFrqLabel.append(listFrqLabel)


fig, ax = plt.subplots()
for i in range(len(twoDimListFrqLabel)//4, 3*len(twoDimListFrqLabel)//4):
    ax.plot(twoDimListFrqLabel[i], sliceList[i])
plt.xlabel("Hz", fontsize=15)
plt.xlim((1, 10000))
# plt.xscale('log')
plt.title("384 Hz, first take")
plt.show()




# ax.plot(twoDimListFrqLabel[20], sliceList[20])




# print(type(sliceList[10]))
# dict = max.datapls(sliceList[20], twoDimListFrqLabel[20], 10, 10000)
# print(dict)
# print(peaks)




# c = fft(b) # calculate fourier transform (complex numbers list)

# plt.plot(c)
# plt.show()

# d = round(len(c)/2)  # you only need half of the fft list (real signal symmetry)
# c = c[:(d-1)]
# plt.plot(abs(c),'r')
# k = arange(len(data))
# T = len(data)/fs  # where fs is the sampling frequency
# frqLabel = k/T
# plt.show()

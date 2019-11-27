import matplotlib.pyplot as plt
import numpy as np
import scipy
import projectlabMax as max
import reoderPeakDictionary as reorder

from scipy.fftpack import fft
from scipy.io import wavfile # get the api

def f(filename):
    fs, data = wavfile.read('110119audioFilesWAV/'+filename) # load the data

    a = data.T[0] # this is a two channel soundtrack, I get the first track
    b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)

    # print(fs//10) #fs is the sample rate in Hz, samples per second. So if we want a .05 second slice then we want fs/20 data points

    #iterate through slices and perform fft's. add to a list
    i=1
    sliceList = []
    while(i<len(b)//(fs/20)):
        slice = fft(b[(i-1)*(fs//20):(i)*(fs//20)])
        sliceList.append(abs(slice[:round(len(slice)/2)]))
        i+=1

    #set up the xscaler from index number to frequency
    k = scipy.arange(len(slice))
    T = len(slice)/(fs)  # where fs is the sampling frequency
    frqLabel = k/T
    listFrqLabel = np.ndarray.tolist(frqLabel)

    #create a 2d list of the xscaler so it matches the dimensions of the fft list
    #apply Max's program to find the peaks of each fft, compile to a separate list
    twoDimListFrqLabel = []
    peaks = []
    for i in range(len(sliceList)):
        twoDimListFrqLabel.append(listFrqLabel)
        peak = max.datapls(sliceList[i], listFrqLabel, 10, 10000)
        peaks.append(peak)
        # print(peak)

    graphPeaks, peakFrqList = reorder.reorder(peaks[10:])

    fig, ax = plt.subplots()
    for i in range(len(graphPeaks)):
        ax.plot(graphPeaks[i])
    plt.xlabel("Hz", fontsize=15)
    # plt.xlim((1, 10000))
    # plt.xscale('log')
    plt.title("384 Hz, first take")
    plt.legend(peakFrqList)
    # plt.show()

    plt.savefig('graphs/'+filename+'.png',bbox_inches='tight')

    plt.close()

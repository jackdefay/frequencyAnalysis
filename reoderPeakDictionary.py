import numpy
import heapq
def reorder(peaks):
    """reorders the peaks to be in a more graphable format

    returns: a nested list of peaks, a list of the frequencies that correspond to those peaks

    parameter: peaks
    precondition: peaks is a list of dictionaries of the form {frequency, amplitude}
    """

    #convert from the list of dictionaries provided to a list of peak objects
    peakList = []
    knownValues = []
    for i in peaks:
        for x in i.keys():
            if not x in knownValues:
                p = Peak(x, i.get(x))
                peakList.append(p)
                knownValues.append(x)
            else:
                peakList[knownValues.index(x)].add(i.get(x))

    #sort the list greatest to least in terms of the length of each peak's sublist
    peakList.sort(key = lambda p: p.getLenth(), reverse=True)

    #then convert that into 2 lists: one a 2d of the values and the other the corresponding list of frequencies in order
    graphPeaks = []
    graphValues = []
    for j in range(0,min(5, len(peakList))):
        graphPeaks.append(peakList[j].getAmp())
        graphValues.append(peakList[j].getFrq())

    return graphPeaks, graphValues


class Peak:
    """object to store peak information"""
    def __init__(self, frequency, firstAmplitude):
        self.frequency = frequency
        self.amplitudes = []
        self.add(firstAmplitude)

    def __lt__(self, other):
        return self.getLenth() - other.getLenth()

    def __eq__(self, other):
        return self.frequency.equals(other.frequency) and self.amplitudes.equals(other.amplitudes)

    def __repr__(self):
        return str(self.frequency) + ', ' + str(len(self.amplitudes))

    def __str__(self):
        return str(self.frequency) + ', ' + str(len(self.amplitudes))

    def getLenth(self):
        return len(self.amplitudes)

    def add(self, amp):
        self.amplitudes.append(amp)

    def getAmp(self):
        return self.amplitudes

    def getFrq(self):
        return self.frequency

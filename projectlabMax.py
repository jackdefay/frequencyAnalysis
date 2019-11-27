import numpy
def datapls(b, xrange, fmin,fmax):
    """Makes a spectrum data text file into a dictionary of Hz:dB

    When using the export data button on audacity, it returns a text file with
    a bunch of data in a sorted list. This program converts that file into a
    dictionary, which can then be otherwise manipulated in python. Make sure to
    delete the part at the top of the text file which says 'Frequency (Hz)' and
    'Level (dB)', as this program is only designed to work with numbers. The
    values for fmin and fmax are the range of values that you want your dictionary
    to include the values between.

    As a tip, changing the size in audacity in the spectrum analyzer
    can also change the amount of data that audacity outputs. By default it is
    512, but changing it to higher values causes it to output data more
    frequently. Keep in mind, however, that changing it to be too high might
    break the program.

    Also when I tested this program some of our data files just did not work
    well with it, so it is worth manually comparing just to make sure your data
    generally matches what the program outputs.

    Paramter x: The name of the file to analyze
    Precondition: x is a string

    Paramter fmin: The minimum frequency of the values
    Precondition: fmin is a number

    Parameter fmax: the maximum frequency of the values
    Precondition: fmax is a number
    """
    #next three lines convert the data to an ordered list
    g={}
    # b=numpy.loadtxt(x)
    c=numpy.ndarray.tolist(b)
    #converts the list to a dictionary with form frequency:decibels
    for i in range(10,len(c)-10):
        #Sets the data to be within the range of fmin and fmax
        if i>fmin and i<fmax:
            #picks out the data points which are greater than the 3 points to
            #the left and right of them
            if (c[i]>c[i+1] and c[i]>c[i+2] and c[i]>c[i-1] and c[i]>c[i-2] and c[i]>c[i-3] and c[i]>c[i+3]):
                if(c[i]>c[i+10]+10 and c[i]>c[i-10]+10):
                    g.update({xrange[i]:c[i]})
    return g

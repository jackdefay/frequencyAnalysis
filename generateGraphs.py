import glob
import graphPeaks

files = glob.glob('110119audioFilesWAV'+'./*.wav')

for ele in files:
    name = ele.split('\\', 2)[1]
    print(name)
    graphPeaks.f(name)
quit()

# graphPeaks.f('384 - 1.wav')
# quit()

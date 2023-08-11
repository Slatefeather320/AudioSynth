#THIS IS LITRARLY JUST audlib2.py BUT RENAMED TO PUT ON GITHUB

import math, numpy
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

class audio:
    def __init__(self, lenght, bitrate=44100):
        self.lenght = lenght
        self.bitrate = bitrate
        self.waveform = []
    
    def makeTone(self, frequency, amplitude=1):
        self.waveform = []
        for i in range(0,self.bitrate*self.lenght):
            ni = i/self.bitrate #normalized i
            si = ni*math.pi*2 #scaled i
            self.waveform.append(amplitude*math.sin(si*(frequency)))
    
    def addTone(self, frequency, amplitude=1, start=0, end=1):
        start = start*len(self.waveform)
        end = end*len(self.waveform)
        for i in range(int(start),int(end)):
            ni = i/self.bitrate #normalized i
            si = ni*math.pi*2 #scaled i
            self.waveform[i]=((amplitude*math.sin(si*(frequency)))+self.waveform[i])
    
    def appendTone(self, frequency, amplitude=1, lenght=1):
        for i in range(0,self.bitrate*lenght):
            ni = i/self.bitrate #normalized i
            si = ni*math.pi*2 #scaled i
            self.waveform.append(amplitude*math.sin(si*(frequency)))
            self.lenght += lenght
    

    def showForm(self):
        x = range(0,len(self.waveform))
        y = self.waveform
        plt.plot(x, y)
        plt.show()

    def export(self, name = "Audio",maxAmp=32767): #if you kept adding tones on top of eachother, if they constructivly interfared, there might be places where the amplitude exceded the maxium playible. For those cases this second parameter exists, for most cases you don't need to enter any value for it. If you think your audio is clipping at the loudest parts, double this value.
        d = []
        for i in self.waveform:
            d.append(int(i*maxAmp/2000)) #i dont know why but the number 2000 works  
        data = numpy.array(d, dtype=numpy.uint8)
        write(name+".wav",self.bitrate,data)

            



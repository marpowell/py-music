import pyaudio
import math
from multiprocessing.dummy import Pool as ThreadPool 
#Todo: make one period of data for sinewave. repeat ad nauseum


class music: 
    
    def __init__(self,
                 rate=44100,
                 channels=2,
                 width=2,
                 freq=440):
        self.rate = rate #SAMPLES PER SECOND
        self.channels = channels #2 = STEREO
        self.width = width #SAMPLE WIDTH IN BYTES (16 Bit 44100 = CD Quality)
        self.frequency = freq #A4 = 440Hz
        self.coefficient = 2 * math.pi * self.frequency / self.rate
        self.amplitude = .75 * math.pow(2,2*self.width-1) / 2 -1
        self.wave = self._generateWave()
        self._pa = pyaudio.PyAudio()
        self._audiostream = self._pa.open(format = self._pa.get_format_from_width(width), 
                         channels = channels,
                         rate = rate,
                         output = True,)
                         
        
    def sine(self, x):
        x = round(self.amplitude * math.sin(x * self.coefficient))
        if x < 0:
            x = int((math.pow(2,2*self.width)-1)) & x
        
        temp = 0
        
        for i in range(self.width): #render in little endian representation
            temp = (temp << 8) | x & 255
            x = x >> 8
         
        x = temp 
          
        x = ("{0:0"+str(2*self.width)+"X}").format(x) #format to pad out zeroes
        
        return x + x
      
    def _generateWave(self):
        
        wave = list(range(self.rate))
        pool = ThreadPool(8)
        return str(pool.map(self.sine, wave))
        
    
         
        
    def setFrequency(self, freq):
        self.frequency = freq
        self.coefficient = 2 * math.pi * self.frequency / self.rate
        self.amplitude = math.pow(2,2*self.width-1) / 2 -1
        self.wave = self._generateWave()
        
    def playTone(self, note, seconds):
        if (seconds < 0):
            raise ValueError('Seconds cannot be a negative number!') 
                

        for i in range(math.floor(seconds)):
            self._audiostream.write(self.wave) #1 length of wave = 1 second (len(wave) = width*channels*rate)
        
        
        if (seconds - math.floor(seconds) != 0): 
            index = int(round(2*self.width*self.channels*self.rate*(seconds-math.floor(seconds)))) #remainder of frames
            wave = self.wave[0:index]
            #tack on the remainder in case that seconds is not whole          
            self._audiostream.write(wave)
        
        
    
    def terminate(self):
        self._audiostream.stop_stream()
        self._audiostream.close()
        self._pa.terminate()
        
        
        
        
        
m = music()

m.playTone(1, .25)
m.setFrequency(523.25)
m.playTone(1, .25)
m.setFrequency(659.25)
m.playTone(1, .25)
m.setFrequency(789.99)
m.playTone(1, .25)
m.setFrequency(987.77)
m.playTone(1, .25)
m.setFrequency(1318.51)
m.playTone(1, .25)
m.setFrequency(1046.50)
m.playTone(1, .75)

m.terminate()
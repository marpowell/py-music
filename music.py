#!/usr/bin/env python
import pyaudio
import math
from multiprocessing.dummy import Pool as ThreadPool 


class music: 
    notes = {'C':0,'C#':1,'Db':1,'D':2,'D#':3,'Eb':3,
             'E':4,'F':5,'F#':6,'Gb':6,'G':7,'G#':8,
             'Ab':8,'A':9,'A#':10,'Bb':10,'B':11}
    A4 = 12* 4 + 9 #A4 = 440 Hz

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
        self.amplitude = .8 * math.pow(2,2*self.width-1) / 2 -1
        self.wave = self._generateWave()
        self._pa = pyaudio.PyAudio()
        self._audiostream = self._pa.open(format = self._pa.get_format_from_width(width), 
                         channels = channels,
                         rate = rate,
                         output = True,)
                         
        
    def sine(self, x):
        x = round(self.amplitude * math.sin(x * self.coefficient))
        if x < 0:
            x = int((math.pow(2,2*self.width)-1)) & x #two's compliment
        
        temp = 0
        
        for i in range(self.width): #render in little endian representation
            temp = (temp << 8) | x & 255
            x = x >> 8
         
        x = temp 
          
        x = ("{0:0"+str(2*self.width)+"X}").format(x) #format to pad out zeroes
        
        return x + x
      
    def _generateWave(self):
        samples = int(round(self.rate/self.frequency))
        wave = list(range(samples))
        pool = ThreadPool(4)
        return str(pool.map(self.sine, wave))
        
    
         
        
    def setFrequency(self, freq):
        self.frequency = freq
        self.coefficient = 2 * math.pi * self.frequency / self.rate
        self.amplitude = math.pow(2,2*self.width-1) / 2 -1
        self.wave = self._generateWave()
        
    def playTone(self, note, seconds):
        if (seconds < 0):
            raise ValueError('Seconds cannot be a negative number!') 
        
        self.setFrequency(music._freqFromNote(note[:-1],int(note[-1:])))        

        for i in range(round(self.frequency * seconds)):
            self._audiostream.write(self.wave) #1 length of wave = 1 second (len(wave) = width*channels*rate)
        
        
        
        
    def _freqFromNote(letter, octave):
        difference = (12 * octave + music.notes[letter]) - music.A4
        return 440 * math.pow(2, difference / 12)
        
    def terminate(self):
        self._audiostream.stop_stream()
        self._audiostream.close()
        self._pa.terminate()
        
        
        
        
        
m = music()
'''
m.playTone("A4", .3)
m.playTone("C5", .1)
m.playTone("E5", .1)
m.playTone("G5", .1)
m.playTone("B5", .1)
m.playTone("D6", .1)
m.playTone("A6", .1)
m.playTone("G6", .1)
m.playTone("C6", .75)'''

m.terminate()
import pyaudio
import math
import time
import wave
#TO DO: fix negatives


p = pyaudio.PyAudio()

RATE = 44100 #SAMPLES PER SECOND
CHANNELS = 2
WIDTH = 2 #SAMPLE WIDTH IN BYTES (16 Bit 44100 = CD Quality)
frequency = 523.25 #A4 = 440Hz
majorscale = [523.25, 587.23, 659.25, 698.46, 783.99, 880.00, 987.77, 1046.50]
position = 0
wf = 0
n = 0


def initializeWave():
    global wf
    global n
    wf = wave.open('h.wav', 'rb')
    #wf.setnchannels(2)
    #wf.setsampwidth(2)
    #wf.setframerate(44100)
    #wf.setnframes(1048576)
    n = 1

initializeWave()

def write(sample):
    global n
    if (n < 1048576):
        wf.writeframes(bytes.fromhex(sample))
        n += 1
    if (n < 1048576):
        wf.writeframes(bytes.fromhex(sample))
        n += 1

def littleEndian(twobytes): #returns little endian representation of a 16 bit number
    if (twobytes < 0):
        twobytes = twobytes & int((math.pow(2,WIDTH*8)-1))

    return ((twobytes & 255) << 8) | (twobytes >> 8)
    
    
    
    
def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    return (data, pyaudio.paContinue)
    
    '''global position
    out_data = ''
    coefficient = 2 * math.pi * frequency / RATE
    amplitude = math.pow(2,WIDTH*8-1) -1 #maximum bitwidth / 2 [ should be / 2]
    global n
    for x in range(position, position + frame_count):
        sample = littleEndian(round(amplitude * math.sin(x * coefficient)))
        #should remove vertical shift eventually, but fix negatives first
 
        sample = '{0:04X}'.format(sample)   #hex function returns '0xAA' string rep of float number
        
        #write(sample)
        
        out_data +=  sample + sample #left and right channels
        #if (out_data == 0):
        #    out_data = (sample << 16) | sample
        #else:
        #    out_data = (((out_data << 16) | sample) << 16) | sample #left and right channels

        
    
    position += frame_count
    return (out_data, pyaudio.paContinue)'''
    
audiostream = p.open(format = p.get_format_from_width(WIDTH), 
                     channels = CHANNELS,
                     rate = RATE,
                     output = True,
                     stream_callback = callback);


audiostream.start_stream()

#for i in range(0,8):
#    if audiostream.is_active():
#        frequency = majorscale[i]
#        time.sleep(1)
while audiostream.is_active():
    time.sleep(0.1)

audiostream.stop_stream()
audiostream.close()
wf.close()
#print(bytes.fromhex(callback(0,100,0,0)[0]))
#print(p.get_format_from_width(WIDTH))
p.terminate()
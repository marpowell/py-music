import tkinter as tk
import winsound
import math
import random

letterModulus = {'C':0,'CX':1,'Db':1,'D':2,'DX':3,'Eb':3,'E':4,'F':5,'FX':6,'Gb':6,'G':7,'GX':8,'Ab':8,'A':9,'AX':10,'Bb':10,'B':11}
A4 = 12* 4 + 9 #A4 = 440 Hz
    
class EarTraining(tk.Frame):
    scorenum = 0
    total = 0
    state = 0
    def __init__(self, master=None):
        #master.minsize(width = 600, height=600)
        #master.maxsize(width = 600, height=600)
        master.resizable(0,0)
        master.wm_title("Ear Training")
        tk.Frame.__init__(self, master)
        score = tk.Label(self, text = "Score: 0").grid(row=0, column = 5)
        tk.Label(self, text="Select the interval you hear",height = 3).grid(row = 0, column = 0,columnspan=5)
        tk.Label(self, text="Major:").grid(row = 1, column = 0,padx=30,pady=5)
        tk.Label(self, text="Minor:").grid(row = 2, column = 0,pady=5)
        tk.Button(self, text = "M2",width=3).grid(row = 1, column = 1,padx=30)        
        tk.Button(self, text = "M2",width=3).grid(row = 1, column = 2,padx=30)        
        tk.Button(self, text = "M2",width=3).grid(row = 1, column = 3,padx=30)        
        tk.Button(self, text = "M2",width=3).grid(row = 1, column = 4,padx=30)        
        tk.Button(self, text = "m2",width=3).grid(row = 2, column = 1)        
        tk.Button(self, text = "m2",width=3).grid(row = 2, column = 2)        
        tk.Button(self, text = "m2",width=3).grid(row = 2, column = 3)        
        tk.Button(self, text = "m2",width=3).grid(row = 2, column = 4)        
        tk.Button(self, text = "P4",width=3).grid(row = 3, column = 1)        
        tk.Button(self, text = "tritone",width=6).grid(row = 3, column = 2,columnspan=2)
        tk.Button(self, text = "P5",width=3).grid(row = 3, column = 4)        
        tk.Button(self, text = "P8 (octave)").grid(row = 3, column = 5,padx=30)        
        tk.Button(self, text = "unison").grid(row = 3, column = 0,pady=5)        
        
        playbtn= tk.Button(self, text = "Play!", height = 2, width = 60, command = self.playTone())
        playbtn.grid(row  = 4, column = 0, columnspan = 6)
        
        self.grid()

    
    def playTone(self):
        if (self.state == 1):
            return
        self.state = 1
        randint = random.randint(1,12)
        
    def getFreq(mod, mult):
        difference = A4 - (12 * mult + letterModulus[mod])
        return math.pow(math.pow(2,.125), difference) + 440
        
root = tk.Tk()
app = EarTraining(master = root)
app.mainloop()
winsound.Beep(220, 1000)
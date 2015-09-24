#!/usr/bin/env python
import tkinter as tk
import random
import music

    
class EarTraining(tk.Frame):
    scorenum = 0
    total = 0
    state = 0
    interval = 0
    root = 0
    changebtns = []
    m = music.music()
    def __init__(self, master=None):
        #master.minsize(width = 600, height=600)
        #master.maxsize(width = 600, height=600)
        master.resizable(0,0)
        master.wm_title("Ear Training")
        tk.Frame.__init__(self, master)
        self.score = tk.Label(self, text = "Score: 0")
        self.score.grid(row=0, column = 5)
        
        self.select = tk.Label(self, text="Select the interval you hear",height = 3)
        self.select.grid(row = 0, column = 0,columnspan=5)
        
        tk.Label(self, text="Major:").grid(row = 1, column = 0,padx=30,pady=5)
        tk.Label(self, text="Minor:").grid(row = 2, column = 0,pady=5)
        
        self.maj2 = tk.Button(self, text = "M2",width=3, command = lambda : self.checkAnswer(2))
        self.maj3 = tk.Button(self, text = "M3",width=3, command = lambda : self.checkAnswer(4))
        self.maj6 = tk.Button(self, text = "M6",width=3, command = lambda : self.checkAnswer(9))
        self.maj7 = tk.Button(self, text = "M7",width=3, command = lambda : self.checkAnswer(11))
        self.min2 = tk.Button(self, text = "m2",width=3, command = lambda : self.checkAnswer(1))
        self.min3 = tk.Button(self, text = "m3",width=3, command = lambda : self.checkAnswer(3))
        self.min6 = tk.Button(self, text = "m6",width=3, command = lambda : self.checkAnswer(8))
        self.min7 = tk.Button(self, text = "m7",width=3, command = lambda : self.checkAnswer(10))
        self.p4 = tk.Button(self, text = "P4",width=3, command = lambda : self.checkAnswer(5))
        self.tri = tk.Button(self, text = "tritone",width=6, command = lambda : self.checkAnswer(6))
        self.p5 = tk.Button(self, text = "P5",width=3, command = lambda : self.checkAnswer(7))
        self.p8 = tk.Button(self, text = "P8 (octave)",width=10, command = lambda : self.checkAnswer(12))
        self.uni = tk.Button(self, text = "unison", command = lambda : self.checkAnswer(0))
                
        
        self.maj2.grid(row = 1, column = 1,padx=30)  
        self.maj3.grid(row = 1, column = 2,padx=30)
        self.maj6.grid(row = 1, column = 3,padx=30) 
        self.maj7.grid(row = 1, column = 4,padx=30) 
        self.min2.grid(row = 2, column = 1)  
        self.min3.grid(row = 2, column = 2)
        self.min6.grid(row = 2, column = 3)
        self.min7.grid(row = 2, column = 4) 
        self.p4.grid(row = 3, column = 1)    
        self.tri.grid(row = 3, column = 2,columnspan=2)
        self.p5.grid(row = 3, column = 4)
        self.p8.grid(row = 3, column = 5,padx=30)  
        self.uni.grid(row = 3, column = 0,pady=5)
        
        self.playbtn= tk.Button(self, text = "Play!", height = 2, width = 60, command = self.playTone)
        self.playbtn.grid(row  = 4, column = 0, columnspan = 5)
        tk.Button(self, text = "Quit", height = 1, width = 10, command = self.terminate).grid(row=4,column=5)
        
        self.grid()

    def playTone(self):
        number_to_note = {0:"C",1:"C#",2:"D",3:"D#",4:"E",5:"F",6:"F#",7:"G",8:"G#",9:"A",10:"A#",11:"B"}
        
        if self.state == 1:
            # _thread.start_new_thread(self._playnotes, (number_to_note[self.root[0]]+str(self.root[1]),
            #                                number_to_note[(self.root[0]+self.interval) % 12]+str(self.root[1])))
            #self._playnotes(number_to_note[self.root[0]]+str(self.root[1]),
            #                 number_to_note[(self.root[0]+self.interval) % 12]+str(self.root[1]+self.upoctave))
            return
            
        self.state = 1
        
        if self.changebtns != None:
            for btn in self.changebtns:
                btn.config(bg=self.playbtn.cget("bg"))
        
        self.changebtns = []
                
        root = [random.randint(0,11), random.randint(4,6)]
        interval = random.randint(0,12) 
        
        self.upoctave = False 
        if interval + root[0] > 11:
            self.upoctave = True

        self.interval = interval
        self.root = root
        
        #self.select.config(text= number_to_note[root[0]]+str(root[1]) +" "+ number_to_note[(root[0]+interval) % 12]+str(root[1]+self.upoctave)+
        #                    " " + str(root) + " " + str(interval) )
                        
        #_thread.start_new_thread(self._playnotes, (number_to_note[root[0]]+str(root[1]),
        #                                           number_to_note[(root[0]+interval) % 12]+str(root[1])))
        self._playnotes(number_to_note[root[0]]+str(root[1]),
                        number_to_note[(root[0]+interval) % 12]+str(root[1]+self.upoctave))
                        
    def _playnotes(self, note1,note2):
        self.m.playTone(note1,.5)
        self.m.playTone(note2,.5)
        
    def checkAnswer(self, answer):
        if (self.state == 0):
            return
        self.state = 0
        interval_to_button = {0:self.uni, 1:self.min2, 2:self.maj2,
                              3:self.min3, 4:self.maj3, 5:self.p4,
                              6:self.tri, 7:self.p5, 8:self.min6,
                              9:self.maj6, 10:self.min7, 11:self.maj7,
                              12:self.p8}
        
        interval_to_button[answer].config(bg = "red")
        interval_to_button[self.interval].config(bg="green")
        self.changebtns = [interval_to_button[answer],interval_to_button[self.interval]]        
        
        if answer == self.interval:
            self.scorenum +=1
            self.total+=1
            
            self.score.config(text = "Correct! "+str(self.scorenum)+"/"+str(self.total),fg="green")
        else:
            self.total+=1
            self.score.config(text = "Incorrect. "+str(self.scorenum)+"/"+str(self.total),fg="red")
            
    def terminate(self):
        
        self.m.terminate()
        self.quit()
        
    
        
root = tk.Tk()
app = EarTraining(master = root)
app.mainloop()
#winsound.Beep(220, 1000)
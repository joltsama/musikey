#!/usr/bin/env python3
import tkinter as tk
import random, simpleaudio as sa

root=tk.Tk()
root.title("Client")
root.geometry(('400x275'))

class musikey(tk.Tk):

    seq=[]
    cor=[]
    usr=[]
    waves={}
    record=False

    def __init__(self):
        self.cor=['D','F','G']

        self.status=tk.Label(root, text='Locked')
        # self.unlock=tk.Label(root, text='Unlocked')
        self.display=tk.Label(root, text='Please play the melody')
    
        self.button_c=tk.Button(root, text="1", command=lambda: self.Play(0))
        self.button_d=tk.Button(root, text="2", command=lambda: self.Play(1))
        self.button_e=tk.Button(root, text="3", command=lambda: self.Play(2))
        self.button_f=tk.Button(root, text="4", command=lambda: self.Play(3))
        self.button_g=tk.Button(root, text="5", command=lambda: self.Play(4))
        self.button_a=tk.Button(root, text="6", command=lambda: self.Play(5))
        self.button_b=tk.Button(root, text="7", command=lambda: self.Play(6))

        self.start=tk.Button(root, text="Recording", command=self.Record)
        self.verify=tk.Button(root, text="Verify", command=self.Verify)
        self.exit=tk.Button(root, text='Exit', command=self.Exit)
        self.placewidgets()

        self.waves={'C':sa.WaveObject.from_wave_file('./wav/c1.wav'),
        'D':sa.WaveObject.from_wave_file('./wav/d1.wav'),
        'E':sa.WaveObject.from_wave_file('./wav/e1.wav'),
        'F':sa.WaveObject.from_wave_file('./wav/f1.wav'),
        'G':sa.WaveObject.from_wave_file('./wav/g1.wav'),
        'A':sa.WaveObject.from_wave_file('./wav/a1.wav'),
        'B':sa.WaveObject.from_wave_file('./wav/b1.wav'),}
        self.Random()
        self.PlaySounds()

        #self.Connect()
        
    def placewidgets(self):
        self.status.pack()
        self.display.pack()
        self.button_c.pack()
        self.button_d.pack()
        self.button_e.pack()
        self.button_f.pack()
        self.button_g.pack()
        self.button_a.pack()
        self.button_b.pack()
        self.verify.pack()
        self.start.pack()
        self.exit.pack()

    def Record(self):
        self.usr=[]
        if self.record==True:
            self.record=False
            self.start.config(text="Stopped")
        else:
            self.record=True
            self.start.config(text="Recording")

    def PlaySounds(self):

        for i in range(len(self.seq)):
            
            play_obj = self.waves[self.seq[i]].play()
            play_obj.wait_done()


    def Random(self):
        self.seq=['C','D','E','F','G','A','B']
        random.shuffle(self.seq)
        print(self.seq)

    def Play(self, k):

        po=self.waves[self.seq[k]].play()
        po.wait_done()

        if self.record==True:
            self.usr.append(self.seq[k])
            print(self.usr)
        #playing according to key strokes

    def Verify(self):
        if len(self.usr)==len(self.cor):
            for i in range(len(self.usr)):
                if self.usr[i]==self.cor[i]:
                    print(self.usr)
                    self.status.config(text="Unlocked")

        self.usr=[]
        #check if the combination is correct
    
    def Change(self):
        pass
        #to change password

    def Exit(self):
        root.quit()

        
C=musikey()
root.mainloop()
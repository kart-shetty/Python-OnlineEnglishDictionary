from tkinter import *
from tkinter import ttk
import time

class ContinousProgressBar:
    def progressBar(self, frame1):
        self.master = frame1
        global progressbar
        progressbar = ttk.Progressbar(self.master, orient=VERTICAL, length=150, mode='indeterminate',
                                      maximum=10.0,
                                      value=0)
        progressbar.pack(side=RIGHT, ipadx=1, ipady=30)
        while 1:
            progressbar.step(0.25)
            self.master.update()
            time.sleep(0.1)

    def forgetProgressBar(self):
        progressbar.forget()
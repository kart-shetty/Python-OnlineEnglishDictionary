from tkinter import *
from tkinter import ttk
class NewFrame2:

    def stage2(self ,root):

        self.root = root
        self.frame2 = ttk.LabelFrame(self.root, height=250, width=500, text='RESULT FIELD')
        self.frame2.config(relief=RIDGE )
        self.frame2.pack(side=LEFT)
        self.root.update()


    def close_button(self, frame2, button):
        button.configure(command=frame2.forget())


    def outputField(self, resultVal):
        global b
        self.textarea = Text(self.frame2)
        self.scroll = ttk.Scrollbar(self.textarea)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.place(x=10, y=0 , width=480, height=220)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.textarea.insert(END, resultVal)
        a = NewFrame2()
        self.button = ttk.Button(self.frame2, text='CLOSE', command= lambda: a.close_button(self.frame2, self.button))
        self.button.place(x=420, y=0, width=50, height=22)
        b = a

    def closeButton(self):
        b.close_button()
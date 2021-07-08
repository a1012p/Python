from gui.converters import Converters
from tkinter import *

class App:
    def __init__(self,master):
        self.conv = Converters("C","F",1.8,32)

        frame = Frame(root)
        frame.pack()

        Label(frame,text="deg C").grid(row=0,column=0)
        self.c = DoubleVar() #실수형 변수
        Entry(frame,textvariable=self.c).grid(row=0,column=1)

        Label(frame,text="deg F").grid(row=1,column=0)
        self.f = DoubleVar() #실수형 변수
        Label(frame,textvariable=self.f).grid(row=1,column=1)

        Button(frame,text = "변환" , command=self.convert).grid(row=2,columnspan=2)

    def convert(self):
        f =self.conv.convert(self.c.get())
        self.f.set("%.2f" % f)

root = Tk()
root.title("온도 변환기")

app= App(root)

root.mainloop()
#컨트롤 도구 - 레이블,버튼,목록 박스
from tkinter import *

class App:
    def __init__(self,master):
        self.root = master
        frame = Frame(master)
        frame.pack()

        Label(frame,text="제목",padx=10,pady=10).grid(row=0,column=0)
        Entry(frame,width=20).grid(row = 0,column=1)
        Button(frame,text="확인").grid(row=0,column=2)
        check_var = StringVar() #문자형의 변수 사용
        check = Checkbutton(frame,text="체크",variable=check_var,
                    onvalue='Y',offvalue='N')
        check.grid(row=1,column=0)
        listbox = Listbox(frame,height=3,selectmode=SINGLE)
        for i in ['red','green','blue','yellow']:
            listbox.insert(1,i)
        listbox.grid(row=2,column=1)
        radio_frame = Frame(frame)
        radio_select = StringVar()
        b1 = Radiobutton(radio_frame,text='left',variable= radio_select,value='P')
        b1.pack(side=LEFT)
        b2 = Radiobutton(radio_frame,text='right',variable= radio_select,value='L')
        b2.pack(side=LEFT)
        radio_frame.grid(row=1,column=2)

root = Tk()
root.title("컨트롤 도구 UI")
app = App(root)

root.mainloop()
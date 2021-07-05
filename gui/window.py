# 윈도우 만들기

from tkinter import *

root = Tk()
root.title("window")
root.geometry("400x100+600+300") #너비x높이 + x좌표 + y좌표


frame = Frame(root)   #root 위에 위치하는 프레임 객체
frame.pack()            #pack메소드 레이아웃을 담당

#문자열 출력 - Label class

Label(frame,text="Hello Python").grid(row=0,column=0)
Button(frame,text="버튼").grid(row=1,column=0)

root.mainloop()
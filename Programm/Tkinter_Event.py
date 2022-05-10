# 定义事件函数
from tkinter import *

def handleMotion(event):
    lb1['text'] = '你移动了光标的所在位置'
    lb2['text'] = '目前光标位置：x ='+ str(event.x)+';y='+str(event.y)
    print('光标当前位置',event.x,event.y)

# 创建主窗口
win = Tk()
win.config(bg='#87CEEB')
win.title("C语言中文网")
win.geometry('450x350+300+200')
#win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# 创建一个窗体容器frame
frame = Frame (win, relief=RAISED, borderwidth=2, width=300,height=200)
frame.bind('<Motion>',handleMotion)
lb1 = Label(frame,text='没有任何事件触发', bg='yellow', )
# 使用place进行位置布局，下一节会介绍
lb1.place (x=20,y=20)
lb2 = Label(frame,text='')
lb2.place (x=16,y=60)
frame.pack(side=TOP)
# 显示窗口
win.mainloop()
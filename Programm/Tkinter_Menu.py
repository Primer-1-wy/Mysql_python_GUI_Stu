from tkinter import *
win=Tk()
win.config(bg='#87CEEB')
win.title("C语言中文网")
win.geometry('450x350+300+200')
#win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
#创建一个菜单按钮
menubtn=Menubutton(win, text='点击进行操作', relief='sunk')
# 设置位置（布局）
menubtn.grid(padx=195, pady=105)
#添加菜单,使用 tearoff 参数不显示分割线
filemenu=Menu(menubtn,tearoff = False)
filemenu.add_command(label='新建')
filemenu.add_command(label='删除')
filemenu.add_command(label='复制')
filemenu.add_command(label='保存')
# 显示菜单，将菜单命令绑定在菜单按钮对象上
menubtn.config(menu=filemenu)
win.mainloop()
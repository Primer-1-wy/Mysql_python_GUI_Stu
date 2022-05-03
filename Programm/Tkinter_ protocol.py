import tkinter as tk
from tkinter import Tk
# 导入 对话框控件
from tkinter import messagebox

# 创建主窗口
root = Tk()
# 定义回调函数，当用户点击窗口x退出时，执行用户自定义的函数
def QueryWindow():
    # 显示一个警告信息，点击确后，销毁窗口
    if messagebox.showwarning("警告","出现了一个错误"):
        # 这里必须使用 destory()关闭窗口
        root.destroy()
def callback():
    print("执行回调函数","C语言中文网欢迎您")

def Window_inMid():
    width = 300
    height = 300
    # 窗口居中，获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    return size_geo
# 使用协议机制与窗口交互，并回调用户自定义的函数
root.title("test")
#上述代码表示，设置主窗口的宽度为 450，高度为 400
#同时窗口距离左边屏幕的距离为 300（以像素为单位），距离屏幕顶部的距离为 200，这里我们将带“+”的参数值称为“位置参数”
root.geometry('450x400+300+200')
#当设置了一个超过屏幕的负参数值时，主窗口会被移动至“屏幕之外”，此时就看不到主窗口了，这也是隐藏窗口的一种方法。
#root.geometry('+-1500+-2000')
#root.geometry(Window_inMid())   #使窗口居中

button = tk.Button(root, text="执行", command=callback)
button.pack()
root.protocol('WM_DELETE_WINDOW', QueryWindow)#执行QueryWindow这个回调函数
root.mainloop()



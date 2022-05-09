'''
单选框按钮控件（Radiobutton），同样允许用户选择具体的选项值，不过与 Listbox 相比，
单选按钮控件仅允许用户选择单一的选项值，各个选项值之间是互斥的关系，因此只有一个选项可以被用户选择。

Radiobutton 控件通常都是成组出现的，所有控件都使用相同的变量。Radiobutton 可以包含文本或图像，每一个按钮都可以与一个 Python 函数相关联。
当按钮被按下时，对应的函数会被执行。这里需要注意的是，单选按钮控件仅能显示单一字体的文本，但文本可以跨越多行，除此之外，您还可以为个别的字符添加下划线。
'''

import tkinter as tk

window = tk.Tk()
window.title("C语言中文网")
window.geometry('400x180')
#window.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# IntVar() 用于处理整数类型的变量
v = tk.IntVar()
# 根据单选按钮的 value 值来选择相应的选项
v.set(0)
# 使用 variable 参数来关联 IntVar() 的变量 v
tk.Radiobutton(window, text="C语言中文网", fg='blue',font=('微软雅黑','12','bold'),variable=v, value=0).pack(anchor = 'w')
tk.Radiobutton(window, text="CSDN平台", variable=v, value=2).pack(anchor = 'w')
tk.Radiobutton(window, text="知乎平台", variable=v, value=3).pack(anchor = 'w')
tk.Radiobutton(window, text="牛客网平台", variable=v, value=4).pack(anchor = 'w')
# 显示窗口
window.mainloop()
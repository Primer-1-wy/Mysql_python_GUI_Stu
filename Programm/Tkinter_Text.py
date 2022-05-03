import tkinter as tk

root = tk.Tk()
root.title("C语言中文网")
root.geometry('400x200')
#root.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
text = tk.Text(root, width=35, heigh=15)
text.pack()

text.insert("insert", "C语言中文网")
# 设置标记，这里的 1.end 表示 第一行最后一个字符，当然也可以使用数字来表示比如 1.5 表示第一行第五个字符
text.mark_set("name", "1.end")
# 在标记之后插入相应的文字
text.insert("name", ",网址：c.biancheng.net")
# 跟着自动移动，往后插入，而不是停留在原位置
text.insert("name", ",欢迎光临")
# 若使用 mark_unset() 可以删除指定的标记
# text.mark_unset("name")
# 但使用delete来清楚所有的内容， mark 标记依旧会存在
# text.delete("1.0","end")
# 依然可以使用 name标记来插入
# text.insert("name", "Python答疑")
# 显示窗口
root.mainloop()
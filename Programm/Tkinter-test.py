from tkinter import *
root=Tk()
# # 设置主窗口区的背景颜色以区别画布区的颜色
root.config(bg='#8DB6CD')
root.title("C语言中文网")
root.geometry('500x300')
#root.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# # 将画布设置为白色
cv = Canvas(root,bg='white')
# tkinter 提供的内置位图名称
bitmaps = ["error", "gray75", "gray50", "gray25", "gray12",
"hourglass", "info", "questhead", "question", "warning"]
# 列出所有的位图样式
for i in range(len(bitmaps)):
    # 前两个参数指定一个位图的位置，后续依次排列
    cv.create_bitmap((i+1)*30,30,bitmap=bitmaps[i])

#并在画布上添加文本
# 参数说明，前两个参数（x0，y0）参照点，指定文字字符串的左上角坐标
# anchor 指定了文本的对于参照点的相对位置，以方位来指定,比如 W/E/N/S等
cv.create_text(30,80,text = "tkinter内置位图预览",fill ='#7CCD7C',anchor = W,font =('微软雅黑',15,'bold'))
# 展示图片，使用 PhotoImage()来加载图片
img = PhotoImage (file="C:/Users/Administrator/Desktop/c.biancheng.gif")
cv.create_image(30,150,image = img,anchor =W)
cv.create_text(30,220,text = "图片预览",fill ='#7CCD7C',anchor = W,font =('微软雅黑',15,'bold'))
cv.pack()
mainloop()
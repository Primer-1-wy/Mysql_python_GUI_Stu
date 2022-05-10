from tkinter import *
root = Tk()
# 设置窗口的背景颜色以区别画布
root.config(bg='#87CEEB')
root.title("C语言中文网")
root.geometry('450x350')
root.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# 设置画布的背景颜色为白色
cv=Canvas(root,bg="white",width =300, height = 250)
# 将控件放置在主窗口中
cv.pack()
# 设置坐标点,此处可以元组的形式来设置坐标点
point=[(10,20),(20,30),(30,40),(40,100),(80,120),(150,90)]
# 创建画布，添加线条
# fill 参数指定填充的颜色，如果为空字符串，则表示透明
# dash 参数表示用来绘制虚线轮廓，元组参数，分别代表虚线中线段的长度和线段之间的间隔
# arrow 设线段的箭头样式，默认不带箭头，参数值 first 表示添加箭头带线段开始位置，last表示到末尾占位置，both表示两端均添加
# smooth 布尔值参数，表示是否以曲线的样式划线，默认为 False
# width 控制线宽
line1=cv.create_line(point,fill="purple",dash=(1,1),arrow=LAST,width=5)
print('线段line1的画布id号:',line1)
line2=cv.create_line(point,fill="red",arrow=BOTH,smooth=TRUE,width=5)
print('线段line2的画布id号:',line2)
# 移动其中一条线段，只需要更改其坐标就可以,使用 coords()方法移动曲线
cv.coords(line2,50,30,25,35,35,40,50,120,60,170,10,180)
# 显示窗口
root.mainloop()
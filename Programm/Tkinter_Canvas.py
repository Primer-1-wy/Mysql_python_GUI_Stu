from tkinter import *
root = Tk()
# 设置主窗口区的背景颜色以区别画布区的颜色
root.config(bg='#8DB6CD')
root.title("C语言中文网")
root.geometry('500x400')
#root.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')

# 将画布设置为白色
canvas = Canvas(root,width = 400,height = 400,bg='white')
# 设置基准坐标
x0,y0,x1,y1 = 10,10,80,80
# 绘制扇形,起始角度为 0 度，结束角度为 270, 扇形区域填充色为淡蓝色，轮廓线为蓝色，线宽为 2px
arc = canvas.create_arc(x0, y0, x1, y1,start = 0, extent = 270, fill = '#B0E0E6',outline ='blue',width = 2)
# 绘制圆形
oval = canvas.create_oval(x0+150, y0, x1+150, y1,fill ='#CD950C',outline = 'blue',width=2)
# 绘制矩形,并将轮廓线设置为透明色，即不显示最外围的轮廓线，默认为黑色
rect = canvas.create_rectangle(x0,y0+100,x1,y1+100,fill='red',outline = '')
# 绘制一个三角形，填充色为绿色
trigon = canvas.create_polygon(80,80,150,80,200,200, outline="", fill="green",)

# 当然也可以绘制一个任意多边形，只要你的坐标正确就可以
# 绘制一个多边形，首先定义一系列的多边形上的坐标点
poly_points=[(0,280),(140,200),(140,240),(270,240),(270,320),(140,320),(140,360)]
polygon = canvas.create_polygon(poly_points,fill="#BF3EFF")

# 放置画布在主窗口
canvas.pack()
# 显示窗口
root.mainloop()
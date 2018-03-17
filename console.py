#!/usr/bin/python3

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
from tkinter.scrolledtext import ScrolledText
from hashlib import md5
import re
import time

from Bin_packing_FF import *
from BIn_packing_BT import *
from Bin_packing_BNB import *


top = tk.Tk()
top.title('1D Bin-packing System')
top.geometry('1000x800')


input_frame = tk.Frame(top, width=400, bg='gray', height=300, borderwidth=2)
console_frame = tk.Frame(top, width=600, height=300, bg='red', borderwidth=2)
canvas_frame = tk.Frame(top, width=1000, height=500, borderwidth=2)

input_frame.place(x=0, y=0, anchor='nw')
console_frame.place(x=400, y=0, anchor='nw')
canvas_frame.place(x=0, y=300, anchor='nw')


######################################################
###              the input stage                   ###
######################################################

# 全局变量　　　　容量，物品的ｓｔｒ格式　　　　　选取的选项			容量，物品的ｌｉｓｔ　
item_num_s = ''
goods_s = ''
selection = ''

goods = []
item_num = 0
bins = []		# 用于获取程序运行所得的箱子，进行动画展示

#===========================建立提示标签===========================

class ToolTip(object):  
    def __init__(self, widget):  
        self.widget = widget  
        self.tipwindow = None  
        self.id = None  
        self.x = self.y = 0  
  
    def showtip(self, text):  
        "Display text in tooltip window"  
        self.text = text  
        if self.tipwindow or not self.text:  
            return  
        x, y, _cx, cy = self.widget.bbox("insert")  
        x = x + self.widget.winfo_rootx() + 27  
        y = y + cy + self.widget.winfo_rooty() +27  
        self.tipwindow = tw = tk.Toplevel(self.widget)  
        tw.wm_overrideredirect(1)  
        tw.wm_geometry("+%d+%d" % (x, y))  
  
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,  
                      background="#ffffe0", relief=tk.SOLID, borderwidth=1,  
                      font=("tahoma", "8", "normal"))  
        label.pack(ipadx=1)  
  
    def hidetip(self):  
        tw = self.tipwindow  
        self.tipwindow = None  
        if tw:  
            tw.destroy()  


def createToolTip( widget, text):  
    toolTip = ToolTip(widget)  
    def enter(event):  
        toolTip.showtip(text)  
    def leave(event):  
        toolTip.hidetip()  
    widget.bind('<Enter>', enter)  
    widget.bind('<Leave>', leave)  

 # 展现错误提示

def _msgBox1():
 	mBox.showwarning('Input Error:', '容量格式输入错误！！！')

def _msgBox2():
 	mBox.showwarning('Input Error:', '物品重量输入错误！！！')

def msgBox3():
 	mBox.showwarning('Input Error:', '物品重量不得大于箱子容量！！！')
#===============================================================


tag1 = tk.Label(input_frame, text='The input Stage:', font='Helvetica -24 bold')
tag1.place(x=100, y=0, anchor='nw')

tag2 = tk.Label(input_frame, text='请选择算法：',font='Helvetica -14 bold')
tag2.place(x=0, y= 50, anchor='nw')

variable = tk.StringVar(input_frame)
variable.set("List") # default value
w = tk.OptionMenu(input_frame, variable, "First-fit", "Backtracking-fit", "BranchandBound-fit")
w.place(x=100, y=50, anchor="nw")

tag3 =tk.Label(input_frame, text="请输入箱子容量：",font='Helvetica -14 bold')
tag3.place(x=0, y=100, anchor='nw')

s_e_num = tk.StringVar()
e_num = tk.Entry(input_frame, textvariable=s_e_num)
e_num.place(x=130, y=100, anchor='nw')



l_items = tk.Label(input_frame, text="请输入物品的重量，以逗号隔开：",font='Helvetica -14 bold')
l_items.place(x=0, y=140, anchor="nw")

s_items = ScrolledText(input_frame, width=50, height=6, wrap=tk.WORD)
#
s_items.place(x=8, y=170, anchor="nw")

b_ok = tk.Button(input_frame, text="Run", font='Helvetica -17 bold')
b_ok.place(x=165, y=265, anchor='nw')


# 添加tooltip
createToolTip(e_num, '请输入一个整数')
createToolTip(s_items, '机智的人会永远注意格式的')





###########################################################
###             the output stage                        ###
###########################################################

console_label = ttk.LabelFrame(console_frame, text="Console line:")
console_label.place(x=0, y=0, anchor='nw')
text_scro = ScrolledText(console_label, width=85, height=20)
text_scro.tag_config('a', font='Helvetica -15 bold')
text_scro.pack()


###########################################################
###              the dynamic display area               ###
###########################################################

click_times = 1		#  监听开始按钮
start_canvas = tk.Canvas(top, bg='pink',width=50, height=50)
tri_angel = start_canvas.create_polygon(10, 10, 10, 50, 40, 30)
start_canvas.place(x=0, y=300, anchor='nw')

qick_canvas = tk.Canvas(top, bg='yellow', width=50, height=50)
quick = qick_canvas.create_polygon(10, 25, 40,5 , 40 , 45)
qick_canvas.place(x=850, y=300,anchor='nw')

slow_canvas  =  tk.Canvas(top, bg='yellow', width=50, height='50')
slow = slow_canvas.create_polygon(10,5,10,45,40,25)
slow_canvas.place(x=900, y=300, anchor='nw')



dis_canvas = tk.Canvas(top,  width=1000, height=450)
dis_canvas.place(x=0, y=350, anchor='nw')

p1_file = tk.PhotoImage(file='source/person1.gif')
bg_file = tk.PhotoImage(file='source/bg2.gif')
m1 = dis_canvas.create_image(0, 30, anchor='nw', image=p1_file)
m2 = dis_canvas.create_image(590, 30, anchor='nw', image=bg_file)


car_file = tk.PhotoImage(file='source/turk2.gif')
def add_car(x_, y_, num):
	#car_canvas = tk.Canvas(dis_canvas, width=450, height=150)
	car_text = dis_canvas.create_text(x_, y_, anchor='nw', text='Car '+str(num))
	car_img = dis_canvas.create_image(x_, y_+15, anchor='nw', image=car_file)
	dis_canvas.update()
	#car_canvas.place(x=x_, y=y_,anchor='nw')
	return car_text, car_img

item_file = tk.PhotoImage(file='source/goods_.gif')
def add_item(x_, y_, size):
	#item_canvas = tk.Canvas(dis_canvas, width=200, height=170)
	item_text = dis_canvas.create_text(x_, y_,anchor='nw', text='我是重为'+size+'的货物')
	item_img = dis_canvas.create_image(x_, y_+15, anchor="nw", image=item_file)
	#item_canvas.place(x=x_, y=y_, anchor='nw')
	return item_text, item_img


#  初始化动态演示界面的货车

car1_t, car1_i = add_car(0, 270, 1)
# item1_t, item1_i = add_item(800, 0, 1)




##########################################################
###                       event                        ###
##########################################################
def clear(item):
	item.delete(0, tk.END)

def print_(str, tag='a'):
	#global text_scro
	text_scro.config(state=tk.NORMAL)
	text_scro.insert(tk.END, str, tag)
	text_scro.config(state=tk.DISABLED)


#	获取用户输入的数据，并且调用来自其他三个脚本的不同算法
#   在　　console_frame　　中以ｓｈｅｌｌ形式输出运行结果
#
def get_ins(event):
	global item_num_s, goods_s
	item_num_s = s_e_num.get()
	goods_s = s_items.get(1.0, tk.END)
	print(goods_s, type(goods_s))

	# 验证输入数据
	patern0 = re.compile(r'\d+')
	patern1 = re.compile(r'\d+(,\d+)*')
	item_re = patern0.match(item_num_s)
	goods_re = patern1.match(goods_s)

	tag1 = 0;tag2 = 0
	if (not item_re) or (item_num_s != item_re.group(0)):
		print('\n容量格式错误！！！！！！\n')
		_msgBox1()
	else:
		tag1 = 1
	if (not goods_re):
		print('\n物品重量格式错误！！！！！\n')
		_msgBox2()
	else:
		tag2 = 1
	if tag1 and tag2:
		fun(event)



def fun(event):
	item_num = int(item_num_s)
	goods = list(map(int, goods_s.split(',')))
	for item in goods:
		if item > item_num:
			print('物品重量不得大于箱子容量！！！')
			msgBox3()
			return
	print(type(goods[0]))
	print(repr(event))
	print(selection, type(selection))
	global bins

	if(selection == 'First-fit'):
		print_('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
		print_('\n>>>Using the First-fit Algorithm:')
		print_('\n>>>')
		print(goods, item_num)
		temp = goods.copy()
		start = time.clock()
		bins = nf_binpick(temp, item_num)
		end = time.clock()
		for i in range(len(bins)):
			print_('\n>>>'+str(i+1)+':'+str(bins[i]))
			print(i+1, ":", bins[i])
		print_('\n>>>Use bins:         %s' % len(bins))
		print_('\n>>>Run time:         %7.5f ms' % ((end-start)*1000))
	elif selection == 'Backtracking-fit':
		print_('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
		print_('\n>>>Using the Backtracking-fit Algorithm:')
		print_('\n>>>')
		print(goods, item_num)
		tem = goods.copy()
		start = time.clock()
		bins = loading(tem, item_num)
		end = time.clock()
		for i in range(len(bins)):
			print_('\n>>>'+str(i+1)+':'+str(bins[i]))
			print(i+1, ":", bins[i])
		print_('\n>>>Use bins:         %s' % len(bins))
		print_('\n>>>Run time:         %7.5f ms' % ((end-start)*1000))
	elif selection == 'BranchandBound-fit':
		print_('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
		print_('\n>>>Using the BranchandBound-fit Algorithm:')
		print_('\n>>>')
		print(goods, item_num)
		te = goods.copy()		# 防止对原数据的破坏，进行复制
		start = time.clock()
		bins = loading_(te, item_num)
		end = time.clock()
		for i in range(len(bins)):
			print_('\n>>>'+str(i+1)+':'+str(bins[i]))
			print(i+1, ":", bins[i])
		print_('\n>>>Use bins:         %s' % len(bins))
		print_('\n>>>Run time:         %7.5f ms' % ((end-start)*1000))
		

#============================动态演示控制区＝=============================

speed = 0.25
def quick(event):
	global speed
	speed -= 0.01
	print(repr(event), speed)
def slow(event):
	global speed
	speed += 0.01
	print(repr(event), speed)

def move_car(obj1, obj2, size):
	for i in range(18):
		dis_canvas.move(obj1, size, 0)
		dis_canvas.move(obj2, size, 0)
		dis_canvas.update()
		time.sleep(speed)
slow_canvas.bind("<Button-1>", slow)
qick_canvas.bind('<Button-1>', quick)


def start_dy(event):
	print(repr(event))
	global click_times, car1_i, car1_t
	t1 ,t2 = 0, 0
	if click_times % 2 == 1:
		start_canvas.delete(tk.ALL)
		start_canvas.update()
		start_canvas.create_line((20,10),(20,50),width=6)
		start_canvas.create_line(35,10,35,50,width=6)
		start_canvas.update()
		click_times += 1
		print_('\n正在进行动态演示！！！！！！！')

		index = 1 
		
		for item in bins:
			_goods = item.items
			print_('\n............正在装填第%d辆车' % index)
			for i in _goods:
			 	size = str(i)	#　获取结果的每一个物品
			 	time.sleep(1)

			 	item1_t, item1_i = add_item(800, 270, size)
			 	move_car(item1_t, item1_i, -20)
			 	dis_canvas.delete(item1_t)
			 	dis_canvas.delete(item1_i)
			 	dis_canvas.update()
			print_('\n............第%d辆车装填完毕，快被帅的人开走吧！' % index)

			
			t1 = dis_canvas.create_text(105,65,anchor='nw', text='The system runs perfectly!')
			move_car(car1_t, car1_i, -25)
			time.sleep(1)
			t2 = dis_canvas.create_text(700,50,anchor='nw', text='Of course, it\'s made by J.D!')
			index += 1
			car1_t, car1_i = add_car(0, 270, index)
		dis_canvas.delete(car1_i)
		dis_canvas.delete(car1_t)
		dis_canvas.delete(t1)
		dis_canvas.delete(t2)
		car1_t, car1_i = add_car(0, 270, 1)
		print_('\n动态展示结束！！！！！！！！！！！')
		start_canvas.delete(tk.ALL)
		start_canvas.update()
		start_canvas.create_polygon(10, 10, 10, 50, 40, 30)
		start_canvas.update()
		click_times += 1
	else:
		start_canvas.delete(tk.ALL)
		start_canvas.update()
		start_canvas.create_polygon(10, 10, 10, 50, 40, 30)
		start_canvas.update()
		click_times += 1
#======================================================================


def select(event):
	global selection
	selection = variable.get()
	print(repr(event), selection)

	#print_('\n>>>'+selection)
def show_t():
	print_(time.strftime('%Y年%m月%d日 %H:%M:%S', time.localtime(time.time())))
	

"""
s_items.insert(tk.INSERT,'dvdsv')
goods = s_items.get(1.0, tk.END)
print_('\n'+goods, 'a')
"""

b_ok.bind('<Button-1>', get_ins)

show_t()
print_('\n>>>进入装箱系统：', 'a')
print_('\n>>>loading.............................', 'a')


w.bind('<Button-1>', select)
start_canvas.bind('<Button-1>', start_dy)

"""
s_s_items.set(s_items.get(1.0))
while s_s_items != None:
	b_ok.bind('<Button-1>', print_(s_s_items))
	print(str(s_s_items))
"""


top.mainloop()
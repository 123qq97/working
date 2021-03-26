# coding=gbk
import tkinter
from tkinter import messagebox
from tkinter import ttk
import sys

window = tkinter.Tk()
window.title('测试框架')
window.geometry("400x400+200+50")

#文本区块
'''-------------------------------------------------------------------------------------------Label控件'''
label = tkinter.Label(window,text='this is a text!',bg='pink',fg="black",font=('黑体',20),width=20,height=10,justify='left',anchor='nw')
# label.pack()


#按钮
'''------------------------------------------------------------------------------------------Button控件'''
def func():
    print('方法1')

button1 = tkinter.Button(window,text="按钮",command=func,width=10,height=5)
button2 = tkinter.Button(window,text="按钮",command=lambda:print('I am iron man!!!'))
button3 = tkinter.Button(window,text="退出",command=window.quit ,width=10,height=5)

# button2.pack()
# button3.pack()

#输入框
'''-----------------------------------------------------------------Entry：输入控件，用于显示简单的文本内容'''
# 显示成密文形式
entry1 = tkinter.Entry(window,show="*")
# entry1.pack()

e = tkinter.Variable()
entry2 = tkinter.Entry(window,textvariable=e,font=('Arisl',14))
# entry2.pack()
e.set('wegame') #输入框设置值
# print(e.get())
# print(entry2.get())



'''--------------------------------------------------------------------------------案例一：显示输入框内容'''
def get_text():
    text = input_gettext.get()      #获取输入框内容
    odd_text = v.get()              #获取原文本区块内容
    v.set(odd_text  + text + '\n')  #设置文本区块显示的内容

input_gettext = tkinter.Entry(window)   #输入框
button_gettext = tkinter.Button(window,text='点击获取输入框内容',command=get_text)  #按钮
v = tkinter.StringVar()         #可变文本
label_gettext = tkinter.Label(window, textvariable=v, bg='pink', fg="black", font=('黑体', 20), width=20,height=10, justify='left', anchor='nw')  #文本区块

input_gettext.pack()
button_gettext.pack()
label_gettext.pack()


'''--------------------------------------------------------------------------------------------Text控件'''
#创建滚动条
scroll = tkinter.Scrollbar()
# scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)  #side放到窗体哪一侧，fill填充

#创建多行文本
text = tkinter.Text(window,width=30,height=20)
# text.pack()

str1='北冥有鱼，其名为鲲。鲲之大，不知其几千里也；化而为鸟，其名为鹏。鹏之背，不知其几千里也；怒而飞，其翼若垂天之云。是鸟也，海运则将徙于南冥。南冥者，天池也。《齐谐》者，志怪者也。《谐》之言曰：“鹏之徙于南冥也，水击三千里，抟扶摇而上者九万里，去以六月息者也。”野马也，尘埃也，生物之以息相吹也。天之苍苍，其正色邪？其远而无所至极邪？其视下也，亦若是则已矣。且夫水之积也不厚，则其负大舟也无力。覆杯水于坳堂之上，则芥为之舟，置杯焉则胶，水浅而舟大也。风之积也不厚，则其负大翼也无力。故九万里，则风斯在下矣，而后乃今培风；背负青天，而莫之夭阏者，而后乃今将图南。蜩与学鸠笑之曰：“我决起而飞，抢榆枋而止，时则不至，而控于地而已矣，奚以之九万里而南为？”适莽苍者，三餐而反，腹犹果然；适百里者，宿舂粮；适千里者，三月聚粮。之二虫又何知！'
text.insert(tkinter.INSERT,str1)     #插入文本

#文本与滚动条互相关联
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)


'''-------------------------------------------------------------------------------------------Listbox控件

列表框控件：可以包含一个或多个文本框
作用：在listbox控件的小窗口显示一个字符串
'''

#创建一个listbox,添加几个元素
lb = tkinter.Listbox(window,selectmode=tkinter.BROWSE)
# lb.pack()

for item in ['good','nice','handsome','aaa','bbb','ccc','ddd']:
    #添加：在末尾添加
    lb.insert(tkinter.END,item)

#添加：在开始添加
lb.insert(tkinter.ACTIVE,'cool')
# 添加;将列表当做一个元素添加
lb.insert(tkinter.END,['very good','very nice'])
#删除：删除第1个到第3个的数据；可传一个参数，删除对应下标数据
lb.delete(0,2)
#选中:选中第2个到第4个的数据；可传一个参数，选中对应下标数据
lb.select_set(1,3)
# 取消选中：取消选中第2个到第3个的数据；可传一个参数，取消选中对应下标数据
lb.select_clear(1,2)
# 获取到列表中的元素个数
print(lb.size())
# 获取列表中的值
print(lb.get(1,3))
# 返回当前的索引项
print(lb.curselection())
# 判断：一个选项是否被选中
print(lb.selection_includes(2))



'''---------------------------------------------------------------------------------------Listbox控件二'''
#绑定变量
lbv = tkinter.StringVar()
# 与BORWSE相似，但是不支持鼠标按下后移动选中位置
lb2 = tkinter.Listbox(window,selectmode=tkinter.SINGLE,listvariable=lbv)
# lb2.pack()

for item in ['good','nice','handsome','aaa','bbb','ccc','ddd']:
    # 按顺序添加
    lb2.insert(tkinter.END,item)

# 打印当前列表中的值
print(lbv.get())

#设置值
lbv.set(('1','2','3'))


'''-----------------------------------------------------------------------------------Radiobutton单选框'''
#输出的值给变量r，r的类型为int型
r = tkinter.IntVar()

def radio_updata():
    print(r.get())

radio1 = tkinter.Radiobutton(window,text='one',value=1,variable=r,command=radio_updata)
# radio1.pack()
radio2 = tkinter.Radiobutton(window,text='two',value=2,variable=r,command=radio_updata)
# radio2.pack()


'''-------------------------------------------------------------------------------Checkbutton多选框控件'''
def update():
    message = ""
    if hobby1.get() == True:
        message += "money\n"
    if hobby2.get() == True:
        message += "power\n"
    if hobby3.get() == True:
        message += "people\n"

    check_text.insert(tkinter.INSERT, message)

#要绑定的变量
hobby1 = tkinter.BooleanVar()
hobby2 = tkinter.BooleanVar()
hobby3 = tkinter.BooleanVar()

#多选框
check1 = tkinter.Checkbutton(window,text="money",variable=hobby1,command=update)
check2 = tkinter.Checkbutton(window,text="power",variable=hobby2,command=update)
check3 = tkinter.Checkbutton(window,text="people",variable=hobby3,command=update)

#文本框
check_text = tkinter.Text(window,width=50,height=5)

# check1.pack()
# check2.pack()
# check3.pack()
# check_text.pack()


'''---------------------------------------------------------------------------------------Scale窗口部件'''
#在图形界面上创建一个标签label用以显示并放置
l = tkinter.Label(window,bg='green',fg='white', width=20, text='empty')
# l.pack()

#定义一个触发函数功能
def print_selection(v):
    l.config(text='you have selected ' + v)

#创建一个尺度滑条，长度200字符，从0开始10结束，以2为刻度，精度为0.01，触发调用print_selection函数
s = tkinter.Scale(window, label='try me', from_=0, to=10, orient=tkinter.HORIZONTAL, length=200, showvalue=0,tickinterval=2, resolution=0.01, command=print_selection)
# s.pack()


'''--------------------------------------------------------------------------------------Canvas窗口部件'''
#在图形界面上创建 500 * 200 大小的画布
canvas = tkinter.Canvas(window, bg='green', height=200, width=500)
# 定位图片位置，并导入图片到画布上
image_file = tkinter.PhotoImage(file=r'C:\Users\JF\Desktop\文件存放\证件资料上传\timg.gif')                            # 图片位置
image = canvas.create_image(250, 0, anchor='n',image=image_file)    # 图片锚定点（n图片顶端的中间点位置）放在画布（250,0）坐标处


# 定义多边形参数，然后在画布上画出指定图形
x0, y0, x1, y1 = 100, 100, 150, 150
line = canvas.create_line(x0-50, y0-50, x1-50, y1-50)                   # 画直线
oval = canvas.create_oval(x0+120, y0+50, x1+120, y1+50, fill='yellow')  # 画圆 用黄色填充
arc = canvas.create_arc(x0, y0+50, x1, y1+50, start=0, extent=180)      # 画扇形 从0度打开收到180度结束
rect = canvas.create_rectangle(330, 30, 330+20, 30+20)                  # 画矩形正方形
# canvas.pack()

def moveit():
    canvas.move(rect, 2, 2) # 移动正方形rect（也可以改成其他图形名字用以移动一起图形、元素），按每次（x=2, y=2）步长进行移动

# 第5步，定义一个按钮用来移动指定图形的在画布上的位置
# b = tkinter.Button(window, text='move item',command=moveit).pack()


'''----------------------------------------------------------------------------------------Menu顶层菜单'''
le = tkinter.Label(window,text='    ',bg='green')
# l.pack()

counter = 1
def do_it():
    global counter
    le.config(text='do '+ str(counter))
    counter +=1

#创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
menubar = tkinter.Menu(window)

#创建一个空菜单（默认不下拉）
filemenu = tkinter.Menu(menubar,tearoff=0)

#将上面定义的空菜单命名为File，放在菜单栏中，就是装入那个容器中
menubar.add_cascade(label='File',menu=filemenu)

#在File中加入New、Open、Save等小菜单，即我们平时看到的下拉菜单
filemenu.add_command(label='New',command=do_it)
filemenu.add_command(label='Open',command=do_it)
filemenu.add_command(label='Save',command=do_it)

#添加一条分割线
filemenu.add_separator()
filemenu.add_command(label='Exit',command=window.quit)

submenu= tkinter.Menu(filemenu)
filemenu.add_cascade(label='import',menu=submenu,underline=0)

submenu.add_command(label='packge',command=do_it)
submenu.add_command(label='project',command=do_it)

# 显示菜单栏menubar
# window.config(menu=menubar)

'''---------------------------------------------------------------------------------------Frame 窗口部件'''

# 在图形界面上创建一个标签用以显示内容并放置
# tkinter.Label(window, text='on the window', bg='red', font=('Arial', 16)).pack()  # 和前面部件分开创建和放置不同，其实可以创建和放置一步完成

# 第5步，创建一个主frame，长在主window窗口上
frame = tkinter.Frame(window)
# frame.pack()

# 第6步，创建第二层框架frame，长在主框架frame上面
frame_l = tkinter.Frame(frame)  # 第二层frame，左frame，长在主frame上
frame_r = tkinter.Frame(frame)  # 第二层frame，右frame，长在主frame上
# frame_l.pack(side='left')
# frame_r.pack(side='right')

# 第7步，创建三组标签，为第二层frame上面的内容，分为左区域和右区域，用不同颜色标识
# tkinter.Label(frame_l, text='on the frame_l1', bg='green').pack()
# tkinter.Label(frame_l, text='on the frame_l2', bg='green').pack()
# tkinter.Label(frame_l, text='on the frame_l3', bg='green').pack()
# tkinter.Label(frame_r, text='on the frame_r1', bg='yellow').pack()
# tkinter.Label(frame_r, text='on the frame_r2', bg='yellow').pack()

'''---------------------------------------------------------------------------------------Frame 窗口部件'''
def hit_me():
    tkinter.messagebox.showinfo(title='Hi', message='你好！')            # 提示信息对话窗
    tkinter.messagebox.showwarning(title='Hi', message='有警告！')       # 提出警告对话窗
    tkinter.messagebox.showerror(title='Hi', message='出错了！')         # 提出错误对话窗
    print(tkinter.messagebox.askquestion(title='Hi', message='你好！'))  # 询问选择对话窗return 'yes', 'no'
    print(tkinter.messagebox.askyesno(title='Hi', message='你好！'))     # return 'True', 'False'
    print(tkinter.messagebox.askokcancel(title='Hi', message='你好！'))  # return 'True', 'False'

# 第4步，在图形界面上创建一个标签用以显示内容并放置
# tkinter.Button(window, text='hit me', bg='green', font=('Arial', 14), command=hit_me).pack()

'''-------------------------------------------------------------------窗口部件三种放置方式pack/grid/place'''
#1、grid 是方格, 所以所有的内容会被放在这些规律的方格中
# for i in range(3):
#     for j in range(3):
#         tkinter.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10, ipadx=10, ipady=10)

#2、Pack
# tkinter.Label(window, text='P', fg='red').pack(side='top')    # 上
# tkinter.Label(window, text='P', fg='red').pack(side='bottom') # 下
# tkinter.Label(window, text='P', fg='red').pack(side='left')   # 左
# tkinter.Label(window, text='P', fg='red').pack(side='right')  # 右

#2、Place
# tkinter.Label(window, text='Pl', font=('Arial', 20), ).place(x=50, y=100, anchor='nw')


'''---------------------------------------------------------------------------------下拉列表框(Combobox)'''
def go(*args):  # 处理事件，*args表示可变参数
    print(comboxlist.get())  # 打印选中的值

comvalue=tkinter.StringVar()#窗体自带的文本，新建一个值
comboxlist=ttk.Combobox(window,textvariable=comvalue,state='readonly') #初始化
comboxlist["values"]=("1","2","3","4")
comboxlist.current(0)  #默认选择第一个
comboxlist.bind("<<ComboboxSelected>>",go)  #绑定事件,(下拉列表框被选中时，绑定go()函数)
# comboxlist.pack()




window.mainloop() #进入主循环
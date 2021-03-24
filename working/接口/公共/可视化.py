# coding=gbk
import tkinter

window = tkinter.Tk()
window.title('测试框架')
window.geometry("400x400+200+50")

#文本区块
'''Label控件'''
label = tkinter.Label(window,text='this is a text!',bg='pink',fg="black",font=('黑体',20),width=20,height=10,justify='left',anchor='nw')
# label.pack()


#按钮
'''Button控件'''
def func():
    print('方法1')
button1 = tkinter.Button(window,text="按钮",command=func,width=10,height=5)

button2 = tkinter.Button(window,text="按钮",command=lambda:print('I am iron man!!!'))

button3 = tkinter.Button(window,text="退出",command=window.quit ,width=10,height=5)

# button2.pack()
# button3.pack()

#输入框
'''Entry：输入控件，用于显示简单的文本内容'''
entry1 = tkinter.Entry(window,show="")
# entry1.pack()

e = tkinter.Variable()
entry2 = tkinter.Entry(window,textvariable=e)
# entry2.pack()

e.set('wegame') #输入框设置值
# print(e.get())
# print(entry2.get())

'''案例一：显示输入框内容'''
def get_text():
    text = input_gettext.get()      #获取输入框内容
    odd_text = v.get()              #获取原文本区块内容
    v.set(odd_text  + text + '\n')  #设置文本区块显示的内容

input_gettext = tkinter.Entry(window)   #输入框
button_gettext = tkinter.Button(window,text='点击获取输入框内容',command=get_text)  #按钮
v = tkinter.StringVar()         #可变文本
label_gettext = tkinter.Label(window, textvariable=v, bg='pink', fg="black", font=('黑体', 20), width=20,height=10, justify='left', anchor='nw')  #文本区块

# input_gettext.pack()
# button_gettext.pack()
# label_gettext.pack()


'''Text控件'''
#创建滚动条
scroll = tkinter.Scrollbar()
# scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)  #side放到窗体哪一侧，fill填充

#创建多行文本
text = tkinter.Text(window,width=30,height=20)
# text.pack()

str='北冥有鱼，其名为鲲。鲲之大，不知其几千里也；化而为鸟，其名为鹏。鹏之背，不知其几千里也；怒而飞，其翼若垂天之云。是鸟也，海运则将徙于南冥。南冥者，天池也。《齐谐》者，志怪者也。《谐》之言曰：“鹏之徙于南冥也，水击三千里，抟扶摇而上者九万里，去以六月息者也。”野马也，尘埃也，生物之以息相吹也。天之苍苍，其正色邪？其远而无所至极邪？其视下也，亦若是则已矣。且夫水之积也不厚，则其负大舟也无力。覆杯水于坳堂之上，则芥为之舟，置杯焉则胶，水浅而舟大也。风之积也不厚，则其负大翼也无力。故九万里，则风斯在下矣，而后乃今培风；背负青天，而莫之夭阏者，而后乃今将图南。蜩与学鸠笑之曰：“我决起而飞，抢榆枋而止，时则不至，而控于地而已矣，奚以之九万里而南为？”适莽苍者，三餐而反，腹犹果然；适百里者，宿舂粮；适千里者，三月聚粮。之二虫又何知！'
text.insert(tkinter.INSERT,str)     #插入文本

#文本与滚动条互相关联
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)





'''Checkbutton多选框控件'''
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

'''Radiobutton单选框'''
#输出的值给变量r，r的类型为int型
r = tkinter.IntVar()

def radio_updata():
    print(r.get())

radio1 = tkinter.Radiobutton(window,text='one',value=1,variable=r,command=radio_updata)
# radio1.pack()
radio2 = tkinter.Radiobutton(window,text='two',value=2,variable=r,command=radio_updata)
# radio2.pack()

'''Listbox控件

列表框控件：可以包含一个或多个文本框
作用：在listbox控件的小窗口显示一个字符串
'''

#创建一个listbox,添加几个元素
lb = tkinter.Listbox(window,selectmode=tkinter.BROWSE)
lb.pack()

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


window.mainloop() #进入主循环
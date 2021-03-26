# coding=gbk
import tkinter
from tkinter import messagebox
from tkinter import ttk
import sys

window = tkinter.Tk()
window.title('���Կ��')
window.geometry("400x400+200+50")

#�ı�����
'''-------------------------------------------------------------------------------------------Label�ؼ�'''
label = tkinter.Label(window,text='this is a text!',bg='pink',fg="black",font=('����',20),width=20,height=10,justify='left',anchor='nw')
# label.pack()


#��ť
'''------------------------------------------------------------------------------------------Button�ؼ�'''
def func():
    print('����1')

button1 = tkinter.Button(window,text="��ť",command=func,width=10,height=5)
button2 = tkinter.Button(window,text="��ť",command=lambda:print('I am iron man!!!'))
button3 = tkinter.Button(window,text="�˳�",command=window.quit ,width=10,height=5)

# button2.pack()
# button3.pack()

#�����
'''-----------------------------------------------------------------Entry������ؼ���������ʾ�򵥵��ı�����'''
# ��ʾ��������ʽ
entry1 = tkinter.Entry(window,show="*")
# entry1.pack()

e = tkinter.Variable()
entry2 = tkinter.Entry(window,textvariable=e,font=('Arisl',14))
# entry2.pack()
e.set('wegame') #���������ֵ
# print(e.get())
# print(entry2.get())



'''--------------------------------------------------------------------------------����һ����ʾ���������'''
def get_text():
    text = input_gettext.get()      #��ȡ���������
    odd_text = v.get()              #��ȡԭ�ı���������
    v.set(odd_text  + text + '\n')  #�����ı�������ʾ������

input_gettext = tkinter.Entry(window)   #�����
button_gettext = tkinter.Button(window,text='�����ȡ���������',command=get_text)  #��ť
v = tkinter.StringVar()         #�ɱ��ı�
label_gettext = tkinter.Label(window, textvariable=v, bg='pink', fg="black", font=('����', 20), width=20,height=10, justify='left', anchor='nw')  #�ı�����

input_gettext.pack()
button_gettext.pack()
label_gettext.pack()


'''--------------------------------------------------------------------------------------------Text�ؼ�'''
#����������
scroll = tkinter.Scrollbar()
# scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)  #side�ŵ�������һ�࣬fill���

#���������ı�
text = tkinter.Text(window,width=30,height=20)
# text.pack()

str1='��ڤ���㣬����Ϊ���֮�󣬲�֪�伸ǧ��Ҳ������Ϊ������Ϊ������֮������֪�伸ǧ��Ҳ��ŭ���ɣ�����������֮�ơ�����Ҳ��������������ڤ����ڤ�ߣ����Ҳ������г���ߣ�־����Ҳ����г��֮��Ի������֮������ڤҲ��ˮ����ǧ��ҷ�ҡ�����߾����ȥ������Ϣ��Ҳ����Ұ��Ҳ������Ҳ������֮��Ϣ�വҲ����֮�Բԣ�����ɫа����Զ����������а��������Ҳ�������������ӡ��ҷ�ˮ֮��Ҳ�������为����Ҳ����������ˮ������֮�ϣ����Ϊ֮�ۣ��ñ����򽺣�ˮǳ���۴�Ҳ����֮��Ҳ�������为����Ҳ�������ʾ�������˹�����ӣ������˽���磻�������죬��Ī֮ز���ߣ������˽�ͼ�ϡ�����ѧ�Ц֮Ի�����Ҿ�����ɣ������ʶ�ֹ��ʱ�����������ڵض����ӣ�����֮���������Ϊ������ç���ߣ����Ͷ��������̹�Ȼ���ʰ����ߣ�����������ǧ���ߣ����¾�����֮�����ֺ�֪��'
text.insert(tkinter.INSERT,str1)     #�����ı�

#�ı���������������
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)


'''-------------------------------------------------------------------------------------------Listbox�ؼ�

�б��ؼ������԰���һ�������ı���
���ã���listbox�ؼ���С������ʾһ���ַ���
'''

#����һ��listbox,��Ӽ���Ԫ��
lb = tkinter.Listbox(window,selectmode=tkinter.BROWSE)
# lb.pack()

for item in ['good','nice','handsome','aaa','bbb','ccc','ddd']:
    #��ӣ���ĩβ���
    lb.insert(tkinter.END,item)

#��ӣ��ڿ�ʼ���
lb.insert(tkinter.ACTIVE,'cool')
# ���;���б���һ��Ԫ�����
lb.insert(tkinter.END,['very good','very nice'])
#ɾ����ɾ����1������3�������ݣ��ɴ�һ��������ɾ����Ӧ�±�����
lb.delete(0,2)
#ѡ��:ѡ�е�2������4�������ݣ��ɴ�һ��������ѡ�ж�Ӧ�±�����
lb.select_set(1,3)
# ȡ��ѡ�У�ȡ��ѡ�е�2������3�������ݣ��ɴ�һ��������ȡ��ѡ�ж�Ӧ�±�����
lb.select_clear(1,2)
# ��ȡ���б��е�Ԫ�ظ���
print(lb.size())
# ��ȡ�б��е�ֵ
print(lb.get(1,3))
# ���ص�ǰ��������
print(lb.curselection())
# �жϣ�һ��ѡ���Ƿ�ѡ��
print(lb.selection_includes(2))



'''---------------------------------------------------------------------------------------Listbox�ؼ���'''
#�󶨱���
lbv = tkinter.StringVar()
# ��BORWSE���ƣ����ǲ�֧����갴�º��ƶ�ѡ��λ��
lb2 = tkinter.Listbox(window,selectmode=tkinter.SINGLE,listvariable=lbv)
# lb2.pack()

for item in ['good','nice','handsome','aaa','bbb','ccc','ddd']:
    # ��˳�����
    lb2.insert(tkinter.END,item)

# ��ӡ��ǰ�б��е�ֵ
print(lbv.get())

#����ֵ
lbv.set(('1','2','3'))


'''-----------------------------------------------------------------------------------Radiobutton��ѡ��'''
#�����ֵ������r��r������Ϊint��
r = tkinter.IntVar()

def radio_updata():
    print(r.get())

radio1 = tkinter.Radiobutton(window,text='one',value=1,variable=r,command=radio_updata)
# radio1.pack()
radio2 = tkinter.Radiobutton(window,text='two',value=2,variable=r,command=radio_updata)
# radio2.pack()


'''-------------------------------------------------------------------------------Checkbutton��ѡ��ؼ�'''
def update():
    message = ""
    if hobby1.get() == True:
        message += "money\n"
    if hobby2.get() == True:
        message += "power\n"
    if hobby3.get() == True:
        message += "people\n"

    check_text.insert(tkinter.INSERT, message)

#Ҫ�󶨵ı���
hobby1 = tkinter.BooleanVar()
hobby2 = tkinter.BooleanVar()
hobby3 = tkinter.BooleanVar()

#��ѡ��
check1 = tkinter.Checkbutton(window,text="money",variable=hobby1,command=update)
check2 = tkinter.Checkbutton(window,text="power",variable=hobby2,command=update)
check3 = tkinter.Checkbutton(window,text="people",variable=hobby3,command=update)

#�ı���
check_text = tkinter.Text(window,width=50,height=5)

# check1.pack()
# check2.pack()
# check3.pack()
# check_text.pack()


'''---------------------------------------------------------------------------------------Scale���ڲ���'''
#��ͼ�ν����ϴ���һ����ǩlabel������ʾ������
l = tkinter.Label(window,bg='green',fg='white', width=20, text='empty')
# l.pack()

#����һ��������������
def print_selection(v):
    l.config(text='you have selected ' + v)

#����һ���߶Ȼ���������200�ַ�����0��ʼ10��������2Ϊ�̶ȣ�����Ϊ0.01����������print_selection����
s = tkinter.Scale(window, label='try me', from_=0, to=10, orient=tkinter.HORIZONTAL, length=200, showvalue=0,tickinterval=2, resolution=0.01, command=print_selection)
# s.pack()


'''--------------------------------------------------------------------------------------Canvas���ڲ���'''
#��ͼ�ν����ϴ��� 500 * 200 ��С�Ļ���
canvas = tkinter.Canvas(window, bg='green', height=200, width=500)
# ��λͼƬλ�ã�������ͼƬ��������
image_file = tkinter.PhotoImage(file=r'C:\Users\JF\Desktop\�ļ����\֤�������ϴ�\timg.gif')                            # ͼƬλ��
image = canvas.create_image(250, 0, anchor='n',image=image_file)    # ͼƬê���㣨nͼƬ���˵��м��λ�ã����ڻ�����250,0�����괦


# �������β�����Ȼ���ڻ����ϻ���ָ��ͼ��
x0, y0, x1, y1 = 100, 100, 150, 150
line = canvas.create_line(x0-50, y0-50, x1-50, y1-50)                   # ��ֱ��
oval = canvas.create_oval(x0+120, y0+50, x1+120, y1+50, fill='yellow')  # ��Բ �û�ɫ���
arc = canvas.create_arc(x0, y0+50, x1, y1+50, start=0, extent=180)      # ������ ��0�ȴ��յ�180�Ƚ���
rect = canvas.create_rectangle(330, 30, 330+20, 30+20)                  # ������������
# canvas.pack()

def moveit():
    canvas.move(rect, 2, 2) # �ƶ�������rect��Ҳ���Ըĳ�����ͼ�����������ƶ�һ��ͼ�Ρ�Ԫ�أ�����ÿ�Σ�x=2, y=2�����������ƶ�

# ��5��������һ����ť�����ƶ�ָ��ͼ�ε��ڻ����ϵ�λ��
# b = tkinter.Button(window, text='move item',command=moveit).pack()


'''----------------------------------------------------------------------------------------Menu����˵�'''
le = tkinter.Label(window,text='    ',bg='green')
# l.pack()

counter = 1
def do_it():
    global counter
    le.config(text='do '+ str(counter))
    counter +=1

#����һ���˵������������ǿ��԰�������һ���������ڴ��ڵ��Ϸ�
menubar = tkinter.Menu(window)

#����һ���ղ˵���Ĭ�ϲ�������
filemenu = tkinter.Menu(menubar,tearoff=0)

#�����涨��Ŀղ˵�����ΪFile�����ڲ˵����У�����װ���Ǹ�������
menubar.add_cascade(label='File',menu=filemenu)

#��File�м���New��Open��Save��С�˵���������ƽʱ�����������˵�
filemenu.add_command(label='New',command=do_it)
filemenu.add_command(label='Open',command=do_it)
filemenu.add_command(label='Save',command=do_it)

#���һ���ָ���
filemenu.add_separator()
filemenu.add_command(label='Exit',command=window.quit)

submenu= tkinter.Menu(filemenu)
filemenu.add_cascade(label='import',menu=submenu,underline=0)

submenu.add_command(label='packge',command=do_it)
submenu.add_command(label='project',command=do_it)

# ��ʾ�˵���menubar
# window.config(menu=menubar)

'''---------------------------------------------------------------------------------------Frame ���ڲ���'''

# ��ͼ�ν����ϴ���һ����ǩ������ʾ���ݲ�����
# tkinter.Label(window, text='on the window', bg='red', font=('Arial', 16)).pack()  # ��ǰ�沿���ֿ������ͷ��ò�ͬ����ʵ���Դ����ͷ���һ�����

# ��5��������һ����frame��������window������
frame = tkinter.Frame(window)
# frame.pack()

# ��6���������ڶ�����frame�����������frame����
frame_l = tkinter.Frame(frame)  # �ڶ���frame����frame��������frame��
frame_r = tkinter.Frame(frame)  # �ڶ���frame����frame��������frame��
# frame_l.pack(side='left')
# frame_r.pack(side='right')

# ��7�������������ǩ��Ϊ�ڶ���frame��������ݣ���Ϊ��������������ò�ͬ��ɫ��ʶ
# tkinter.Label(frame_l, text='on the frame_l1', bg='green').pack()
# tkinter.Label(frame_l, text='on the frame_l2', bg='green').pack()
# tkinter.Label(frame_l, text='on the frame_l3', bg='green').pack()
# tkinter.Label(frame_r, text='on the frame_r1', bg='yellow').pack()
# tkinter.Label(frame_r, text='on the frame_r2', bg='yellow').pack()

'''---------------------------------------------------------------------------------------Frame ���ڲ���'''
def hit_me():
    tkinter.messagebox.showinfo(title='Hi', message='��ã�')            # ��ʾ��Ϣ�Ի���
    tkinter.messagebox.showwarning(title='Hi', message='�о��棡')       # �������Ի���
    tkinter.messagebox.showerror(title='Hi', message='�����ˣ�')         # �������Ի���
    print(tkinter.messagebox.askquestion(title='Hi', message='��ã�'))  # ѯ��ѡ��Ի���return 'yes', 'no'
    print(tkinter.messagebox.askyesno(title='Hi', message='��ã�'))     # return 'True', 'False'
    print(tkinter.messagebox.askokcancel(title='Hi', message='��ã�'))  # return 'True', 'False'

# ��4������ͼ�ν����ϴ���һ����ǩ������ʾ���ݲ�����
# tkinter.Button(window, text='hit me', bg='green', font=('Arial', 14), command=hit_me).pack()

'''-------------------------------------------------------------------���ڲ������ַ��÷�ʽpack/grid/place'''
#1��grid �Ƿ���, �������е����ݻᱻ������Щ���ɵķ�����
# for i in range(3):
#     for j in range(3):
#         tkinter.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10, ipadx=10, ipady=10)

#2��Pack
# tkinter.Label(window, text='P', fg='red').pack(side='top')    # ��
# tkinter.Label(window, text='P', fg='red').pack(side='bottom') # ��
# tkinter.Label(window, text='P', fg='red').pack(side='left')   # ��
# tkinter.Label(window, text='P', fg='red').pack(side='right')  # ��

#2��Place
# tkinter.Label(window, text='Pl', font=('Arial', 20), ).place(x=50, y=100, anchor='nw')


'''---------------------------------------------------------------------------------�����б��(Combobox)'''
def go(*args):  # �����¼���*args��ʾ�ɱ����
    print(comboxlist.get())  # ��ӡѡ�е�ֵ

comvalue=tkinter.StringVar()#�����Դ����ı����½�һ��ֵ
comboxlist=ttk.Combobox(window,textvariable=comvalue,state='readonly') #��ʼ��
comboxlist["values"]=("1","2","3","4")
comboxlist.current(0)  #Ĭ��ѡ���һ��
comboxlist.bind("<<ComboboxSelected>>",go)  #���¼�,(�����б��ѡ��ʱ����go()����)
# comboxlist.pack()




window.mainloop() #������ѭ��
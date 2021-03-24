# coding=gbk
import tkinter

window = tkinter.Tk()
window.title('���Կ��')
window.geometry("400x400+200+50")

#�ı�����
'''Label�ؼ�'''
label = tkinter.Label(window,text='this is a text!',bg='pink',fg="black",font=('����',20),width=20,height=10,justify='left',anchor='nw')
# label.pack()


#��ť
'''Button�ؼ�'''
def func():
    print('����1')
button1 = tkinter.Button(window,text="��ť",command=func,width=10,height=5)

button2 = tkinter.Button(window,text="��ť",command=lambda:print('I am iron man!!!'))

button3 = tkinter.Button(window,text="�˳�",command=window.quit ,width=10,height=5)

# button2.pack()
# button3.pack()

#�����
'''Entry������ؼ���������ʾ�򵥵��ı�����'''
entry1 = tkinter.Entry(window,show="")
# entry1.pack()

e = tkinter.Variable()
entry2 = tkinter.Entry(window,textvariable=e)
# entry2.pack()

e.set('wegame') #���������ֵ
# print(e.get())
# print(entry2.get())

'''����һ����ʾ���������'''
def get_text():
    text = input_gettext.get()      #��ȡ���������
    odd_text = v.get()              #��ȡԭ�ı���������
    v.set(odd_text  + text + '\n')  #�����ı�������ʾ������

input_gettext = tkinter.Entry(window)   #�����
button_gettext = tkinter.Button(window,text='�����ȡ���������',command=get_text)  #��ť
v = tkinter.StringVar()         #�ɱ��ı�
label_gettext = tkinter.Label(window, textvariable=v, bg='pink', fg="black", font=('����', 20), width=20,height=10, justify='left', anchor='nw')  #�ı�����

# input_gettext.pack()
# button_gettext.pack()
# label_gettext.pack()


'''Text�ؼ�'''
#����������
scroll = tkinter.Scrollbar()
# scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)  #side�ŵ�������һ�࣬fill���

#���������ı�
text = tkinter.Text(window,width=30,height=20)
# text.pack()

str='��ڤ���㣬����Ϊ���֮�󣬲�֪�伸ǧ��Ҳ������Ϊ������Ϊ������֮������֪�伸ǧ��Ҳ��ŭ���ɣ�����������֮�ơ�����Ҳ��������������ڤ����ڤ�ߣ����Ҳ������г���ߣ�־����Ҳ����г��֮��Ի������֮������ڤҲ��ˮ����ǧ��ҷ�ҡ�����߾����ȥ������Ϣ��Ҳ����Ұ��Ҳ������Ҳ������֮��Ϣ�വҲ����֮�Բԣ�����ɫа����Զ����������а��������Ҳ�������������ӡ��ҷ�ˮ֮��Ҳ�������为����Ҳ����������ˮ������֮�ϣ����Ϊ֮�ۣ��ñ����򽺣�ˮǳ���۴�Ҳ����֮��Ҳ�������为����Ҳ�������ʾ�������˹�����ӣ������˽���磻�������죬��Ī֮ز���ߣ������˽�ͼ�ϡ�����ѧ�Ц֮Ի�����Ҿ�����ɣ������ʶ�ֹ��ʱ�����������ڵض����ӣ�����֮���������Ϊ������ç���ߣ����Ͷ��������̹�Ȼ���ʰ����ߣ�����������ǧ���ߣ����¾�����֮�����ֺ�֪��'
text.insert(tkinter.INSERT,str)     #�����ı�

#�ı���������������
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)





'''Checkbutton��ѡ��ؼ�'''
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

'''Radiobutton��ѡ��'''
#�����ֵ������r��r������Ϊint��
r = tkinter.IntVar()

def radio_updata():
    print(r.get())

radio1 = tkinter.Radiobutton(window,text='one',value=1,variable=r,command=radio_updata)
# radio1.pack()
radio2 = tkinter.Radiobutton(window,text='two',value=2,variable=r,command=radio_updata)
# radio2.pack()

'''Listbox�ؼ�

�б��ؼ������԰���һ�������ı���
���ã���listbox�ؼ���С������ʾһ���ַ���
'''

#����һ��listbox,��Ӽ���Ԫ��
lb = tkinter.Listbox(window,selectmode=tkinter.BROWSE)
lb.pack()

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


window.mainloop() #������ѭ��
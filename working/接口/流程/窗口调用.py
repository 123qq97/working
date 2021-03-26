# coding=gbk
import tkinter
from tkinter import messagebox
from tkinter import ttk
from �ӿ�.����.ƽ̨���� import process
import sys
import os

head_url='http://192.168.0.58:82'
window = tkinter.Tk()
window.title('�Զ����ӿ�')
window.geometry("400x600+800+400")




canvas = tkinter.Canvas(window, width=400, height=135, bg='green')
image_file = tkinter.PhotoImage(file='../����/����/����.gif')
image = canvas.create_image(200, 0, anchor='n', image=image_file)
canvas.pack(side='top')
# tkinter.Label(window, text='Wellcome',font=('Arial', 16)).pack()

node=("��Ӫ����","��س���","��ظ���","�շ�",'�ÿ�ȷ��','��Ҫ��','ִ�иڱ�ע','��������','�ʽ���','��������','�ʽ���','�鵵������','��ȡ��֤��','��������','��������','��������','����','��¥')


def go(*args):  # �����¼���*args��ʾ�ɱ����
    start_node = comboxlist1.get()
    end_node = comboxlist2.get()
    start_node_index =node.index(start_node)
    end_node_index =node.index(end_node)
    odd_num = odd_name.get()

    if odd_name.get() == '':
        tkinter.messagebox.showwarning(title='������ʾ', message='�����뵥�ݺţ�')  # �������Ի���

    if end_node_index < start_node_index:
        tkinter.messagebox.showwarning(title='������ʾ', message='��ʼ�ڵ㲻���ڽ����ڵ�֮ǰ��')  # �������Ի���


    for node_process_name in node[start_node_index:end_node_index+1]:
        '''��ʼ-���������нڵ�'''
        p = process(odd_num=odd_num, head_url=head_url, handing_username='17666121214')
        node_func_dict = {
            '��Ӫ����': p.preliminary_operation_review,
            '��س���': p.risk_review,
            '��ظ���': p.risk_recheck,
            '�շ�': p.charge,
            '�ÿ�ȷ��': p.Payment_confirmation,
            '��Ҫ��': p.collection_requirements,
            'ִ�иڱ�ע': p.insertRiskExecutionRemarks,
            '��������': p.queryRiskGuaranteeMainPage,
            '�ʽ���': p.financial_arrangement,
            '��������': p.fund_arrange,
            '�ʽ���': p.updateArrivalAccountStatus,
            '�鵵������': p.updateCheckDocAndLawsuit,
            '��ȡ��֤��': p.deposit_collection,
            '��������': p.disbursement_application,
            '��������': p.auditBilling,
            '��������': p.process_approval,
            '����': p.payment,
            '��¥': p.foreclosure_building,
        }

        node_func_dict[node_process_name]()

    return




# ����
tkinter.Label(window, text='�����뵥�ݺţ�', font=('Arial', 10)).place(x=90, y=150)
tkinter.Label(window, text='��ʼ�ڵ㣺', font=('Arial', 10)).place(x=90, y=185)
tkinter.Label(window, text='�����ڵ㣺', font=('Arial', 10)).place(x=90, y=225)


#���ݺ������
odd_name = tkinter.Entry(window,width=13,font=('Arisl',11))
odd_name.place(x=200,y=150,height=20)
#�б��1
value1=tkinter.StringVar()#�����Դ����ı����½�һ��ֵ
comboxlist1=ttk.Combobox(window,state='readonly',width=12) #��ʼ��
comboxlist1["values"]=node
comboxlist1.current(0)  #Ĭ��ѡ���һ��
# comboxlist1.bind("<<ComboboxSelected>>",go)  #���¼�,(�����б��ѡ��ʱ����go()����)
comboxlist1.place(x=200,y=185)

#�б��2
comboxlist2=ttk.Combobox(window,state='readonly',width=12) #��ʼ��
comboxlist2["values"]=node
comboxlist2.current(0)  #Ĭ��ѡ���һ��
# comboxlist2.bind("<<ComboboxSelected>>",go)  #���¼�,(�����б��ѡ��ʱ����go()����)
comboxlist2.place(x=200,y=225)



button1 = tkinter.Button(window,text="����",command=go,width=5,height=1).place(x=120,y=260)
button2 = tkinter.Button(window,text='ֹͣ',command=window.quit(),width=5,height=1).place(x=240,y=260)




tkinter.mainloop()
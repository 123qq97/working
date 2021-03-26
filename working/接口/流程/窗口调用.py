# coding=gbk
import tkinter
from tkinter import messagebox
from tkinter import ttk
from 接口.流程.平台流程 import process
import sys
import os

head_url='http://192.168.0.58:82'
window = tkinter.Tk()
window.title('自动化接口')
window.geometry("400x600+800+400")




canvas = tkinter.Canvas(window, width=400, height=135, bg='green')
image_file = tkinter.PhotoImage(file='../公共/案例/加油.gif')
image = canvas.create_image(200, 0, anchor='n', image=image_file)
canvas.pack(side='top')
# tkinter.Label(window, text='Wellcome',font=('Arial', 16)).pack()

node=("运营初审","风控初审","风控复审","收费",'用款确认','收要件','执行岗备注','保函寄送','资金安排','资料推送','资金到账','查档查诉讼','收取保证金','出款申请','出款审批','流程审批','出款','赎楼')


def go(*args):  # 处理事件，*args表示可变参数
    start_node = comboxlist1.get()
    end_node = comboxlist2.get()
    start_node_index =node.index(start_node)
    end_node_index =node.index(end_node)
    odd_num = odd_name.get()

    if odd_name.get() == '':
        tkinter.messagebox.showwarning(title='错误提示', message='请输入单据号！')  # 提出警告对话窗

    if end_node_index < start_node_index:
        tkinter.messagebox.showwarning(title='错误提示', message='开始节点不能在结束节点之前！')  # 提出警告对话窗


    for node_process_name in node[start_node_index:end_node_index+1]:
        '''开始-结束的所有节点'''
        p = process(odd_num=odd_num, head_url=head_url, handing_username='17666121214')
        node_func_dict = {
            '运营初审': p.preliminary_operation_review,
            '风控初审': p.risk_review,
            '风控复审': p.risk_recheck,
            '收费': p.charge,
            '用款确认': p.Payment_confirmation,
            '收要件': p.collection_requirements,
            '执行岗备注': p.insertRiskExecutionRemarks,
            '保函寄送': p.queryRiskGuaranteeMainPage,
            '资金安排': p.financial_arrangement,
            '资料推送': p.fund_arrange,
            '资金到账': p.updateArrivalAccountStatus,
            '查档查诉讼': p.updateCheckDocAndLawsuit,
            '收取保证金': p.deposit_collection,
            '出款申请': p.disbursement_application,
            '出款审批': p.auditBilling,
            '流程审批': p.process_approval,
            '出款': p.payment,
            '赎楼': p.foreclosure_building,
        }

        node_func_dict[node_process_name]()

    return




# 文字
tkinter.Label(window, text='请输入单据号：', font=('Arial', 10)).place(x=90, y=150)
tkinter.Label(window, text='开始节点：', font=('Arial', 10)).place(x=90, y=185)
tkinter.Label(window, text='结束节点：', font=('Arial', 10)).place(x=90, y=225)


#单据号输入框
odd_name = tkinter.Entry(window,width=13,font=('Arisl',11))
odd_name.place(x=200,y=150,height=20)
#列表框1
value1=tkinter.StringVar()#窗体自带的文本，新建一个值
comboxlist1=ttk.Combobox(window,state='readonly',width=12) #初始化
comboxlist1["values"]=node
comboxlist1.current(0)  #默认选择第一个
# comboxlist1.bind("<<ComboboxSelected>>",go)  #绑定事件,(下拉列表框被选中时，绑定go()函数)
comboxlist1.place(x=200,y=185)

#列表框2
comboxlist2=ttk.Combobox(window,state='readonly',width=12) #初始化
comboxlist2["values"]=node
comboxlist2.current(0)  #默认选择第一个
# comboxlist2.bind("<<ComboboxSelected>>",go)  #绑定事件,(下拉列表框被选中时，绑定go()函数)
comboxlist2.place(x=200,y=225)



button1 = tkinter.Button(window,text="运行",command=go,width=5,height=1).place(x=120,y=260)
button2 = tkinter.Button(window,text='停止',command=window.quit(),width=5,height=1).place(x=240,y=260)




tkinter.mainloop()
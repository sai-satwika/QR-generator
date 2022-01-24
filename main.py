
from tkinter import*
from turtle import bgcolor
import qrcode
from PIL import Image,ImageTk 
from resizeimage import resizeimage
class Generateqr:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Generator using Python")
        self.root.resizable(False,False)
        
        title=Label(self.root,text="QR Code Generator",font=("Arial",50),bg='light blue').place(x=0,y=0,relwidth=1)
        #Employee Deails
        #variables
        self.var_emp_code=StringVar()
        self.var_emp_name=StringVar()
        self.var_emp_dept=StringVar()
        self.var_emp_des=StringVar()

        emp_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        emp_Frame.place(x=50,y=100,width=500,height=380)
        emp_title=Label(emp_Frame,text="Employee Details",font=("Arial",30),bg='light blue').place(x=0,y=0,relwidth=1)
        
        
        lbl_emp_code=Label(emp_Frame,text="Employee ID",font=("Arial",15,'bold'),bg='white').place(x=20,y=65)
        lbl_emp_name=Label(emp_Frame,text="Name",font=("Arial",15,'bold'),bg='white').place(x=20,y=105)
        lbl_emp_dept=Label(emp_Frame,text="Department",font=("Arial",15,'bold'),bg='white').place(x=20,y=145)
        lbl_emp_des=Label(emp_Frame,text="Designation",font=("Arial",15,'bold'),bg='white').place(x=20,y=190)
        
        txt_emp_code=Entry(emp_Frame,font=("Arial",15,'bold'),textvariable=self.var_emp_code,bg='white').place(x=200,y=65)
        txt_emp_name=Entry(emp_Frame,font=("Arial",15,'bold'),textvariable=self.var_emp_name,bg='white').place(x=200,y=105)
        txt_emp_dept=Entry(emp_Frame,font=("Arial",15,'bold'),textvariable=self.var_emp_dept,bg='white').place(x=200,y=145)
        txt_emp_des=Entry(emp_Frame,font=("Arial",15,'bold'),textvariable=self.var_emp_des,bg='white').place(x=200,y=190)
        
        btn_generate=Button(emp_Frame,text="Generate QR code",command=self.generate,font=("Arial",10,'bold'),bg='light blue').place(x=90,y=250,width=125,height=30)
        btn_clear=Button(emp_Frame,text="Clear",command=self.clear,font=("Arial",10,'bold'),bg='light blue').place(x=250,y=250,width=100,height=30)
        self.msg=''
        self.lbl_msg=Label(emp_Frame,text=self.msg,font=("Arial",15,'bold'),bg='white')
        self.lbl_msg.place(x=0,y=320,relwidth=1)
        
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_Frame.place(x=600,y=100,width=250,height=380)
        qr_title=Label(qr_Frame,text="Employee QR code",font=("Arial",15),bg='light blue').place(x=0,y=0,relwidth=1)
        self.qr_code=Label(qr_Frame, text="QR Code \nNot Available",font=('Arial',15),bg='light blue',bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)
    def clear(self):
        self.var_emp_code.set('')
        self.var_emp_name.set('')
        self.var_emp_dept.set('')
        self.var_emp_des.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg,fg='red')
        self.qr_code.config(image='')
    def generate(self):
        if self.var_emp_des.get()=='' or self.var_emp_code.get()=='' or self.var_emp_dept.get()=='' or self.var_emp_name.get()=='':
            self.msg='All fields are required Fill all fields'
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"Employee ID: {self.var_emp_code.get()}\nEmployee Name:{self.var_emp_name.get()}\nDepartment:{self.var_emp_dept.get()}\nDesignation:{self.var_emp_des.get()}")
            qr_code=qrcode.make(qr_data)
            #print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("exampleqr/ex_"+str(self.var_emp_code.get())+'.png')
            self.im=ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)
            self.msg='QR Code generated successfully' 
            self.lbl_msg.config(text=self.msg,fg='green')
root=Tk()
ob=Generateqr(root)
root.mainloop()
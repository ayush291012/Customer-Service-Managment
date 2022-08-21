from tkinter import messagebox
from types import *
import pymysql
from tkinter import *
import datetime
import time

from pymysql import NULL





def adminsql(A,B):
    try:
        AA=pymysql.connect(user="root",host="localhost",passwd="aaaa",database="cservice");
        BB=AA.cursor()
        BB.execute("select ID,passwd from admin;")
        BB1=BB.fetchall()
        print(BB1)
        for i in BB1:
            if A.get()==i[0]:
                if B.get()==i[1]:
                    return 1
        else:
            messagebox.showinfo("Error!","Invalid Credentials!")
    except Exception as ex:
        print(ex)
        messagebox.showinfo(ex)
        
        

        
        
def usersql(A,B):
    try:
        AA=pymysql.connect(user="root",host="localhost",passwd="aaaa",database="cservice")
        BB=AA.cursor()
        BB.execute("select ID,passwd from user_log;")
        BB1=BB.fetchall()
        print(BB1)
        for i in BB1:
            if A.get()==i[0]:
                if B.get()==i[1]:
                    return 1
            else:
                messagebox.showinfo("Error!","Invalid Credentials!")
    except Exception as ex:
        print(ex)
        messagebox.showinfo(ex)
        
    




def cs_check_data(A):
    try:
        AA=pymysql.connect(user="root",host="localhost",passwd="aaaa",database="cservice")
        BB=AA.cursor()
        BB.execute("select * from Customer where phone='%s';"%(A.get()))
        BB1=BB.fetchone()
        
        if BB1==None:
            messagebox.showinfo("None","No Results Found!")
            print(BB1,0)
            return [0];

        else:
            messagebox.showinfo("Verfication","Name:%s\n\nAddress:%s\n\nPhone:%s\n\nEmail:%s"%(BB1[1],BB1[2],BB1[4],BB1[5]))
            print(BB1,1);
            return BB1;#return CUID
    except Exception as ex:
        print(ex)
        messagebox.showinfo(ex);








def cs_reg_data(A):
    try:
        AA=pymysql.connect(user="root",host="localhost",passwd="aaaa",database="cservice")
        BB=AA.cursor()
        BB.execute("select count(*) from Customer;")
        BB1=BB.fetchone()[0]
        a=A[0].get()
        b=A[1].get()
        c=A[2].get()
        d=A[3].get()
        e=A[4].get(1.0,"end-1c")

        print(e)

        BB.execute("insert into Customer values(%d,'%s','%s','%s','%s','%s');"%(BB1+1,a,e,c,d,b))
        AA.commit()
        
    except Exception as ex:
        print(ex)
        messagebox.showinfo(ex);
        
        
        


        
def cs_srsql(A,B,C):
    try:
        print(A.get())
        AA=pymysql.connect(user="root",host="localhost",passwd="aaaa",database="cservice")
        BB=AA.cursor()
        BB.execute("select product_name,varient_name from product_log where product_ID='%s';"%(A.get()))
        BB1=BB.fetchone()
        
        B.insert(0,BB1[0])
        C.insert(0,BB1[1])
        
        return BB1


    except Exception as ex:
        print(ex)
        messagebox.showinfo("Error",ex)
        
        
        
        


def cs_ccb(A):
    try:
        list1=[]
        AA=pymysql.connect(user="root",host="localhost",passwd="aaaa",database="cservice")
        BB=AA.cursor()
        BB.execute("select product_ID from product_log;")
        BB1=BB.fetchall()
        for i in BB1:
            list1.append(i[0])
        print(list1)
        A['values']=list1
    except Exception as ex:
        print(ex)
        messagebox.showinfo(ex)
        
# print(cs_check_data());

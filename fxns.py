import time 
import datetime
from tkinter import *
import pymysql

def ttime(A,B):#A as date||B as time
    x=datetime.date.today()#this contains date
    x=str(x)
    x=x.split("-")#x1 is a list splitted my -
    x=x[2]+"-"+x[1]+"-"+x[0]
    
    y=time.ctime()
    y=y.split()#this contains time
    print(y[3])
    A.insert(0,x)
    B.insert(0,y[3])
    A.config(state=DISABLED)#these mine would disable entry box for no further editing
    B.config(state=DISABLED)
    
def cref_Id():
    x1=datetime.date.today()
    x1=str(x1)
    x1=x1.split("-")#x1 is a list splitted my -
    x1=x1[2]+x1[1]+x1[0]#now date is in the format datemonthyear 11102021 
    print(x1)
    y1=time.ctime()
    y1=y1.split()
    y1=y1[3]
    y1=y1.split(":")
    y1=y1[0]+y1[1]+y1[2]#this contains time in hour min sec format 145320
    print(y1)
    
    ref_id=y1 + x1#here is ref id time + date 
    ref_id=int(ref_id)
    print(ref_id)#the call reference id we desired to get in integer format
    return ref_id
def Ex_date(A):
    x1=datetime.date.today()
    x1=str(x1)
    x1=x1.split("-")#x1 is a list splitted my -
    x1[2]=str(int(x1[2]) + 3)#here we added 3 days in the date
    x1=x1[2]+"-"+x1[1]+"-"+x1[0]#now date is in the format datemonthyear 11-10-2021 
    A.insert(0,x1)


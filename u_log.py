from tkinter import *
#from maincall import *
from sql_main import *
from tkinter.ttk import *
from tkinter import ttk as tt




def clean(A):#cleaning Window
    for i in A:
        i.destroy()
def clear(A):
    for i in A:
        i.delete(0,50)
def adminbypass(t,A):
    aa1=adminsql(A[3],A[4])
    if aa1==1:
        clean(A)
        user_login(t)
def userbypass(t,A):
    aa1=usersql(A[3],A[4])
    if aa1==1:
        clean(A)
        cs_sr(t)

    
    
        
    
    
    





def admin_log():#admin Login
    t=Tk()
    t.geometry('640x480')
    
    a=Label(t,text="Admin Login",font=("Verdana",15))
    b=Label(t,text="Admin ID:",font=("Verdana",10))
    c=Label(t,text="Password:",font=("Verdana",10))
    
    d=Entry(t,width=50)
    e=Entry(t,width=50,show="•")
    f=Button(t,text="Next",command=lambda:[adminbypass(t,ad)])
    g=Button(t,text="Clear",command=lambda:[clear([d,e])])
    ad=[a,b,c,d,e,f,g]
        
    a.place(x=250,y=60)
    b.place(x=60,y=140)
    c.place(x=60,y=230)
    
    d.place(x=180,y=140,height=25)
    e.place(x=180,y=230,height=25)
    
    f.place(x=180,y=280,width=145)
    g.place(x=334,y=280,width=145)
    
    t.mainloop()
    
def user_login(t):#User Login
    t.geometry('640x480')
    
    a=Label(t,text="User Login",font=("Verdana",15))
    b=Label(t,text="User ID:",font=("Verdana",10))
    c=Label(t,text="Password:",font=("Verdana",10))
    
    d=Entry(t,width=50)
    e=Entry(t,width=50,show="•")
    f=Button(t,text="Next",command=lambda:[userbypass(t,us)])
    g=Button(t,text="Clear")
    us=[a,b,c,d,e,f,g]
        
    a.place(x=250,y=60)
    b.place(x=60,y=140)
    c.place(x=60,y=230)
    
    d.place(x=180,y=140,height=25)
    e.place(x=180,y=230,height=25)
    
    f.place(x=180,y=280,width=145)
    g.place(x=334,y=280,width=145)
    
    t.mainloop()
    
def cs_sr(t):#Coustomer Service
    t.geometry('640x480')
    
    l1=Label(t,text='Pr_ID:',font=('Verena',10))
    l2=Label(t,text='Pr_Name:',font=('Verena',10))
    l3=Label(t,text='Varient_Name:',font=('Verena',10))
    l4=Label(t,text='CUSTOMER SERVICE',font=('Verena',15))
    
    a=Entry(t,width=50)
    b=Entry(t,width=50)
    c=Entry(t,width=50)
    
    bt=Button(t,text="Next",width=10,command=lambda:[clean([l1,l2,l3,l4,a,b,c,bt,bt1,bt2])])
    bt1=Button(t,text="Clear",width=10,command=lambda:[clear([a,b,c])])
    bt2=Button(t,text="Find",width=10,command=lambda:[cs_srsql(a,b,c)])
    
    
    l1.place(x=50,y=130)
    l2.place(x=50,y=202)
    l3.place(x=50,y=273)
    l4.place(x=220,y=40)
    
    a.place(x=200,y=130,height=25)
    b.place(x=200,y=200,height=25)
    c.place(x=200,y=270,height=25)
    
    bt.place(x=200,y=330,width=141)
    bt1.place(x=350,y=330,width=141)
    bt2.place(x=510,y=130,height=25)
    
    t.mainloop()
admin_log()





from re import L
from tkinter import *
#from maincall import *
from sql_main import *
from tkinter.ttk import *
from tkinter import ttk as tt
from fxns import *




    

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
        Cs_check(t)
 




def csbypass(t,A):    #for customer checking info 
    aa1=cs_check_data(A[2])
    print(aa1)
    if aa1[0]>0:
        clean(A)
        cs_sr(t,aa1)
    

    elif aa1[0]==0:
        z=A[2].get()
        clean(A)
        cus_reg(t,z)






def regbypass(t,A):
    aa1=cs_reg_data([A[6],A[7],A[8],A[9],A[10]])
    
    clean(A)
    cs_sr(aa1)





    
    
        
    
    
    





def admin_log():#admin Login
    
    t=Tk()
    t.geometry('640x480')
    
    Mn=Menu(t)#for menu above the admin login
    #mn=Menu(Mn, tearoff=0)
    
    Mn.add_command(label="Admin WorkSpace")
    
    t.config(menu=Mn)
    
    
    
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










def Cs_check(t):#Customer verfication

    # t=Tk()
    t.geometry('640x480')
    
    Mn=Menu(t)#for menu above the admin login
    #mn=Menu(Mn, tearoff=0)
    
    Mn.add_command(label="Admin WorkSpace")
    
    t.config(menu=Mn)
    
    a=Label(t,text="Customer Verfication",font=("Verdana",15))
    b=Label(t,text="Phone Number:",font=("Verdana",10))
        
    d=Entry(t,width=50)

    f=Button(t,text="Next",command=lambda:[csbypass(t,ad)])     #change function to change
    g=Button(t,text="Clear",command=lambda:[clear([d])])
    
    ad=[a,b,d,f,g]
    
    a.place(x=250,y=60)
    b.place(x=60,y=140)
    
    d.place(x=180,y=140,height=25)

    f.place(x=220,y=280,width=145)
    g.place(x=374,y=280,width=145)
    
    t.mainloop();
    









def cus_reg(t,number):
    # t=Tk()

    t.geometry('640x480')
    
    l1=Label(t,text="Customer Registration",font=("Verdana",15))
    l2=Label(t,text="Name:",font=("Verdana",10))
    l3=Label(t,text="Phone Number 1:",font=("Verdana",10))
    l4=Label(t,text="Phone Number 2:",font=("Verdana",10))
    l5=Label(t,text="Email Address:",font=("Verdana",10))
    l6=Label(t,text="Address:",font=("Verdana",10))
    
    e1=Entry(t,width=50)
    e2=Entry(t,width=50)
    e3=Entry(t,width=50)
    e4=Entry(t,width=50)
    e5=Text(t,width=50)
    
    

    b1=Button(t,text="Next",command=lambda:[regbypass(t,us),cs_sr(t,number)])
    b2=Button(t,text="Clear")

    us=[l1,l2,l3,l4,l5,l6,e1,e2,e3,e4,e5,b1,b2]
        
    l1.place(x=250,y=60)
    l2.place(x=60,y=140)
    l3.place(x=60,y=170)
    l4.place(x=60,y=200)
    l5.place(x=60,y=230)
    l6.place(x=60,y=260)
    
    e1.place(x=180,y=140,height=25)
    e2.place(x=180,y=170,height=25)
    e3.place(x=180,y=200,height=25)
    e4.place(x=180,y=230,height=25)
    e5.place(x=180,y=260,height=100)

    e2.insert(0,number)
    
    b1.place(x=180,y=380,width=250)
    b2.place(x=400,y=380,width=145)
    
    t.mainloop()









def cs_sr(data):#Coustomer Service
    t=Tk()

    t.geometry('700x750')
    
    l1=Label(t,text='Pr_ID:',font=('Verena',10))
    l2=Label(t,text='Pr_Name:',font=('Verena',10))
    l3=Label(t,text='Varient_Name:',font=('Verena',10))
    l4=Label(t,text='CUSTOMER SERVICE',font=('Verena',15))
    l5=Label(t,text='Call Ref. ID:',font=('Verena',10))
    l6=Label(t,text='Customer ID:',font=('Verena',10))
    l7=Label(t,text='Service ID:',font=('Verena',10))
    l8=Label(t,text='Service Name:',font=('Verena',10))
    l9=Label(t,text='Engineer ID:',font=('Verena',10))
    l10=Label(t,text='Date:',font=('Verena',10))
    l11=Label(t,text='Time:',font=('Verena',10))
    l12=Label(t,text='Service Expected Date:',font=('Verena',10))
    
    
    a=tt.Combobox(t,width=47)   #1
    b=Entry(t,width=50)         #2
    c=Entry(t,width=50)         #3
    d=Entry(t,width=50)         #4
    e=Entry(t,width=50)         #5
    f=tt.Combobox(t,width=47)   #6
    g=Entry(t,width=50)         #7
    h=tt.Combobox(t,width=47)   #8
    i=Entry(t,width=50)         #9
    j=Entry(t,width=50)         #10
    k=Entry(t,width=50)         #11
    
    cs=[a,f,h]  #combobox
    cs_ccb(a)
    ttime(i,j)  #this will insert the date time values in entry box
    Ex_date(k)
    
    call_id=cref_Id()
    d.insert(0,call_id)
    d.config(state=DISABLED)
    print(d.get())
    
    
    
    
    bt=Button(t,text="Next",width=10,command=lambda:[clean([l1,l2,l3,l4,a,b,c,bt,bt1,bt2])])
    bt1=Button(t,text="Clear",width=10,command=lambda:[clear([a,b,c])])
    bt2=Button(t,text="Find",width=10,command=lambda:[clear([b,c]),cs_srsql(a,b,c)])
    
    
    l1.place(x=50,y=130)
    l2.place(x=50,y=180)
    l3.place(x=50,y=230)
    l4.place(x=220,y=40)
    l5.place(x=50,y=280)
    l6.place(x=50,y=330)
    l7.place(x=50,y=380)
    l8.place(x=50,y=430)
    l9.place(x=50,y=480)
    l10.place(x=50,y=530)
    l11.place(x=50,y=580)
    l12.place(x=50,y=630)
    
    
    
    a.place(x=200,y=130,height=25)
    b.place(x=200,y=180,height=25)
    c.place(x=200,y=230,height=25)
    d.place(x=200,y=280,height=25)
    e.place(x=200,y=330,height=25)
    f.place(x=200,y=380,height=25)
    g.place(x=200,y=430,height=25)
    h.place(x=200,y=480,height=25)
    i.place(x=200,y=530,height=25)
    j.place(x=200,y=580,height=25)
    k.place(x=200,y=630,height=25)
    
    bt.place(x=210,y=690,width=141)#next
    bt1.place(x=360,y=690,width=141)#clear
    bt2.place(x=600,y=130,height=25)#find
    
    t.mainloop()






admin_log();


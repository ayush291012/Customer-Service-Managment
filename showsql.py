import pymysql
import csv
import os
def dat_show(dat,tab):#this displays the table in csv format
    
    AA=pymysql.connect(user="root",host="localhost",passwd="aaaa",database=dat)
    BB=AA.cursor()
    BB.execute("Select * from %s ;"%(tab))
    A1=BB.fetchall()#it has all the required data
    BB.execute("desc %s"%(tab))
    A2=BB.fetchall()#it has the required fields
    
    
    
    
    A3=[]#Field Name
    A4=[]#field type
    for i in A2:#loop to append values in list
        A3.append(i[0])
        A4.append(i[1])
        
    for i in range(len(A4)):
        if A4[i]=='int':
            pass
        elif A4[i][:3]=='var':
            A4[i]=A4[i][:7]
            
        
    
    
    
    #print(A3)
    #print(A4)
    f1=open("%s_%s.csv"%(dat,tab),"w",newline='')
    s1=csv.writer(f1)
    s1.writerow(A3)#field name
    s1.writerow(A4)#filed type
    s1.writerows(A1)
    f1.close()
    
    os.startfile("%s_%s.csv"%(dat,tab))#opens the file at last of the code
    return ("%s_%s.csv"%(dat,tab))
    
    
    
    
    
def dat_update(csvf,dat,tab):#this update the data in mysql table from csv file
    
    f=open(csvf,"r")
    s=f.read(1000)
    #print(s)
    f.close()
    s=s.split("\n")
    s.pop()
    print(s)
    print()
    for i in range(len(s)):
        s[i]=s[i].split(",")
    print(s)
    print()
    for i in range(len(s[0])):
        if s[1][i]=='int':
            for j in range(2,len(s)):
                s[j][i]=int(s[j][i])
    print(s)
    print()
    st=""
    for i in s[1]:
        if i=="int":
            st=st+"%d,"
        elif i=="varchar":
            st=st+"'%s',"
    st=st[:len(st)-1]
    print(st)
    
    
    
    
    
    
    AA=pymysql.connect(user="root",host="localhost",passwd="aaaa",database=dat)
    BB=AA.cursor()
    #print()#contains values of Sql table
    #print()
    print(s)#contains values of CSV table
    BB.execute("delete from %s;"%(tab))
    AA.commit()

    for i in range(2,len(s)):
        mm=tuple(s[i])
        print(mm)
        exc="insert into %s values("%(tab)+st%mm+");"
        BB.execute(exc)
        AA.commit()
        print("inserted",i)

    os.remove("%s_%s.csv"%(dat,tab))

Az=dat_show("db1","test")
input("Press Enter...")
dat_update(Az,"db1","test")

    
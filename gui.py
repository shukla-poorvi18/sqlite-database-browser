from tkinter import*
from tkinter import filedialog
import sqlite3 as s
import os

scr=Tk()
def opens():
    global c
    global client
    name=filedialog.askopenfilename()
    if name.endswith('.db'):
        client=s.connect(name)
        c=client.cursor()
        c.execute('''SELECT
    name
FROM
    sqlite_master
WHERE
    type='table' AND
    name NOT LIKE "sqlite_%"''')
        l=[]
        for i in c.fetchall():
            l.append(i[0])
        for i,j in enumerate(l):
            listbox.insert(i,j)

    
scr.geometry("1350x750+0+0")


listbox_F = Frame(scr,bg='White',bd=10,height=700,width=400,relief=GROOVE)
listbox_F.place(x=0,y=50)

listbox=Listbox(listbox_F,selectmode='SINGLE',font=('aerial',20,'bold'))


listbox.pack()


def listbox_sel(listbox):
    global result
    table=listbox.get(listbox.curselection())
    result=c.execute('select * FROM {}'.format(table))


def fun():
    global result
    output_F.delete('1.0',END)
    listbox_sel(listbox)
    l=[','.join([str(j) for j in i]) for i in list(result)]
    print(l)
    output_F.insert('1.0',"\n".join(l))

def create1(dbname):
    if str(dbname.endswith('.db')):
        global client
        global c
        client=s.connect(dbname)
        c=client.cursor()
        
def create():
    w=Toplevel(scr,bg='white',bd=4)
    e=Entry(w,bd=4,bg='powder blue',fg='black',relief=SUNKEN)
    e.pack()
    b5=Button(w,bd=4,bg='powder blue',fg='black',text='create',relief=SUNKEN,command=lambda:create1(e.get()))
    b5.pack()

def delete1(dbname):
    os.remove(dbname)
def Delete():
    w=Toplevel(scr,bg='white',bd=4)
    e=Entry(w,bd=4,bg='powder blue',fg='black',relief=SUNKEN)
    e.pack()
    b5=Button(w,bd=4,bg='powder blue',fg='black',text='delete',relief=SUNKEN,command=lambda:delete1(e.get()))
    b5.pack()
    

bt1=Button(scr,padx=16,pady=1,bd=7,fg='black',font=('aerial',12,'bold'),width=4,text='open',bg='powder blue',command=opens).grid(row=0,column=0)
bt2=Button(scr,padx=16,pady=1,bd=7,fg='black',font=('aerial',12,'bold'),width=4,text='create',bg='powder blue',command=create).grid(row=0,column=1)
bt3=Button(scr,padx=16,pady=1,bd=7,fg='black',font=('aerial',12,'bold'),width=4,text='delete',bg='powder blue',command=Delete).grid(row=0,column=2)

    
output_F=Text(scr,bg='white',bd=10,height=40,width=100,relief=GROOVE)
output_F.place(x=400,y=10)
bt4=Button(listbox_F,padx=16,pady=1,bd=7,fg='black',font=('aerial',12,'bold'),width=4,text='enter',bg='powder blue',command=fun)
bt4.place(x=90,y=270)

w=Label(scr,bg='powder blue',bd=4,fg='black',relief=SUNKEN,text='enter the sql querry',font=('aerial',15,'bold'),width=15)
w.place(x=450,y=550)

def sql(q):
    result=c.execute('{}'.format(q.get()))
    client.commit()
    q.delete(0,END)
    fun()
    
    

sqlquerry_E=Entry(scr,bg="powder blue",bd=4,fg='black',relief=SUNKEN,width=45,font=("aerial",15,"bold"))
sqlquerry_E.place(x=650,y=550)
bt4=Button(scr,padx=16,pady=1,bd=7,fg='black',font=('aerial',12,'bold'),width=4,text='SAVE',bg='powder blue',command=lambda:sql(sqlquerry_E))
bt4.place(x=650,y=600)

scr.mainloop()

from tkinter import *
from tkinter import ttk
from datetime import datetime,timedelta,date

win=Tk()
win.geometry('600x400')


dates=Label(win, text='DATE RANGE',font=("Arial",20,'bold','underline'),fg='blue')
dates.place(x=200,y=10)

date1=Label(win, text='From:',font=("Arial",15),fg='grey')
date1.place(x=20,y=60)

date_1=Label(win,text='',font=('Arial',15,'bold'),fg='navy blue')
date_1.place(x=80,y=60)

date2=Label(win, text='To:',font=("Arial",15),fg='grey')
date2.place(x=300,y=60)

date_2=Label(win,text='',font=('Arial',15,'bold'),fg='navy blue')
date_2.place(x=360,y=60)



def btn1_click():
    btn2.place(x=150,y=10)
    btn3.place(x=300,y=10)
    
    btn1.config(font=("Arial",10,'bold','underline'),fg='blue')
    btn1.place(x=10,y=0)
    
                
    btn2.config(font=("Arial",10),fg='black')
    btn3.config(font=("Arial",10),fg='black')
                
    date = datetime.now().strftime("%b %d %Y")
    date= datetime.strptime(date, "%b %d %Y")
    present_date=(date - timedelta(days=0)).strftime('%b %d ,%Y')
    prev_date = (date - timedelta(days=6)).strftime('%b %d ,%Y')
    date_1.config(text=prev_date)
    date_2.config(text=present_date)

                         
def btn2_click():
    btn1.place(x=10,y=10)
    btn3.place(x=300,y=10)
    
    btn2.config(font=("Arial",10,'bold','underline'),fg='blue')
    btn2.place(x=150,y=0)
    
    btn1.config(font=("Arial",10),fg='black')
    btn3.config(font=("Arial",10),fg='black')
    
    date = datetime.now().strftime("%b %d %Y")
    date = datetime.strptime(date, "%b %d %Y")
    present_date=(date - timedelta(days=0)).strftime('%b %d ,%Y')
    prev_date = (date - timedelta(days=29)).strftime('%b %d ,%Y')
    
    date_1.config(text=prev_date)
    date_2.config(text=present_date)

    
def btn3_click():
    
    btn1.place(x=10,y=10)
    btn2.place(x=150,y=10)
    
    btn3.config(font=("Arial",10,'bold','underline'),fg='blue')
    btn3.place(x=300,y=0)
    
    btn2.config(font=("Arial",10),fg='black')
    btn1.config(font=("Arial",10),fg='black')
    
    date = datetime.now().strftime("%b %d %Y")
    date = datetime.strptime(date, "%b %d %Y")
    present_date=(date - timedelta(days=0)).strftime('%b %d ,%Y')
    
    prev_date_slice=int(present_date[4:6])-1
    
    
    prev_date = (date - timedelta(days=prev_date_slice)).strftime('%b %d ,%Y')
    
    date_1.config(text=prev_date)
    date_2.config(text=present_date)

frame1=Frame(win,width=500,height=40,bg='light grey',bd=0)
frame1.place(x=20,y=220)


btn1=Button(frame1,text='7 days',font=("Arial",10),bd=0,fg='black',bg='light grey',activebackground='light grey',command=btn1_click)
btn1.place(x=10,y=10)

btn2=Button(frame1,text='30 days',font=("Arial",10),bd=0,fg='black',bg='light grey',activebackground='light grey',command=btn2_click)
btn2.place(x=150,y=10)

btn3=Button(frame1,text='This month',font=("Arial",10),bd=0,fg='black',bg='light grey',activebackground='light grey',command=btn3_click)
btn3.place(x=300,y=10)

win.mainloop()

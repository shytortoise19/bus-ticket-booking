from tkinter import*
import sqlite3

con=sqlite3.Connection('bus_db')
cur=con.cursor()
root= Tk()
h,w,= root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
img =PhotoImage(file=".\\Bus_for_project.png")
Label(root,image = img).grid(row=0,column=0,padx=w//3+100,sticky='n',columnspan=10)

def cmd():
   frame=LabelFrame(root)
   Label(frame,text='Passengers :Anugya\t   Gender :F',font='bold').grid(row=0,column=0)
   Label(frame,text='No of seats :2 \t      Phone No:7080129266',font='bold').grid(row=1,column=0)
   Label(frame,text='Age :18\t              Fare Rs :2000  ',font='bold').grid(row=2,column=0)
   Label(frame,text='Booking Ref :8 \t           Bus Detail:Ashoka',font='bold').grid(row=3,column=0)
   Label(frame,text='Travel On :16/11/22\t        Booked On :29/11/22 ',font='bold').grid(row=4,column=0)
   Label(frame,text='Boarding Point  :Guna ',font='bold').grid(row=5,column=0)
   Label(frame,text='Total amount to be paid Rs 1500  at the time of boarding of bus ').grid(row=5,column=0)
   frame.grid(row=2,column=1,pady=h//40)
   
def chk():
    cur.execute("select * from passenger as p, booking_history as b where p.phone_no={0} and p.ref_id=b.ref_id".format(mob.get()))
    res=cur.fetchall()
    if res:
        cmd()
    else:
        Label(root,text = "no booking made",font="Arial 20 bold").grid(row= 11 , column = 2,pady=20)

Label(root,text = "Online Bus Booking System",font="Arial 30 bold" ,bg="steelblue1",fg="IndianRed1" ).grid(row=1,column=0,columnspan=10,pady=20)
Label(root,text = "Check Your Booking ",font="Arial 20 bold" ,bg="lawn green",fg="IndianRed1" ).grid(row=3,column=0,columnspan=10,pady=20)
fr=Frame(root)
fr.grid(row= 0 )
fr1=Frame(root)
Label(fr1,text = "Enter Your Mobile Number: ").grid(row= 10 , column = 0,pady=20)
mob=IntVar()
Entry(fr1,textvariable=mob).grid(row= 10, column = 2)
Button(fr1, text = 'Check Booking',command=chk).grid(row= 10, column = 4)
fr1.grid(row= 4,column=2,padx=w//3 )

cur.execute('create table IF NOT EXISTS passenger(phone_no int NOT NULL,name varchar(20),gender varchar(10),age int,ref_id int);')
cur.execute('create table IF NOT EXISTS booking_history(ref_id int NOT NULL,fare int,to_loc varchar(10),from_loc varchar(10),seats int,booked date,travel date);')

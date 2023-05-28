from tkinter import*
import tkinter.messagebox
import sqlite3
'''con=sqlite3.connect('MY BUS')
cur=con.cursor()
cur.execute("create table if not exists Passengerdetails(Name varchar(20),Gender varchar(2),No_of_seats int(10),Mobile_no int(10),Age int (3))")
con.commit()
con.close()'''
root=Tk()
root.title('seat_book,check,add_details')
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=bus).grid(row=0,column=0,columnspan=10,padx=w//3)
Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='Arial 14 bold').grid(row=1,column=0,columnspan=10,pady=40)
Label(root,text='Enter Journey Details',bg='chartreuse2',fg='dark green',font='Arial 10 bold').grid(row=2,column=0,columnspan=10,pady=10)
Label(root,text='To').grid(row=3,column=0)
a=Entry(root)
a.grid(row=3,column=1)
Label(root,text='From').grid(row=3,column=2)
b=Entry(root)
b.grid(row=3,column=3)
Label(root,text='Journey Date').grid(row=3,column=4)
c=Entry(root)
c.grid(row=3,column=5)
Label(root,text='Format_DD-MM-YYYY').grid(row=3,column=6)
'''def val():
    cur.execute('Select * from Busdetails,Operator where')'''

def fun1():
    Label(root,text='Select Bus',font='Arial 10',fg='green').grid(row=4,column=1)
    Label(root,text='Operator',font='Arial 10',fg='green').grid(row=4,column=2)
    Label(root,text='Bus Type',font='Arial 10',fg='green').grid(row=4,column=3)
    Label(root,text='Available/Capacity',font='Arial 10',fg='green').grid(row=4,column=4)
    Label(root,text='Fare',font='Arial 10',fg='green').grid(row=4,column=5)
    Radiobutton(root,text='Bus1',font='Arial 10',bg='light blue').grid(row=5,column=1)
    Label(root,text='Ashoka',font='Arial 10 italic',fg='blue').grid(row=5,column=2)
    Label(root,text='AC 2X2',font='Arial 10',fg='blue').grid(row=5,column=3)
    Label(root,text='25/30',font='Arial 10',fg='blue').grid(row=5,column=4)
    Label(root,text='1000',font='Arial 10',fg='blue').grid(row=5,column=5)
    Button(root,text='Proceed to Book',command=fun2,font='Arial 10',bg='light green').grid(row=5,column=8)
def fun2():
    Label(root,text='Fill Passenger Details To Book The Bus Ticket',bg='light blue',fg='red',font='Arial 14 bold').grid(row=7,column=0,columnspan=10,pady=10)
    Label(root,text='Name',font='Arial 8').grid(row=8,column=0)
    Entry(root).grid(row=8,column=1)
    Label(root,text='Gender',font='Arial 8').grid(row=8,column=2)
    Entry(root).grid(row=8,column=3)
    Label(root,text='No of seats',font='Arial 8').grid(row=8,column=4)
    Entry(root).grid(row=8,column=5)
    Label(root,text='Mobile No',font='Arial 8').grid(row=8,column=6)
    Entry(root).grid(row=8,column=7)
    Label(root,text='Age',font='Arial 8').grid(row=8,column=8)
    Entry(root).grid(row=8,column=9)
def fun4():
    tkinter.messagebox.showinfo("Success","Your confirmed fare is 2000")
    root.destroy()
    import pg4
Button(root,text='Book Seat',command=fun4,font='Arial 10',bg='light green').grid(row=8,column=10)
'''con.execute("")'''
Button(root,text='Show Bus',command=fun1,bg='light green').grid(row=3,column=7)
home=PhotoImage(file="home.png")
Label(root,image=home).grid(row=3,column=8)
root.mainloop()
    

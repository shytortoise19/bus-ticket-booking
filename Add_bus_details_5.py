from tkinter import*
from tkinter.messagebox import *
root= Tk()
import sqlite3

con=sqlite3.Connection('bus_db')
cur=con.cursor()
cur.execute('create table IF NOT EXISTS buses(bid int primary key NOT NULL,fare int,type varchar(10),capacity int,op_id int,route_id int);')
h,w,= root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

img =PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=img).grid(row=0,column=0,padx=w//3+100,sticky='n',columnspan=14)
Label(root,text="Online Bus Booking System" ,font="Arial 30 bold" ,bg="steelblue1",fg="IndianRed1" ).grid(row=1,column=0,columnspan=14,pady=20)
Label(root,text = "Add Bus Details", font = "arial 20 bold",bg = 'light green', fg ='green').grid(row = 2, column = 0, columnspan=14,pady = 20)

bid=IntVar()
Label(root,text = "Bus ID").grid(row=3 , column = 0)
busid=Entry(root,width=9,textvariable=bid)
busid.grid(row = 3 , column =1)

##Label(root,text = "From").grid(row=3 , column = 2)
##source=Entry(root).grid(row = 3 , column =3)
##
##Label(root,text = "To",width=5).grid(row=3 , column = 4)
##source=Entry(root).grid(row = 3 , column =5)
tye=StringVar();
gen=['AC 2X2','AC 3X2','NON AC 2X2','NON AC 3X2','NON AC SLEEPER 2X1','AC SLEEPER 2X1']
Label(root,text = "Bus Type").grid(row=3 , column = 2)
OptionMenu(root,tye,*(gen)).grid(row = 3 , column =3)

cap=IntVar()
Label(root,text = "Capacity").grid(row=3 , column = 4)
Entry(root,textvariable=cap).grid(row = 3 , column =5)

fare=IntVar()
Label(root,text = "Fare Rs").grid(row=3 , column = 6)
Entry(root,width=7,textvariable=fare).grid(row = 3 , column =7)

op_id=IntVar()
Label(root,text = "Opeartor ID").grid(row=3 , column = 8)
Entry(root,width=9,textvariable=op_id).grid(row = 3 , column =9)

route_id=IntVar()
Label(root,text = "Route ID").grid(row=3 , column = 10)
Entry(root,width=9,textvariable=route_id).grid(row = 3 , column =11)


def add_bus():
    li=[bid.get(),tye.get(),cap.get(),fare.get(),op_id.get(),route_id.get()]
    cur.execute('select * from buses where bid={0}'.format(li[0]))
    res=cur.fetchall()
    if res or li[0]==0 or li[2]==0 or li[3]==0 or li[4]==0 or li[5]==0:
        showerror('Error','bus already exist or information missing')
    else:
        #Label(root,text = li).grid(row=10 , column = 1)
        cur.execute('insert into buses(bid,type,capacity,fare,op_id,route_id) values(?,?,?,?,?,?)',li)
        con.commit()
        showinfo('done','Bus added succesfully')
        
Button(root, text= 'Add Bus',fg ='black', font="Arial 15 bold" ,bg= 'light green',command=add_bus).grid(row= 6 ,column = 5)

def edit_bus():
    li=[bid.get(),tye.get(),cap.get(),fare.get(),op_id.get(),route_id.get()]
    cur.execute('select * from buses where bid={0}'.format(li[0]))
    res=cur.fetchall()
    if not(res) or li[0]==0 or li[2]==0 or li[3]==0 or li[4]==0 or li[5]==0:
        showerror('Error','bus doesnt exist or information missing')
    else:
       cur.execute('update buses set (type="{1}",capacity={2},fare={3},op_id={4},route_id={5} )where bid={0}'.format(li[0],li[1],li[2],li[3],li[4],li[5]))  
       con.commit()
       showinfo('done','Bus details updated succesfully')
Button(root,text='Edit Bus',fg ='black' ,bg= 'light green',font="Arial 15 bold",command=edit_bus).grid(row= 6 ,column = 7)
img1 =PhotoImage(file=".\\home.png")
def close():
    root.destroy()
    import option_2
Button(root,fg ='black' ,bg= 'light green',image = img1,font="Arial 15 bold",command=close ).grid(row= 6 ,column = 9, padx = 2)

root.mainloop

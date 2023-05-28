from tkinter import *
import sqlite3

con=sqlite3.Connection('bus_db')
cur=con.cursor()
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
img=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=img).grid(row=0,column=0,padx=w//3+100,sticky='n',columnspan=10)
Label(root,text="Online Bus Booking System" ,font="Arial 30 bold" ,bg="steelblue1",fg="IndianRed1" ).grid(row=1,column=0,columnspan=10,pady=20)
Label(root,text="Enter Journey Details" ,font="Arial 20 bold" ,bg="lawn green",fg="IndianRed1" ).grid(row=3,column=0,columnspan=10,pady=20)
Label(root,text="To ",font="arial 15").grid(row=4,column=1)
source=Entry(root, font=('calibre',10,'normal')).grid(row=4,column=2)
Label(root,text="From ",font="arial 15").grid(row=4,column=3)
destination=Entry(root, font=('calibre',10,'normal')).grid(row=4,column=4)
Label(root,text="Journey Date ",font="arial 15").grid(row=4,column=5)
date=Entry(root, font=('calibre',10,'normal')).grid(row=4,column=6)
##def search():
##    cur.execute('select * from buses where source={0} and destination={1} and date={2}'.format(source,destination,date))

Button(root,text="show buses",font="arial 15 bold",bg='darkolivegreen3',command=search).grid(row=4,column=7)
def close():
    root.destroy()
    import option_2
img1=PhotoImage(file=".\\home.png")
Button(root,image=img1,command=close).grid(row=4,column=8)
root.mainloop()

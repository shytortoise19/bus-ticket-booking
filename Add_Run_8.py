from tkinter import*
import sqlite3

con=sqlite3.Connection('bus_db')
cur=con.cursor()
root= Tk()
h,w,= root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
img =PhotoImage(file=".\\Bus_for_project.png")
Label(root,image = img).grid(row=0,column=0,padx=w//3+100,sticky='n',columnspan=10)
Label(root,text = "Online Bus Booking System",font="Arial 30 bold" ,bg="steelblue1",fg="IndianRed1" ).grid(row=1,column=0,columnspan=10,pady=20)

Label(root,text = "Enter Journey Details",font="Arial 20 bold" ,bg="lawn green",fg="IndianRed1" ).grid(row=2,column=0,columnspan=10,pady=20)

Label(root,text = "Bus Id").grid(row=3 , column = 2)
Text(root, width = 20 , height = 1).grid(row = 3 , column =3)

Label(root,text = "Running Date").grid(row=3 , column = 4)
Text(root, width = 20 , height = 1).grid(row = 3 , column =5)

Label(root,text = "Seat Available").grid(row=3 , column = 6)
Text(root, width = 20 , height = 1).grid(row = 3 , column =7)
fr=Frame(root)
fr.grid(row= 0 )
fr1=Frame(root)
Button(fr1, text= 'Add Run',fg ='black' ,bg= 'light green').grid(row= 4 ,column = 2)
Button(fr1, text= 'Delete Run',fg ='black',bg='Red').grid(row= 4 ,column = 4)
img1 =PhotoImage(file=".\\home.png")
Button(fr1,fg ='black' ,bg= 'light green',image = img1).grid(row= 4 ,column = 6, padx = 10)
fr1.grid(row= 4,padx=w//3 )
root.mainloop

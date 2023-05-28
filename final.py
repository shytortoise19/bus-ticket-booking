from tkinter import *
##    def __init__(self):
##        img=PhotoImage(file=".\\Bus_for_project.png")
##
def close():
    Tk.destroy()
def info_1():
    root=Tk()
    w,h=root.winfo_screenwidth(),root.winfo_screenheight()
    root.geometry("%dx%d+0+0"%(w,h))
    img=PhotoImage(file="C:/Users/ISHA/Documents/ap/Bus_for_project.png")
    Label(root,image=img).pack()
    Label(root,text="Online Bus Booking System" ,font="Arial 30 bold" ,bg="steelblue1",fg="IndianRed1" ).pack()
    Label(root,text="",font="Arial 25 bold",fg="IndianRed1").pack()
    Label(root,text="Name: ISHA SHRIVASTAVA\nEnrollment number:211B143\nmobile:0000000",font="corbel 20" ,fg="deepskyblue4").pack()
    Label(root,text="",font="Arial 25 bold",fg="IndianRed1").pack()
    Label(root,text="Submitted to:Dr. Mahesh Kumar",font="Arial 25 bold" ,bg="steelblue1",fg="IndianRed1").pack()
    Label(root,text="Project based Learning" ,font="Arial 15" ,fg="IndianRed1" ).pack()
    Button(root,text="next",command=option_2).pack()
    #root.bind('<Enter>',root.destroy)
    #self.option()
    #root.mainloop()
    
def option_2():
    root=Tk()
    w,h=root.winfo_screenwidth(),root.winfo_screenheight()
    root.geometry("%dx%d+0+0"%(w,h))
    img=PhotoImage(file="C:/Users/ISHA/Documents/ap/Bus_for_project1.png")
    Label(root,image=img).grid(row=0,column=0,padx=w//3+100,sticky='n',pady=30,columnspan=10)
    Label(root,text="Online Bus Booking System" ,font="Arial 30 bold" ,bg="steelblue1",fg="IndianRed1" ).grid(row=1,column=0,columnspan=10,pady=20)
    Button(root,text="Seat Booking",font="arial 15 bold",bg='darkolivegreen3',command=busdetails_3).grid(row=3,column=0,padx=w//11)
    Button(root,text="Check Booked Seat",font="arial 15 bold",bg='darkolivegreen3').grid(row=3,column=2,padx=w//11)
    Button(root,text="Add bus details",font="arial 15 bold",bg='darkolivegreen4').grid(row=3,column=4,padx=w//11)
    Label(root,text="only for admin",font="calibri 10").grid(row=4,column=4)

def busdetails_3():
    root=Tk()
    w,h=root.winfo_screenwidth(),root.winfo_screenheight()
    root.geometry("%dx%d+0+0"%(w,h))
    img=PhotoImage(file="C:/Users/ISHA/Documents/ap/Bus_for_project.png")
    Label(root,image=img).grid(row=0,column=0,padx=w//3+100,sticky='n',pady=30,columnspan=10)
    Label(root,text="Online Bus Booking System" ,font="Arial 30 bold" ,bg="steelblue1",fg="IndianRed1" ).grid(row=1,column=0,columnspan=10,pady=20)
    Label(root,text="Enter Journey Details" ,font="Arial 20 bold" ,bg="lawn green",fg="IndianRed1" ).grid(row=3,column=0,columnspan=10,pady=20)
    Label(root,text="To ",font="arial 15").grid(row=4,column=1)
    Entry(root, font=('calibre',10,'normal')).grid(row=4,column=2)
    Label(root,text="From ",font="arial 15").grid(row=4,column=3)
    Entry(root, font=('calibre',10,'normal')).grid(row=4,column=4)
    Label(root,text="Journey Date ",font="arial 15").grid(row=4,column=5)
    Entry(root, font=('calibre',10,'normal')).grid(row=4,column=6)
    Button(root,text="show buses",font="arial 15 bold",bg='darkolivegreen3').grid(row=4,column=7)
    img1=PhotoImage(file=".\\home.png")
    Button(root,image=img1).grid(row=4,column=8)

option_2()

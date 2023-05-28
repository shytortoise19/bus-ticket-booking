from tkinter import *

root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
img=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=img).grid(row=0,column=0,padx=w//3+100,sticky='n',columnspan=10)
def close():
    root.destroy()
    import busdetails_3
def close1():
    root.destroy()
    import check_tickets_9
def close2():
    root.destroy()
    import add_new_details_4
Label(root,text="Online Bus Booking System" ,font="Arial 30 bold" ,bg="steelblue1",fg="IndianRed1" ).grid(row=1,column=0,columnspan=10,pady=20)
Button(root,text="Seat Booking",font="arial 15 bold",bg='darkolivegreen3',command=close).grid(row=3,column=0,padx=w//11)
Button(root,text="Check Booked Seat",font="arial 15 bold",bg='darkolivegreen3',command=close1).grid(row=3,column=2,padx=w//11)
Button(root,text="Add bus details",font="arial 15 bold",bg='darkolivegreen4',command=close2).grid(row=3,column=4,padx=w//11)
Label(root,text="only for admin",font="calibri 10").grid(row=4,column=4)
root.mainloop()

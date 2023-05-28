from tkinter import *
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
img=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=img).pack()
Label(root,text="Online Bus Booking System" ,font="Arial 30 bold" ,bg="steelblue1",fg="IndianRed1" ).pack()
Label(root,text="",font="Arial 25 bold",fg="IndianRed1").pack()
Label(root,text="Name: ISHA SHRIVASTAVA\nEnrollment number:211B143\nmobile:0000000",font="corbel 20" ,fg="deepskyblue4").pack()
Label(root,text="",font="Arial 25 bold",fg="IndianRed1").pack()
Label(root,text="Submitted to:Dr. Mahesh Kumar",font="Arial 25 bold" ,bg="steelblue1",fg="IndianRed1").pack()
Label(root,text="Project based Learning" ,font="Arial 15" ,fg="IndianRed1" ).pack()

def close():
    root.destroy()
    import option_2
root.after(3000,close)
root.mainloop()

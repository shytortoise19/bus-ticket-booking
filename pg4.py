from tkinter import*
import tkinter.messagebox
root=Tk()
root.title('Splash screen')
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=bus).grid(row=0,column=0,columnspan=50,padx=w//3)

Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='Arial 14 bold').grid(row=1,column=0,columnspan=100,pady=40)
Label(root,text='Bus Ticket').grid(row=2,columnspan=100)
Label(root,text='Passengers :',font='Arial 10 bold').grid(row=3,column=1,padx=(w/3,0))
Label(root,text='Anugya',font='Arial 10 bold').grid(row=3,column=2)
Label(root,text='Gender :',font='Arial 10 bold').grid(row=3,column=4)
Label(root,text='F',font='Arial 10 bold').grid(row=3,column=5)
Label(root,text='No of seats:',font='Arial 10 bold').grid(row=4,column=1,padx=(w/3,0))
Label(root,text='2',font='Arial 10 bold').grid(row=4,column=2)
Label(root,text='Phone:',font='Arial 10 bold').grid(row=4,column=4)
Label(root,text='7080129266',font='Arial 10 bold').grid(row=4,column=5)
Label(root,text='Age :',font='Arial 10 bold').grid(row=5,column=1,padx=(w/3,0))
Label(root,text='18',font='Arial 10 bold').grid(row=5,column=2)
Label(root,text='Fare Rs :',font='Arial 10 bold').grid(row=5,column=4)
Label(root,text='2000.00',font='Arial 10 bold').grid(row=5,column=5)
Label(root,text='Booking Ref :',font='Arial 10 bold').grid(row=6,column=1,padx=(w/3,0))
Label(root,text='8',font='Arial 10 bold').grid(row=6,column=2)
Label(root,text='Bus Detail :',font='Arial 10 bold').grid(row=6,column=4)
Label(root,text='Ashoka',font='Arial 10 bold').grid(row=6,column=5)
Label(root,text='Travel on :',font='Arial 10 bold').grid(row=7,column=1,padx=(w/3,0))
Label(root,text='16/11/22',font='Arial 10 bold').grid(row=7,column=2)
Label(root,text='Booked On :',font='Arial 10 bold').grid(row=7,column=4)
Label(root,text='29/11/22',font='Arial 10 bold').grid(row=7,column=5)
Label(root,text='No of Seats:',font='Arial 10 bold').grid(row=8,column=1,padx=(w/3,0))
Label(root,text='2',font='Arial 10 bold').grid(row=8,column=2)
Label(root,text='Boarding point :',font='Arial 10 bold').grid(row=8,column=4)
Label(root,text='Guna',font='Arial 10 bold').grid(row=8,column=5)
Label(root,text='Total amount of Rs 1500.00/- to be paid at the time of boarding',font='Arial 8').grid(row=9,columnspan=100,pady=10)
def fun():
    tkinter.messagebox.showinfo("Success","Here by you confirm the booking")
Button(root,text='Confirm',command=fun,bg='misty rose').grid(row=10,column=3,pady=20)
def fun1():
    root.destroy()
    import pg2
Button(root,text='Home',command=fun1,bg='misty rose').grid(row=12,column=3,pady=20)
root.mainloop()




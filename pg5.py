from  tkinter import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(h,w))

fr=Frame(root)

bus=PhotoImage(file='.\\Bus_for_project.png')
photo=Label(fr,image=bus)
heading=Label(fr,text='Online Bus Booking System',font='Arial 14 bold',bg='light blue',fg='red')
sec_hd=Label(fr,text='Check Your Booking ',font='Arial 14 bold',bg='pale green',fg='dark green')
sec_hd.grid(row=2,pady=h//40)
photo.grid(row=0,padx=w//2.5)
heading.grid(row=1,padx=w//2.5,pady=h//40)

fr.grid(row=0,column=1,pady=h//40)

f=Frame(root)

def cmd():
   frame=LabelFrame(root)
   Label(frame,text='Passengers :Anugya\t   Gender :F',font='bold').grid(row=0,column=0)
   Label(frame,text='No of seats :2 \t      Phone No:7080129266',font='bold').grid(row=1,column=0)
   Label(frame,text='Age :18\t              Fare Rs :2000  ',font='bold').grid(row=2,column=0)
   Label(frame,text='Booking Ref :8 \t           Bus Detail:Ashoka',font='bold').grid(row=3,column=0)
   Label(frame,text='Travel On :16/11/22\t        Booked On :29/11/22 ',font='bold').grid(row=4,column=0)
   Label(frame,text='Boarding Point  :Guna ',font='bold').grid(row=5,column=0)
   frame.grid(row=2,column=1,pady=h//40)
   
Label(f,text='Enter your mobile number : ',font='Arial 14 bold').grid(row=0,column=0)
Entry(f,width=25).grid(row=0,column=1)
Button(f,text='Check Booking',font='Arial 14 bold',command=cmd).grid(row=0,column=2,padx=30)

f.grid(row=1,column=1)





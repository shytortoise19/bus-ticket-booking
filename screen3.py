from  tkinter import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

fr=Frame(root)

bus=PhotoImage(file='Bus_for_project.png')
photo=Label(fr,image=bus)
heading=Label(fr,text='Online Bus Booking System',font='Arial 14 bold',bg='light blue',fg='red')

photo.grid(row=0,padx=w//2.5)
heading.grid(row=1,padx=w//2.5)

sec_hd=Label(fr,text='Enter Journey Details ',font='Arial 14 bold',bg='pale green',fg='dark green')
sec_hd.grid(row=2,column=0,pady=h//40)

fr.grid(row=0,column=1)

##Label(root,text='\n').grid(row=3)

def cmd():
   newfr=Frame(root)
   Label(newfr,text='Fill Passenger details to book the bus ticket',font='Arial 14 bold',bg='light blue',fg='red').grid(row=0)
   newfr.grid(row=6,column=1,padx=70,pady=h//20)
   t=Label(fr2,text='Name ')
   t.grid(row=9,column=0)
   ent1=Entry(fr2)
   ent1.grid(row=9,column=1,padx=20)

   gender=IntVar();
   gender.set('Male')
   gen=['Male','Female','Third Gender']
   Label(fr2,text='Gender').grid(row=9,column=2)
   gen=OptionMenu(fr2,gender,*(gen)).grid(row=9,column=3,padx=20)

   t=Label(fr2,text='No. of seats ')
   t.grid(row=9,column=4)
   ent1=Entry(fr2,width=5)
   ent1.grid(row=9,column=5,padx=20)
   
   t=Label(fr2,text='Mobile No ')
   t.grid(row=9,column=6)
   ent1=Entry(fr2)
   ent1.grid(row=9,column=7,padx=20)
   
   t=Label(fr2,text='Age ')
   t.grid(row=9,column=8)
   ent1=Entry(fr2,width=5)
   ent1.grid(row=9,column=9,padx=20)

   Button(fr2,text='Book Seat',bg='pale green').grid(row=9,column=10,padx=20)

def but():
   Label (fram,text='Select Bus',fg='green').grid(row=5,column=0,padx=50)
   Label (fram,text='Operator',fg='green').grid(row=5,column=1,padx=50)
   Label (fram,text='Bus Type',fg='green').grid(row=5,column=2,padx=50)
   Label (fram,text='Availability',fg='green').grid(row=5,column=3,padx=50)
   Label (fram,text='Fare',fg='green').grid(row=5,column=4,padx=50)
   Label(fram,text='\n').grid(row=6)
   Button(fram,text='Bus 1',bg='light blue').grid(row=7,column=0)
   Label (fram,text='Kamla',fg='blue').grid(row=7,column=1)
   Label (fram,text='AC 2x2',fg='blue').grid(row=7,column=2)
   Label (fram,text='25/30',fg='blue').grid(row=7,column=3)
   Label (fram,text='1000',fg='blue').grid(row=7,column=4)
   
   Button(fram,text='Proceed to Book',bg='pale green',command=cmd).grid(row=7,column=5,padx=70)


fra=Frame(root)

t=Label(fra,text='To  ')
t.grid(row=4,column=0)
ent1=Entry(fra)
ent1.grid(row=4,column=1)

t=Label(fra,text='  From  ')
t.grid(row=4,column=2)

ent2=Entry(fra)
ent2.grid(row=4,column=3)

t=Label(fra,text='  Journey Date  ')
t.grid(row=4,column=4)

ent2=Entry(fra)
ent2.grid(row=4,column=5)

but=Button(fra,text='Show Bus',bg='medium sea green',command=but)
but.grid(row=4,column=6,padx=20)

home=PhotoImage(file='home.png')
Label(fra,image=home).grid(row=4,column=7)


fra.grid(row=4,column=1,pady=h//40)
fram=Frame(root)
fram.grid(row=5,column=1)
fr2=Frame(root)
fr2.grid(row=7,column=1,pady=h//50)












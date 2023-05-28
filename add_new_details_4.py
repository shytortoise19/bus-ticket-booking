from tkinter import*
root= Tk()
h,w,= root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

img =PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=img).grid(row=0,column=0,padx=w//3+100,sticky='n',columnspan=10)
Label(root,text="Online Bus Booking System" ,font="Arial 30 bold" ,bg="steelblue1",fg="IndianRed1" ).grid(row=1,column=0,columnspan=10,pady=20)
Label(root,text = "Add New Details to DataBase", font = "arial 20 bold", fg ='green').grid(row = 2, column = 0, columnspan=10,pady = 20)
def addbus():
    root.destroy()
    import Add_bus_details_5

def addoperator():
    root.destroy()
    import Add_operator_6
def addroute():
    root.destroy()
    import Add_Route_7
def addrun():
    root.destroy()
    import Add_Run_8
Button(root, text= 'New Operator',font='20',fg ='black' ,bg= 'light green',command=addoperator).grid(row= 3 ,column = 0,padx=w//13)
Button(root, text= 'New Bus',font='20',fg ='black' ,bg= 'orange red',command=addbus).grid(row= 3 ,column = 2,padx=w//11)
Button(root, text= 'New Route',font='20',fg ='black' ,bg= 'steelBlue1',command=addroute).grid(row= 3 ,column =4,padx=w//11)
Button(root, text= 'New Run',font='20',fg ='black' ,bg= 'rosy brown',command=addrun).grid(row= 3 ,column = 6,padx=w//11)

root.mainloop()

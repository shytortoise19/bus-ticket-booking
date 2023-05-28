from tkinter import*
root= Tk()
h,w,= root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

img =PhotoImage(file=".\\Bus_for_project.png")
Label(root,image = img).grid(row = 0 , column = 6)

Label(root,text = "Online Bus Booking System", font = "arial 18 bold",bg = 'sky blue', fg ='Red').grid(row = 1, column = 6, pady = 20)

Label(root,text = "Add Bus Operator Details", font = "arial 14 bold",bg = 'light green', fg ='green').grid(row = 2, column = 6, pady = 20)

Label(root,text = "Operator").grid(row=3 , column = 2)
Text(root, width = 20 , height = 1).grid(row = 3 , column =3)

Label(root,text = "Name").grid(row=3 , column = 4)
Text(root, width = 20 , height = 1).grid(row = 3 , column =5)

Label(root,text = "Address").grid(row=3 , column = 6)
Text(root, width = 20 , height = 1).grid(row = 3 , column =7)

Label(root,text = "Phone").grid(row=3 , column = 8)
Text(root, width = 20 , height = 1).grid(row = 3 , column =9)

Label(root,text = "Email").grid(row=3 , column = 10)
Text(root, width = 20 , height = 1).grid(row = 3 , column =11)

Button(root, text= 'Add',fg ='black' ,bg= 'light green').grid(row= 3 ,column = 13)
Button(root, text= 'Edit',fg ='black' ,bg= 'light green').grid(row= 3 ,column = 15)

Button(root,fg ='black' ,bg= 'light green',image = img1).grid(row= 3 ,column = 10, padx = 10)
root.mainloop

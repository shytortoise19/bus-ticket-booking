from tkinter import*
root= Tk()
h,w,= root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

Label(root, text = 'Fill Passenger Details to book bus ticket', font = 'Arial 18 bold ' ,fg = 'red' , bg = 'light blue').grid(row = 0, column = 6 ,columnspan= 10)

Label(root,text = "Name").grid(row= 1, column= 3, pady = 100)
Text(root, width = 10, height = 1).grid(row = 1, column = 4, padx = 50)

Label(root,text = "Gender").grid(row= 1, column= 5)
gender_type = StringVar()
opt = ["Male", "Female"]
d_menu = OptionMenu(root, gender_type,*opt).grid(row = 1 ,column = 6, padx = 50)



Label(root,text = "No of Seats").grid(row= 1, column= 7)
Text(root, width = 10, height = 1).grid(row = 1, column = 8 ,padx =50)

Label(root,text = "Mobile No").grid(row= 1, column= 9)
Text(root, width = 10, height = 1).grid(row = 1, column = 10, padx = 50)



Label(root,text = "Age").grid(row= 1, column= 11)
Text(root, width = 10, height = 1).grid(row = 1, column = 12)
Button(root,text='Book seat').grid(row=1,column=13)
    
root.mainloop()





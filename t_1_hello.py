from tkinter import *

root=Tk()
# myLabel=Label(root,text="Lorum Ipsum").grid(column=0,row=0) this works too bcoz python is an oops language

myLabel=Label(root,text="Lorum Ipsum")
myLabel.grid(column=0, row=0)

myLabel2=Label(root,text="Hi I am just a random Label")
myLabel2.grid(column=0,row=1)
mybutton=Button(root,text="click me",padx=3,pady=3)
mybutton.grid(column=0,row=2)
root.mainloop()

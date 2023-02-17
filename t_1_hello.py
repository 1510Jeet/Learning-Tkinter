from tkinter import *

root=Tk()
# myLabel=Label(root,text="Lorum Ipsum").grid(column=0,row=0) this works too bcoz python is an oops language
e=Entry(root,fg="yellow",bg="red")
e.grid()
e.insert(10,"Enter Your Name:")

def myClick ():
    hello="ha " + e.get() +" Clicked Me!"
    myLabel3=Label(root,text=hello)
    myLabel3.grid()

myLabel=Label(root,text="Lorum Ipsum")
myLabel.grid(column=0, row=1)

myLabel2=Label(root,text="Hi I am just a random Label")
myLabel2.grid(column=0,row=2)
mybutton=Button(root,text="Enter Your Name, Or be prepared for Apocalypse",padx=3,pady=3,command=myClick,fg='white',bg='black')
mybutton.grid(column=0,row=3)
# if not using grid use .pack method to push widgets on the screen

root.mainloop()

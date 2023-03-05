from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title('Learning Tkinter')
root.iconbitmap(r"C:\Users\Jeet\Downloads\python_icon_245273.ico") # for adding icon

my_img=ImageTk.PhotoImage(Image.open('mz.png'))
my_label=Label(image=my_img)
my_label.grid()


button_quit=Button(root,text="Exit Program", command=root.quit)
button_quit.grid()



root.mainloop() 
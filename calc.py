from tkinter import *
from tkinter import ttk


root=Tk()
value=StringVar()

root.title("simple calc")
num=Entry(root,textvariable=value)
num.grid()


#steps:
# make textvariables
# S2 make entry 
# step 3 make a return bind
ans=0.000000
# make functions
def Calculate():
    global ans
    ans=0.0
    s=value.get()
    i=0
    x=""
    symbol='+'
    if (s[0]=='-'):
        symbol='-'
        i+=1
    while(i<len(s)):
        
        if ((s[i]>='0' and s[i]<='9') or s[i]=='.' ):
            x+=s[i]
        elif (s[i]=='+' or s[i]=='i'):
            if (symbol=='+'):
                ans=ans+float(x)
            elif (symbol=='-'):
                ans=ans-float(x)   
            x=""    
            if (s[i]=='+'):
                symbol='+'
            elif(s[i]=='-'):
                symbol='-'         
        i+=1
        if (i==len(s)):
            if (symbol=='+'):
                ans=ans+float(x)
            elif (symbol=='-'):
                ans=ans-float(x)   
    value.set(ans)
    return

def add(x):
    value.set(value.get()+x)
    print(value.get())
    return


plus=Button(root,text='+',command=lambda :add('+'))
plus.grid()

plus=Button(root,text='-',command=lambda : add('-'))
plus.grid()

plus=Button(root,text='=',command=Calculate)
plus.grid()


root.mainloop()
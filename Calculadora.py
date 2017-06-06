from tkinter import *

def suma():
    total = int(a.get()) + int(b.get())
    print(total)

lastpos=0
def ingreso():
    a.insert(i,i)
    
tk=Tk()
valor1 = DoubleVar()
valor2 = DoubleVar()
a = Entry(tk,textvariable = valor1)
b = Entry(tk, textvariable = valor2)
Label(tk,text="Ingrese la cantidad:").pack()
a.pack()
a.delete(0,3)
#a.insert(0,"g")
#Label(tk,text="Ingrese la segunda cantidad:").pack()
#b.pack()
for i in range(0,10):
    j=Button(tk,text=i,relief="ridge",bd=5,activebackground="blue"
             ,cursor="hand2",command=ingreso())#.grid(row=3,column=i,sticky=W,pady=(i+3))
    #a.insert(i,i)
    j.pack(side=LEFT)
    if i==9:
        j=Button(tk,text="=",relief="ridge",bd=5,cursor="hand2")
        j.pack(side=LEFT)
Button(tk,text="A",relief="ridge",bd=5,cursor="hand2").pack(side=RIGHT)
                                                   

   
          


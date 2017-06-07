from tkinter import *
master = Tk()
what_ever_you_do= "Whatever you do will be insignificant, but it is very important that you do it. \n(Mahatma Gandhi)"
msg = Message(master, text = what_ever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack()
mainloop() 

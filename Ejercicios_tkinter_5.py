from tkinter import *
root=Tk()
v=IntVar()
v.set(1) #Inicializando la opción

languages = [
    ("Python",1),
    ("Perl",2),
    ("Java",3),
    ("C++",4),
    ("C#",5)
]
def MostrarOpcion():
    print (v.get())

Label(root,text="""Elige tu lenguaje de programación favorito:""",
      justify=LEFT,
      padx=20).pack()

for txt, val in languages:
    Radiobutton(root,
                text=txt,
                padx=30,
                variable=v,
                command=MostrarOpcion,
                value=val).pack(anchor=W)
mainloop()

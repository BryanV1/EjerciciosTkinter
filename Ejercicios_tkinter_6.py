from tkinter import *
root=Tk()
v=IntVar()
v.set(1)

languages=[
    ("Python",1),
    ("Perl",2),
    ("Java",3),
    ("C++",4),
    ("C#",5)
]

def mostrar():
    print(v.get())

Label(root, text="""Elige un lenguaje de programación""",
      justify=LEFT,
      padx=0).pack()

for txt, val in languages:
    Radiobutton(root,
                text=txt,
                indicatoron=0,
                width=20,
                padx=20,
                variable=v,
                command=mostrar(),
                value=val).pack(anchor=W)
mainloop()

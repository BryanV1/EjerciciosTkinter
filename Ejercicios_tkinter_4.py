from tkinter import *
root=Tk()
v=IntVar
Label(root,text="""Choose a programming language:""",justify=LEFT,padx=20).pack()
Radiobutton(root,text="Python",padx=20,variable=v, value=1).pack(anchor=W)
Radiobutton(root,text="Perl",padx=20,variable=v,value=2).pack(anchor=W)
Radiobutton(root,text="Java",padx=20,variable=v,value=3).pack(anchor=W)
Radiobutton(root,text="PHP",padx=20,variable=v,value=5).pack(anchor=W)
Radiobutton(root,text="C++",padx=30,variable=v,value=4).pack(anchor=W)
Radiobutton(root,text="C#",padx=10,variable=v,value=6).pack(anchor=W)
mainloop()

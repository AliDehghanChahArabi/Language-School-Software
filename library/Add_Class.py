from tkinter import *
import tkMessageBox


def show():

    def show_entry_fields():
        tkMessageBox.showinfo(
            "R.C.S.C - I.M.S. S.A. ", "Registration Confirmation students in class : \n \n %s in the class %s added." % (e1.get(), e2.get()))

    add_class = Tk()

    Label(add_class, text="Student ID").grid(row=0)
    e1 = Entry(add_class)
    e1.grid(row=0, column=1)

    Label(add_class, text="Class ID").grid(row=1)
    e2 = Entry(add_class)
    e2.grid(row=1, column=1)

    Button(add_class, text='Quit', command=add_class.quit).grid(
        row=3, column=0, sticky=W, pady=4)
    Button(add_class, text='Save', command=show_entry_fields).grid(
        row=3, column=1, sticky=W, pady=4)

    add_class.mainloop()


show()

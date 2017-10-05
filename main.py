from tkinter import *


def add_ss():
    from library import Sing


def search_ss():
    from library import Search


def add_class_ss():
    from library import Add_Class


def edit_ss():
    from library import Edit


while 1:

    home = Tk()

    home.title("Institute Management Software Shookooh Andihe")

    labelframe = LabelFrame(home, text="Tools")
    labelframe.pack(fill="both", expand="yes")
# logo
    logo = PhotoImage(file="logo.png")
    w1 = Label(labelframe, image=logo).pack(side="right", padx=10)

    labelframe_Students = LabelFrame(labelframe, text="Students")
    labelframe_Students.pack(fill="both", expand="yes")

    labelframe_Professor = LabelFrame(labelframe, text="Professor")
    labelframe_Professor.pack(fill="both", expand="yes")

    labelframe_Classes = LabelFrame(labelframe, text="Classes")
    labelframe_Classes.pack(fill="both", expand="yes")

    labelframe_User = LabelFrame(labelframe, text="User")
    labelframe_User.pack(fill="both", expand="yes")


# Student
    Sing_s = Button(labelframe_Students, text="Sing Student", height=2, width=10,
                    activebackground="blue", command=add_ss).pack(side="left", anchor="ne")
    Search_s = Button(labelframe_Students, text="Search Student", height=2, width=10,
                      activebackground="blue", command=search_ss).pack(side="left", anchor="ne")
    Edit_s = Button(labelframe_Students, text="Edit Student", height=2, width=10,
                    activebackground="blue", command=edit_ss).pack(side="left", anchor="ne")
    Remove_s = Button(labelframe_Students, text="Remove Student", height=2, width=10,
                      activebackground="blue", command="add").pack(side="left", anchor="ne")
    Add_s = Button(labelframe_Students, text="Add Class Student", height=2, width=12,
                   activebackground="blue", command=add_class_ss).pack(side="left", anchor="ne")

# Professor
    Sing_p = Button(labelframe_Professor, text="Sing Professor", height=2, width=10,
                    activebackground="blue", command="add").pack(side="left", anchor="ne")
    Search_p = Button(labelframe_Professor, text="Search Professor", height=2, width=10,
                      activebackground="blue", command="search").pack(side="left", anchor="ne")
    Edit_p = Button(labelframe_Professor, text="Edit Professor", height=2, width=10,
                    activebackground="blue", command="add").pack(side="left", anchor="ne")
    Remove_p = Button(labelframe_Professor, text="Remove Professor", height=2, width=10,
                      activebackground="blue", command="add").pack(side="left", anchor="ne")
    Add_p = Button(labelframe_Professor, text="Add Class Professor", height=2, width=12,
                   activebackground="blue", command="add_class").pack(side="left", anchor="ne")

# Classes
    Sing_c = Button(labelframe_Classes, text="Add class", height=2, width=10,
                    activebackground="blue", command="add").pack(side="left", anchor="ne")
    Search_c = Button(labelframe_Classes, text="Edit class", height=2, width=10,
                      activebackground="blue", command="search").pack(side="left", anchor="ne")
    Edit_c = Button(labelframe_Classes, text="Show class", height=2, width=10,
                    activebackground="blue", command="add").pack(side="left", anchor="ne")
    Remove_c = Button(labelframe_Classes, text="Remove class", height=2, width=10,
                      activebackground="blue", command="add").pack(side="left", anchor="ne")

    mainloop()
    break

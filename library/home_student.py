from tkinter import *
import Search
import Edit
import Sing
import Add_Class


def show():

    def search():
        pass
        Search.show()

    def edit():
        pass
        Edit.show()

    def sing():
        pass
        Sing.show()

    def add_class():
        pass
        Add_Class.show()

    home_student = Tk()

# titel
    home_student.title("Students - I.M.S. S.A.")

    # lable from
    labelframe = LabelFrame(home_student, text="Tools")
    labelframe.pack(fill="both", expand="yes")

# button
    Student = Button(labelframe, text="Search", height=10, width=10,
                     activebackground="blue", command=search)
    Professor = Button(labelframe, text="Edit", height=10, width=10,
                       activebackground="red", command=edit)
    classes = Button(labelframe, text="Sing", height=10, width=10,
                     activebackground="blue", command=sing)
    User = Button(labelframe, text="Add Class", height=10, width=10,
                  activebackground="red", command=add_class)

    Student.pack(side="left", anchor="ne")
    Professor.pack(side="left", anchor="ne")
    classes.pack(side="left", anchor="ne")
    User.pack(side="left", anchor="ne")
    home_student.mainloop()


if __name__ == "__main__":
    show()

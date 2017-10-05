from tkinter import *
import tkMessageBox
import studenttools


def show():

    def ok_data():
        pass
        var_1 = var1.get()
        var_2 = var2.get()
        if var_1 == 1:
            sex = "male"
        if var_2 == 1:
            sex = "female"
        if var_1 == var_2:
            sex = "ERROR !!"

        var_3 = var3.get()
        var_4 = var4.get()
        if var_3 == 1:
            class_fees = "OK"
        else:
            class_fees = "NO"

        if var_4 == 1:
            mony_book = "OK"
        else:
            mony_book = "NO"

        studenttools.sing(First.get(), Last.get(), Father.get(), Data.get(), Level.get(
        ), Code.get(), Mobile.get(), Phone.get(), Address.get(), sex, class_fees, mony_book)

        tkMessageBox.showinfo(
            "Confirmation Form", "ID : %s \n Class Fees : %s | Mony Bokk : %s \n Level : %s \n Sex : %s \n First Name : %s \n Last Name  : %s \n Father's Name : %s \n Data of Birth : %s \n National Code : %s \n Mobile Number : %s \n Phone Number  : %s \n Address : %s" % (Code.get(), class_fees, mony_book, Level.get(), sex, First.get(), Last.get(), Father.get(), Data.get(), Code.get(), Mobile.get(), Phone.get(), Address.get()))

    add_class = Tk()
    # titel
    add_class.title("Students Sing - I.M.S. S.A.")

    Label(add_class, text="First Name").grid(row=0, column=0)
    First = Entry(add_class)
    First.grid(row=0, column=1)

    Label(add_class, text="Last Name").grid(row=0, column=2)
    Last = Entry(add_class)
    Last.grid(row=0, column=3)

    Label(add_class, text="Father's name").grid(row=1, column=0)
    Father = Entry(add_class)
    Father.grid(row=1, column=1)

    Label(add_class, text="Date of birth").grid(row=1, column=2)
    Data = Entry(add_class)
    Data.grid(row=1, column=3)

    Label(add_class, text="Level").grid(row=2, column=0)
    Level = Entry(add_class)
    Level.grid(row=2, column=1)

    Label(add_class, text="National Code").grid(row=2, column=2)
    Code = Entry(add_class)
    Code.grid(row=2, column=3)

    Label(add_class, text="Mobile Number").grid(row=3, column=0)
    Mobile = Entry(add_class)
    Mobile.grid(row=3, column=1)

    Label(add_class, text="Phone Number").grid(row=3, column=2)
    Phone = Entry(add_class)
    Phone.grid(row=3, column=3)

    Label(add_class, text="Address").grid(row=4, column=0)
    Address = Entry(add_class)
    Address.grid(row=4, column=1)

    Label(add_class, text="Your sex:").grid(row=5, column=0, sticky=W)
    var1 = IntVar()
    Checkbutton(add_class, text="male", variable=var1).grid(
        row=5, column=1, sticky=W)
    var2 = IntVar()
    Checkbutton(add_class, text="female", variable=var2).grid(
        row=5, column=2, sticky=W)

    Label(add_class, text="Payments situation:").grid(
        row=6, column=0, sticky=W)
    var3 = IntVar()
    Checkbutton(add_class, text="Class fees", variable=var3).grid(
        row=6, column=1, sticky=W)
    var4 = IntVar()
    Checkbutton(add_class, text="Money Book", variable=var4).grid(
        row=6, column=2, sticky=W)

    # button
    Button(add_class, text='Quit', command=add_class.quit).grid(
        row=10, column=0, sticky=W, pady=4)
    Button(add_class, text='Save and Show', command=ok_data).grid(
        row=10, column=1, sticky=W, pady=4)

    mainloop()


show()

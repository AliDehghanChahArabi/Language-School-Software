from tkinter import *
#import tkMessageBox
import studenttools


def show():

    def action():
        data = studenttools.search(ID.get())

        while data[0] == "OK":

            tkMessageBox.showinfo("Search Results - I.M.S. S.A. ", data)
            ID.delete(0, END)
            data = []

        while data[0] == False:

            tkMessageBox.showinfo(
                "Search Results - I.M.S. S.A. ", "Not Available.")
            ID.delete(0, END)
            data = []

    search = Tk()

# titel
    search.title("Students Search - I.M.S. S.A.")

    Label(search, text="Student ID").grid(row=0, column=0)
    ID = Entry(search)
    ID.grid(row=0, column=1)


# button
    Button(search, text='Quit', command=search.quit).grid(
        row=1, column=0, sticky=W, pady=4)
    Button(search, text='Search and Show', command=action).grid(
        row=1, column=1, sticky=W, pady=4)
    mainloop()


show()

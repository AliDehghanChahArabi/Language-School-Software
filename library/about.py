from tkinter import *


def show():

    about = Tk()

# titel
    about.title("About - I.M.S. S.A.")

    explanation = """Hello
        This is a management software for language institute shookooh andishe.
        Designer and Producer: Ali Dehghan Chaharabi
        Licensed: iPMM Co.

        Contact Us
        Phone:    +98912 088 3990
        Email:     info@alidehqan.com
        website:  http://alidehqan.com"""
    l_about = Label(about, justify=LEFT, padx=10,
                    text=explanation).pack(side="left")
    about.mainloop()
if __name__ == "__main__":
    show()

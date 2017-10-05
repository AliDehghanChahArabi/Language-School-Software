from tkinter import *


def show():

    Help = Tk()

# titel
    Help.title("Help - Institute Management Software shookooh Android")

    explanation = """
    Help :
    """
    l_about = Label(Help, justify=LEFT, padx=10,
                    text=explanation).pack(side="left")
    Help.mainloop()
if __name__ == "__main__":
    show()

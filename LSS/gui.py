try:
	from tkinter import *
	import databaselib
except:
	from Tkinter import *
	import databaselib


class Gui():
	def __init__(self):
		self.win = Tk()
		
		self.win.title("LLC - V 1.0.0.01")
		
		self.win.minsize(width = 100, height = 200)
		self.win.resizable(width = False, height = False)
		
		self.icon_and_logo = PhotoImage(file = 'logo.gif')
		self.win.tk.call ("wm", "iconphoto", self.win._w, self.icon_and_logo)

		self.titleFrame = Frame(self.win, width = 200, height = 260, relief = SUNKEN)
		self.titleFrame.pack(side = TOP)
		self.leftFrame = LabelFrame(self.win, width = 200, height = 260, relief = SUNKEN)
		self.leftFrame.pack(side = LEFT)
		self.centerFrame = LabelFrame(self.win, width = 20, height = 20, relief = SUNKEN)
		self.centerFrame.pack(side = LEFT)
		self.rightFrame = LabelFrame(self.win, width = 200, height = 260, relief = SUNKEN)
		self.rightFrame.pack(side = RIGHT)
		
		self.studentlabel = LabelFrame(self.leftFrame, text = "Students")
		self.studentlabel.pack(side = 'left', fill = 'both', expand = 'yes')
		self.teacherlabel = LabelFrame(self.leftFrame, text = "Teachers")
		self.teacherlabel.pack(side = 'left', fill = 'both', expand = 'yes')
		self.userlabel = LabelFrame(self.rightFrame, text = "User")
		self.userlabel.pack(side = 'right', expand = 'yes')
		self.classlabel = LabelFrame(self.rightFrame, text = "Class")
		self.classlabel.pack(side = 'right', expand = 'yes')
		
		Label(self.titleFrame, font = ('Arial', 20, 'bold'), text = "Kish International Campus").pack()
		Label(self.centerFrame, image = self.icon_and_logo).pack()

		self.btn_height = 2

		Button(self.studentlabel, text = 'add student', height = self.btn_height, command = self.add_student).pack(fill = X)
		Button(self.studentlabel, text = 'search student', height = self.btn_height, command = self.search_student).pack(fill = X)
		Button(self.studentlabel, text = 'edit student', height = self.btn_height, command = self.edit_student).pack(fill = X)
		Button(self.studentlabel, text = 'delet student', height = self.btn_height, command = self.delet_student).pack(fill = X)

		Button(self.teacherlabel, text = 'add teacher', height = self.btn_height).pack(fill = X)
		Button(self.teacherlabel, text = 'search teacher', height = self.btn_height).pack(fill = X)
		Button(self.teacherlabel, text = 'edit teacher', height = self.btn_height).pack(fill = X)
		Button(self.teacherlabel, text = 'delet teacher', height = self.btn_height).pack(fill = X)

		Button(self.classlabel, text = 'add term', height = self.btn_height).pack(fill = X)
		Button(self.classlabel, text = 'add class', height = self.btn_height).pack(fill = X)
		Button(self.classlabel, text = 'add stuedent on class', height = self.btn_height).pack(fill = X)
		Button(self.classlabel, text = 'add teacher on class', height = self.btn_height).pack(fill = X)

		Button(self.userlabel, text = 'setting', height = self.btn_height).pack(fill = X)
		Button(self.userlabel, text = 'edit user', height = self.btn_height).pack(fill = X)
		Button(self.userlabel, text = 'password', height = self.btn_height).pack(fill = X)
		Button(self.userlabel, text = 'close', height = self.btn_height).pack(fill = X)

		self.win.mainloop()

	def add_student(self):

		def action_add_student():
			student_db = databaselib.DataBase()
			print(student_db.add_student(self.F_NAME.get(), self.L_NAME.get(), self.NNO.get(), self.B_DATE.get(), self.FATHER_NAME.get(), self.TEL.get(), self.CELL.get(), self.ADDRESS.get(), self.P_BOX.get()))

		win_student = Tk()
		win_student.title("Add Student Form")

		self.label_studebt_left = LabelFrame(win_student, width = 200, relief = SUNKEN)
		self.label_studebt_left.pack(side = LEFT)

		self.personal_data = LabelFrame(self.label_studebt_left, text = "Personal Data")
		self.personal_data.pack(side = 'left', fill = 'both', expand = 'yes')

		self.personal_data_titel = LabelFrame(self.label_studebt_left, text = "")
		self.personal_data_titel.pack(side = 'left', fill = 'both', expand = 'yes')

		self.personal_data_entry = LabelFrame(self.label_studebt_left, text = "")
		self.personal_data_entry.pack(side = 'right', fill = 'both', expand = 'yes')

		self.ipady = 4

		Label(self.personal_data_titel, text = "First Name:").pack(fill = X)
		self.F_NAME = Entry(self.personal_data_entry)
		self.F_NAME.pack(fill = X, ipady = self.ipady)
		
		Label(self.personal_data_titel, text = "\nLast Name:").pack(fill = X)
		self.L_NAME = Entry(self.personal_data_entry)
		self.L_NAME.pack(fill = X, ipady = self.ipady)
		
		Label(self.personal_data_titel, text = "\nNational ID:").pack(fill = X)
		self.NNO = Entry(self.personal_data_entry)
		self.NNO.pack(fill = X, ipady = self.ipady)
		
		Label(self.personal_data_titel, text = "\nBirth Date:").pack(fill = X)
		self.B_DATE = Entry(self.personal_data_entry)
		self.B_DATE.pack(fill = X, ipady = self.ipady)
		
		Label(self.personal_data_titel, text = "\nFather Name:").pack(fill = X)
		self.FATHER_NAME = Entry(self.personal_data_entry)
		self.FATHER_NAME.pack(fill = X, ipady = self.ipady)
		
		Label(self.personal_data_titel, text = "\nTel.:").pack(fill = X)
		self.TEL = Entry(self.personal_data_entry)
		self.TEL.pack(fill = X, ipady = self.ipady)
		
		Label(self.personal_data_titel, text = "\nCell:").pack(fill = X)
		self.CELL = Entry(self.personal_data_entry)
		self.CELL.pack(fill = X, ipady = self.ipady)
		
		Label(self.personal_data_titel, text = "\nAddress:").pack(fill = X)
		self.ADDRESS = Entry(self.personal_data_entry)
		self.ADDRESS.pack(fill = X, ipady = self.ipady)
		
		Label(self.personal_data_titel, text = "\nP. Box:").pack(fill = X)
		self.P_BOX = Entry(self.personal_data_entry)
		self.P_BOX.pack(fill = X, ipady = self.ipady)

		self.save_btn = Button(self.personal_data, text = "Save Student Data", activebackground = "blue", command = action_add_student)
		self.save_btn.pack(fill = X)

	def search_student(self):

		def action_search_student():
			search_student = databaselib.DataBase()
			self.data = search_student.get_student(self.NNO.get())
			
			win_student = Tk()
			win_student.title("Search Student Form")

			self.label_search = LabelFrame(win_student, width = 200, relief = SUNKEN)
			self.label_search.pack(side = LEFT)

			self.label_result = LabelFrame(self.label_search, text = "Search from Student Database")
			self.label_result.pack(side = 'left', fill = 'both', expand = 'yes')

			self.text = "\nFirst Name: %s\nLast Name: %s\n\nNational ID: %s\nFather Name: %s\nDate Birth:  %s\n\nTel: %s\nCell: %s\nP. Box: %s\nAddress: %s" % (self.data[0][1], self.data[0][2], self.data[0][3], self.data[0][5], self.data[0][4], self.data[0][6], self.data[0][7], self.data[0][9], self.data[0][8])
			self.result = Label(self.label_result, text = self.text)
			self.result.pack(side = 'left', fill = X)
			
			mainloop()

		win_student = Tk()
		win_student.title("Search Student Form")

		self.label_studebt_left = LabelFrame(win_student, width = 200, relief = SUNKEN)
		self.label_studebt_left.pack(side = LEFT)

		self.personal_data = LabelFrame(self.label_studebt_left, text = "Search from Student Database")
		self.personal_data.pack(side = 'left', fill = 'both', expand = 'yes')

		self.personal_data_titel = LabelFrame(self.label_studebt_left, text = "")
		self.personal_data_titel.pack(side = 'left', fill = 'both', expand = 'yes')

		self.personal_data_entry = LabelFrame(self.label_studebt_left, text = "")
		self.personal_data_entry.pack(side = 'right', fill = 'both', expand = 'yes')

		self.ipady = 4

		Label(self.personal_data_titel, text = "National ID No.:").pack(fill = X)
		self.NNO = Entry(self.personal_data_entry)
		self.NNO.pack(fill = X, ipady = self.ipady)

		self.save_btn = Button(self.personal_data, text = "Search", activebackground = "blue", command = action_search_student)
		self.save_btn.pack(fill = X)

		win_student.mainloop()

	def edit_student(self):
		win_student = Tk()
		win_student.title("Edit Student Form")
		win_student.mainloop()

	def delet_student(self):
		win_student = Tk()
		win_student.title("Delet Student Form")
		win_student.mainloop()

if __name__ == '__main__':
	ui = Gui()

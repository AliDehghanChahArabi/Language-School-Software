try:
	import glob, os
	import time
	import sqlite3
except:
	import glob, os
	import time
	import sqlite3




class DataBase():
	def __init__ (self, db_name = "LLS.db"):
		self.db_name = db_name

	def set_new_data(self):
		try:
			self.make_student_db()
			self.make_teacher_db()
			self.make_term_list()
			self.make_class_list()
		except:
			local_time = time.asctime(time.localtime(time.time()))
			local_time = "_".join(local_time.split(" "))
			local_time = "_".join(local_time.split(":"))
			self.db_name = "LLS_%s.db"%(local_time)
			print (self.db_name)
			self.make_student_db()
			self.make_teacher_db()
			self.make_term_list()
			self.make_class_list()

	def make_student_db(self):
		con = sqlite3.connect(self.db_name)
		act = con.cursor()
		SSC = """
		CREATE TABLE student (
		ID INTEGER PRIMARY KEY,
		F_NAME VARCHAR(50),
		L_NAME VARCHAR(50),
		NNO VARCHAR(50),
		B_DATE VARCHAR(50),
		FATHER_NAME VARCHAR(50),
		TEL VARCHAR(50),
		CELL VARCHAR(50),
		ADDRESS VARCHAR(50),
		P_BOX VARCHAR(50));"""
		act.execute(SSC)
		con.commit()
		con.close()

	def make_teacher_db(self):
		con = sqlite3.connect(self.db_name)
		act = con.cursor()
		TSC = """
		CREATE TABLE teacher (
		ID INTEGER PRIMARY KEY,
		F_NAME VARCHAR(50),
		L_NAME VARCHAR(50),
		NNO VARCHAR(50),
		B_DATE VARCHAR(50),
		FATHER_NAME VARCHAR(50),
		TEL VARCHAR(50),
		CELL VARCHAR(50),
		ADDRESS VARCHAR(50),
		EDUCATION VARCHAR(50),
		C_N VARCHAR(50),
		P_BOX VARCHAR (50),
		LEVEL VARCHAR(50),
		COMMENT VARCHAR(100));"""
		act.execute(TSC)
		con.commit()
		con.close()

	def make_term_list(self):
		con = sqlite3.connect(self.db_name)
		act = con.cursor()
		CSC = """
		CREATE TABLE term (
		ID INTEGER PRIMARY KEY,
		NAME VARCHAR(50),
		CODE VARCHAR(50),
		VALUE VARCHAR(50),
		S_DATA VARCHAR(50),
		E_DATA VARCHAR(50),
		TERM VARCHAR(50));"""
		act.execute(CSC) 
		con.commit()
		con.close()

	def make_class_list(self):
		con = sqlite3.connect(self.db_name)
		act = con.cursor()
		CSC = """
		CREATE TABLE class (
		ID INTEGER PRIMARY KEY,
		NAME VARCHAR(50),
		TERM_CODE VARCHAR(50),
		STUDENT_CODE VARCHAR(50),
		TEACHER_CODE VARCHAR(50));"""
		act.execute(CSC) 
		con.commit()
		con.close()

	def add_student(self, F_NAME, L_NAME, NNO, B_DATE, FATHER_NAME, TEL, CELL, ADDRESS, P_BOX):
		try:
			con = sqlite3.connect(self.db_name)
			act = con.cursor()
			SSC = "INSERT INTO student (ID, F_NAME, L_NAME, NNO, B_DATE, FATHER_NAME, TEL, CELL, ADDRESS, P_BOX) VALUES (NULL, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (F_NAME, L_NAME, NNO, B_DATE, FATHER_NAME, TEL, CELL, ADDRESS, P_BOX)
			act.execute(SSC)
			con.commit()
			con.close()
			return "Saved"
		except:
			return "E101 - DB"
			print ("E101 - DB")

	def add_teacher(self, F_NAME, L_NAME, NNO, B_DATE, FATHER_NAME, TEL, CELL, ADDRESS, EDUCATION, C_N, P_BOX, LEVEL, COMMENT):
		try:
			for file in glob.glob("*.db"):
				db_name = file
			con = sqlite3.connect(db_name)
			act = con.cursor()
			SSC = "INSERT INTO teacher (ID, F_NAME, L_NAME, NNO, B_DATE, FATHER_NAME, TEL, CELL, ADDRESS, EDUCATION, C_N, P_BOX, LEVEL, COMMENT) VALUEs (NULL, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (F_NAME, L_NAME, NNO, B_DATE, FATHER_NAME, TEL, CELL, ADDRESS, EDUCATION, C_N, P_BOX, LEVEL, COMMENT)
			act.execute(SSC)
			con.commit()
			con.close()
		except:
			print ("E102 - DB")

	def add_term (self, NAME, CODE, VALUE, S_DATA, E_DATA, TERM):
		try:
			for file in glob.glob("*.db"):
				db_name = file
			con = sqlite3.connect(db_name)
			act = con.cursor()
			SSC = "INSERT INTO term (ID, NAME, CODE, VALUE, S_DATA, E_DATA, TERM) VALUES (NULL, '%s', '%s', '%s', '%s', '%s', '%s');" % (NAME, CODE, VALUE, S_DATA, E_DATA, TERM)
			act.execute(SSC)
			con.commit()
			con.close()
		except:
			print ("E103 - DB")

	def add_class(self, NAME, TERM_CODE, STUDENT_CODE, TEACHER_CODE):
		try:
			for file in glob.glob("*.db"):
				db_name = file
			con = sqlite3.connect(db_name)
			act = con.cursor()
			SSC = "INSERT INTO class (ID, NAME, TERM_CODE, STUDENT_CODE, TEACHER_CODE) VALUES (NULL, '%s', '%s', '%s', '%s');" % (NAME, TERM_CODE, STUDENT_CODE, TEACHER_CODE)
			act.execute(SSC)
			con.commit()
			con.close()
		except:
			print ("E104 - DB")

	def get_student(self, NNO):
		try:
			for file in glob.glob("*.db"):
				db_name = file
			con = sqlite3.connect(db_name)
			act = con.cursor()
			act.execute ("SELECT * FROM student WHERE NNO Like '%s'"%(NNO))
			result = act.fetchall()
			con.close()
			return result
		except:
			con.close()
			print ("E201 - DB")
			return "E201 - DB"

	def get_teacher(self, NNO):
		try:
			for file in glob.glob("*.db"):
				db_name = file
			con = sqlite3.connect(db_name)
			act = con.cursor()
			act.execute ("SELECT * FROM teacher WHERE NNO Like '%s'"%(NNO))
			result = act.fetchall()
			con.close()
			return result
		except:
			con.close()
			print ("E202 - DB")
			return "E202 - DB"

	def get_term(self, CODE):
		try:
			for file in glob.glob("*.db"):
				db_name = file
			con = sqlite3.connect(db_name)
			act = con.cursor()
			act.execute ("SELECT * FROM term WHERE CODE Like '%s'"%(CODE))
			result = act.fetchall()
			con.close()
			return result
		except:
			con.close()
			print ("E203 - DB")
			return "E203 - DB"

	def get_class(self, NAME):
		try:
			for file in glob.glob("*.db"):
				db_name = file
			con = sqlite3.connect(db_name)
			act = con.cursor()
			act.execute ("SELECT * FROM class WHERE NAME Like '%s'"%(NAME))
			result = act.fetchall()
			con.close()
			return result
		except:
			con.close()
			print ("E204 - DB")
			return "E204 - DB"



if __name__ == "__main__":
	print ("lib its ok")
	#act = DataBase()
	#act.set_new_data()
	#act.make_term_list()
	#act.make_class_list()
	#act.add_student("Ali", "DehghanChaharabi", "3520345171", "27 Dec. 1980", "Majid", "02188888888", "09120000000", "Tehran", "11111111")
	#act.add_teacher("Sara", "Saraei", "1234567890", "20 Mar. 1985", "Milad", "02111111111", "09122222222", "Tehran", "Ms", "1", "11111111", "Tofel", "not")
	#act.add_term("P1", "101", "20", "1 April 2020", "20 April 2020", "1")
	#act.add_class("P1-1", "101", "3520345171", "1")
	#print(act.get_student("3520345171"))
	#print(act.get_teacher("1234567890"))
	#print(act.get_term("101"))
	#print(act.get_class("P1-1"))


		




try:
    import glob,os
    import time
    import sqlite3
    from tkinter import *
except ImportError:
    import glob,os
    import time
    import sqlite3
    from Tkinter import *

class DataBase():
    def __init__ (self, db_name = "ShookoohAndishe.db"):
        self.db_name = db_name
    def set_new_data(self):
        try:
            self.make_student_data()
            self.make_teacher_data()
        except :
            local_time = time.asctime(time.localtime(time.time()))
            local_time = "_".join(local_time.split(" "))
            local_time = "_".join(local_time.split(":"))
            self.db_name = "ShookoohAndishe_%s.db"%(local_time)
            self.make_student_data()
            self.make_teacher_data() 
    def make_student_data(self):
        connection = sqlite3.connect("ShookoohAndishe.db")
        cursor = connection.cursor()
        student_sql_command = """
        CREATE TABLE Student ( 
        ID INTEGER PRIMARY KEY, 
        Fname VARCHAR(50), 
        Lname VARCHAR(80),
        nNo VARCHAR(80),
        Bdate VARCHAR(80),
        Father VARCHAR(80),
        Tel VARCHAR(80),
        Phone VARCHAR(80),
        Address VARCHAR(80),
        Company VARCHAR(80),
        CNo VARCHAR(80),
        Pbox VARCHAR(80),
        SNo VARCHAR(80),
        Com VARCHAR(80));"""
        cursor.execute(student_sql_command)
        connection.commit()
        connection.close()
    def make_teacher_data(self):
        connection = sqlite3.connect("ShookoohAndishe.db")
        cursor = connection.cursor()
        teacher_sql_command = """
        CREATE TABLE Teacher ( 
        ID INTEGER PRIMARY KEY, 
        Fname VARCHAR(50), 
        Lname VARCHAR(80),
        nNo VARCHAR(80),
        Bdate VARCHAR(80),
        Father VARCHAR(80),
        Tel VARCHAR(80),
        Phone VARCHAR(80),
        Address VARCHAR(80),
        Education VARCHAR(80),
        CNo VARCHAR(80),
        Pbox VARCHAR(80),
        Level VARCHAR(80),
        Com VARCHAR(80));"""
        cursor.execute(teacher_sql_command)
        connection.commit()
        connection.close()
    def make_class_struc(seld):
        connection = sqlite3.connect("ShookoohAndishe.db")
        cursor = connection.cursor()
        class_sql_command = """
        CREATE TABLE Class ( 
        ID INTEGER PRIMARY KEY, 
        Name VARCHAR(50), 
        Code VARCHAR(80),
        Value VARCHAR(80),
        Sdate VARCHAR(80),
        Edate VARCHAR(80),
        Term VARCHAR(80));"""
        cursor.execute(class_sql_command)
        connection.commit()
        connection.close()
    def make_classList_struc(seld):
        connection = sqlite3.connect("ShookoohAndishe.db")
        cursor = connection.cursor()
        class_sql_command = """
        CREATE TABLE ClassList ( 
        ID INTEGER PRIMARY KEY, 
        ClassCode VARCHAR(50), 
        StudentCode VARCHAR(80),
        TecherCode VARCHAR(80));"""
        cursor.execute(class_sql_command)
        connection.commit()
        connection.close()
    def make_class_data(self,Name,Code,Value,Sdate,Edate,Term):
        connection = sqlite3.connect("ShookoohAndishe.db")
        cursor = connection.cursor()
        class_sql_command = """INSERT INTO Class(ID, Name,Code,Value,Sdate,Edate,Term)
                VALUES (NULL, "%s","%s","%s","%s","%s","%s");"""%(Name,Code,Value,Sdate,Edate,Term)
        cursor.execute(class_sql_command)
        connection.commit()
        connection.close()
    def add_student_data(Fname,Lname,nNo,Bdate,Father,Tel,Phone,Address,Company,CNo,Pbox,SNo,Com):
        try:
            for file in glob.glob("*.db"):
                db_name = file
            print (db_name)
            connection = sqlite3.connect(db_name)
            cursor = connection.cursor()
            student_sql_command = """INSERT INTO Student(ID, Fname,Lname,nNo,Bdate,Father,Tel,Phone,Address,Company,CNo,Pbox,SNo,Com)
                VALUES (NULL, "%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s");"""%(Fname,Lname,nNo,Bdate,Father,Tel,Phone,Address,Company,CNo,Pbox,SNo,Com)
            cursor.execute(student_sql_command)
            connection.commit()
            connection.close()
        except :
            print ("Don't have a daat base file.")
    def add_teacher_data(Fname,Lname,nNo,Bdate,Father,Tel,Phone,Address,Education,CNo,Pbox,Level,Com):
        try:
            for file in glob.glob("*.db"):
                db_name = file
            print (db_name)
            connection = sqlite3.connect(db_name)
            cursor = connection.cursor()
            student_sql_command = """INSERT INTO Teacher (ID, Fname,Lname,nNo,Bdate,Father,Tel,Phone,Address,Education,CNo,Pbox,Level,Com)
                VALUES (NULL, "%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s");"""%(Fname,Lname,nNo,Bdate,Father,Tel,Phone,Address,Education,CNo,Pbox,Level,Com)
            cursor.execute(student_sql_command)
            connection.commit()
            connection.close()
        except :
            print ("Don't have a daat base file.")
    def add_student_in_cals(self,ClassCode,StudentCode,TecherCode):
        for file in glob.glob("*.db"):
            db_name = file
        print (db_name)
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        class_sql_command = """INSERT INTO ClassList(ID, ClassCode,StudentCode,TecherCode)
                VALUES (NULL, "%s","%s","%s");"""%(ClassCode,StudentCode,TecherCode)
        cursor.execute(class_sql_command)
        connection.commit()
        connection.close()
    def show_student(self,Sno):
        try:
            for file in glob.glob("*.db"):
                db_name = file
            print (db_name)
            connection = sqlite3.connect(db_name)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Student WHERE SNo Like '%s';"%(Sno))
            result = cursor.fetchall()
            print (result)
            connection.close()
            return result
        except :
            print ("Not result")
            connection.close()
            return "Not Data"
    def show_teacher(self,Cno):
        try:
            for file in glob.glob("*.db"):
                db_name = file
            print (db_name)
            connection = sqlite3.connect(db_name)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Teacher WHERE CNo Like '%s';"%(Cno))
            result = cursor.fetchall()
            print (result)
            connection.close()
            return result
        except :
            print ("Not result")
            connection.close()
            return "Not Data"
    def show_class(self,Cno):
        try:
            for file in glob.glob("*.db"):
                db_name = file
            print (db_name)
            connection = sqlite3.connect(db_name)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Class WHERE Code Like '%s';"%(Cno))
            result = cursor.fetchall()
            print (result)
            connection.close()
            return result
        except :
            print ("Not result")
            connection.close()
            return "Not Data"
    def show_class_list(self,Cno):
        try:
            outputList = []
            for file in glob.glob("*.db"):
                db_name = file
            print (db_name)
            outputList.append(Cno)
            connection = sqlite3.connect(db_name)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM ClassList WHERE ClassCode Like '%s';"%(Cno))
            result = cursor.fetchall()
            connection.close()
            print (result)
            for i in range(len(result)):
                print ("/////////////////////////////////////")
                print ("I :", i)
                sno = result[i][2]
                tn = result[i][3]
                connection = sqlite3.connect(db_name)
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM Student WHERE SNo Like '%s';"%(sno))
                sresult = cursor.fetchall()
                connection.close()
                print (sresult)
                if sresult:
                    sdla = sno + " " + sresult[0][2] + " " + sresult[0][3]
                    outputList.append(sdla)
                print ("/////////////////////////////////////")
            outputList.append(tn)
            print (outputList)
            return outputList
        except :
            print ("Not result")
            connection.close()
            return "Not Data"


def GUI_add_student():
    def add_student():
        student = DataBase()
        student.add_student_data(fname_s.get(),lname_s.get(),no_s.get(),date_s.get(),father_s.get(),tel_s.get(),phone_s.get(),address_s.get(),company_s.get(),Cno_s.get(),Sno_s.get(),Pbox_s.get())
        print("OK")
    student = Tk()
    student.title("نرم افزار کنترل آموزشگاه زبان شکوه انديشه - نسخه 1.5")
    student.minsize(width=100, height=200)
    student.resizable(width=False, height=False)
    imgicon = PhotoImage(file='logo.gif')
    home.tk.call('wm', 'iconphoto', student._w, imgicon)
    leftF = LabelFrame(student, width = 200, height = 260, relief = SUNKEN)
    leftF.pack(side = LEFT)
    centerF = LabelFrame(student, width = 260, height = 260, relief = SUNKEN)
    centerF.pack(side = LEFT)
    rightF = LabelFrame(student, width = 200, height = 260, relief = SUNKEN)
    rightF.pack(side = RIGHT)
    # label Students
    personal_data = LabelFrame(rightF, text="اطلاعات دانشجو")
    personal_data.pack(side="left",fill="both", expand="yes")
    # label Professor
    company_data = LabelFrame(centerF, text=" ")
    company_data.pack(side="left",fill="both", expand="yes")
    #personal data
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "نام").pack(fill=X)
    fname_s = Entry(personal_data)
    fname_s.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "نام خانوادگي").pack(fill=X)
    lname_s = Entry(personal_data)
    lname_s.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "نام پدر").pack(fill=X)
    father_s = Entry(personal_data)
    father_s.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "تاريخ تولد").pack(fill=X)
    date_s = Entry(personal_data)
    date_s.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "شماره ملي").pack(fill=X)
    no_s = Entry(personal_data)
    no_s.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "تلفن ثابت").pack(fill=X)
    tel_s = Entry(personal_data)
    tel_s.pack(fill=X,ipady=5)
    #company data
    Label(company_data, font = ('B Nazanin', 15, 'bold'), text = "تلفن همراه").pack(fill=X)
    phone_s = Entry(company_data)
    phone_s.pack(fill=X,ipady=5)
    Label(company_data, font = ('B Nazanin', 15, 'bold'), text = "شرکت").pack(fill=X)
    company_s = Entry(company_data)
    company_s.pack(fill=X,ipady=5)
    Label(company_data, font = ('B Nazanin', 15, 'bold'), text = "شماره پرسنلي").pack(fill=X)
    Cno_s = Entry(company_data)
    Cno_s.pack(fill=X,ipady=5)
    Label(company_data, font = ('B Nazanin', 15, 'bold'), text = "شماره دانشجويي").pack(fill=X)
    Sno_s = Entry(company_data)
    Sno_s.pack(fill=X,ipady=5)
    Label(company_data, font = ('B Nazanin', 15, 'bold'), text = "کد پستي").pack(fill=X)
    Pbox_s = Entry(company_data)
    Pbox_s.pack(fill=X,ipady=5)
    Label(company_data, font = ('B Nazanin', 15, 'bold'), text = "آدرس").pack(fill=X)
    address_s = Entry(company_data)
    address_s.pack(fill=X,ipady=5)
    #btns
    Button(leftF, text="ذخيره اطلاعات", height=15, width=25,
                      activebackground="blue", command=add_student).pack(fill=X)
    Button(leftF, text="بستن", height=15, width=25,
                      activebackground="blue", command="").pack(fill=X)
    #pass
    student.mainloop()
    
def GUI_search_student():
    def search_student():
        student = DataBase()
        data = (student.show_student(sNo.get()))
        save = ""
        for i in data :
            save = save+ str(data[0][0])+ "- "+ str(data[0][2])+ " "+ str(data[0][3])+ " "+ str(data[0][4])+ " "+ str(data[0][5])+ " "+ str(data[0][6])+ " "+ str(data[0][7])+ " "+ str(data[0][8])+ " "+ str(data[0][9])+ " "+ str(data[0][10])+ " "+ str(data[0][11])+ " "+ str(data[0][12])+ " "+ str(data[0][13])+ "\n" 
            indent_show.insert(END, save)
    student = Tk()
    student.title("نرم افزار کنترل آموزشگاه زبان شکوه انديشه - نسخه 1.5")
    student.minsize(width=100, height=200)
    student.resizable(width=False, height=False)
    imgicon = PhotoImage(file='logo.gif')
    home.tk.call('wm', 'iconphoto', student._w, imgicon)
    titelF = Frame(student, width = 100, height = 100, relief = SUNKEN)
    titelF.pack(side = TOP)
    titelFF = Frame(student, width = 100, height = 100, relief = SUNKEN)
    titelFF.pack(side = BOTTOM)
    #top
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "کد دانشجو").pack(side = "right")
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "      ").pack(side = "right")
    sNo = Entry(titelF)
    sNo.pack(side = "right",ipady=5)
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "      ").pack(side = "right")
    Button(titelF, text="جست و جو", height=2, width=25,
                      activebackground="blue", command=search_student).pack(fill=X)
    scrollbar = Scrollbar(titelFF)
    indent_show = Text(titelFF, height=20, width=90, bg = "white", relief = SUNKEN)
    scrollbar.pack(side=RIGHT, fill=Y)
    indent_show.pack(side=LEFT, fill=Y)
    scrollbar.config(command=indent_show.yview)
    indent_show.config(yscrollcommand=scrollbar.set)
    #pass
    student.mainloop()
    
def GUI_edit_student():
    student = Tk()
    student.title("نرم افزار کنترل آموزشگاه زبان شکوه انديشه - نسخه 1.5")
    student.minsize(width=100, height=200)
    student.resizable(width=False, height=False)
    imgicon = PhotoImage(file='logo.gif')
    home.tk.call('wm', 'iconphoto', student._w, imgicon)
    titelF = Frame(student, width = 100, height = 100, relief = SUNKEN)
    titelF.pack(side = TOP)
    leftF = LabelFrame(student, width = 200, height = 260, relief = SUNKEN)
    leftF.pack(side = LEFT)
    centerF = LabelFrame(student, width = 260, height = 260, relief = SUNKEN)
    centerF.pack(side = LEFT)
    rightF = LabelFrame(student, width = 200, height = 260, relief = SUNKEN)
    rightF.pack(side = RIGHT)
    # label Students
    personal_data = LabelFrame(rightF, text="ويرايش اطلاعات دانشجو")
    personal_data.pack(side="left",fill="both", expand="yes")
    # label Professor
    company_data = LabelFrame(centerF, text=" ")
    company_data.pack(side="left",fill="both", expand="yes")
    #top
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "کد دانشجو").pack(side = "right")
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "      ").pack(side = "right")
    sNo = Entry(titelF)
    sNo.pack(side = "right",ipady=5)
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "      ").pack(side = "right")
    Button(titelF, text="جست و جو", height=2, width=25,
                      activebackground="blue", command="").pack(fill=X)
    #personal data
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "نام").pack(fill=X)
    fname = Entry(personal_data)
    fname.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "نام خانوادگي").pack(fill=X)
    lname = Entry(personal_data)
    lname.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "نام پدر").pack(fill=X)
    father = Entry(personal_data)
    father.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "تاريخ تولد").pack(fill=X)
    date = Entry(personal_data)
    date.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "شماره ملي").pack(fill=X)
    no = Entry(personal_data)
    no.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "تلفن ثابت").pack(fill=X)
    tel = Entry(personal_data)
    tel.pack(fill=X,ipady=5)
    #company data
    Label(company_data, font = ('B Nazanin', 15, 'bold'), text = "تلفن همراه").pack(fill=X)
    phone = Entry(company_data)
    phone.pack(fill=X,ipady=5)
    Label(company_data, font = ('B Nazanin', 15, 'bold'), text = "شرکت").pack(fill=X)
    company = Entry(company_data)
    company.pack(fill=X,ipady=5)
    Label(company_data, font = ('B Nazanin', 15, 'bold'), text = "شماره پرسنلي").pack(fill=X)
    company = Entry(company_data)
    company.pack(fill=X,ipady=5)
    Label(company_data, font = ('B Nazanin', 15, 'bold'), text = "شماره دانشجويي").pack(fill=X)
    company = Entry(company_data)
    company.pack(fill=X,ipady=5)
    Label(company_data, font = ('B Nazanin', 15, 'bold'), text = "کد پستي").pack(fill=X)
    company = Entry(company_data)
    company.pack(fill=X,ipady=5)
    Label(company_data, font = ('B Nazanin', 15, 'bold'), text = "آدرس").pack(fill=X)
    company = Entry(company_data)
    company.pack(fill=X,ipady=5)
    #btns
    Button(leftF, text="ذخيره اطلاعات", height=15, width=25,
                      activebackground="blue", command="").pack(fill=X)
    Button(leftF, text="بستن", height=15, width=25,
                      activebackground="blue", command="").pack(fill=X)
    #pass
    student.mainloop()
    
def GUI_remove_student():
    student = Tk()
    student.title("نرم افزار کنترل آموزشگاه زبان شکوه انديشه - نسخه 1.5")
    student.minsize(width=100, height=200)
    student.resizable(width=False, height=False)
    imgicon = PhotoImage(file='logo.gif')
    home.tk.call('wm', 'iconphoto', student._w, imgicon)
    titelF = Frame(student, width = 100, height = 100, relief = SUNKEN)
    titelF.pack(side = TOP)
    titelFF = Frame(student, width = 100, height = 100, relief = SUNKEN)
    titelFF.pack(side = BOTTOM)
    #top
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "کد دانشجو").pack(side = "right")
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "      ").pack(side = "right")
    sNo = Entry(titelF)
    sNo.pack(side = "right",ipady=5)
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "      ").pack(side = "right")
    Button(titelF, text="حذف", height=2, width=25,
                      activebackground="blue", command="").pack(fill=X)
    #pass
    student.mainloop()

def GUI_add_techer():
    def add_techer():
        techer = DataBase()
        techer.add_teacher_data(fname_t.get(),lname_t.get(),no_t.get(),date_t.get(),father_t.get(),tel_t.get(),phone_t.get(),address_t.get(),course_t.get(),Cno_t.get(),Pbox_t.get(),gl_t.get())
        print("OK")
    student = Tk()
    student.title("نرم افزار کنترل آموزشگاه زبان شکوه انديشه - نسخه 1.5")
    student.minsize(width=100, height=200)
    student.resizable(width=False, height=False)
    imgicon = PhotoImage(file='logo.gif')
    home.tk.call('wm', 'iconphoto', student._w, imgicon)
    leftF = LabelFrame(student, width = 200, height = 260, relief = SUNKEN)
    leftF.pack(side = LEFT)
    centerF = LabelFrame(student, width = 260, height = 260, relief = SUNKEN)
    centerF.pack(side = LEFT)
    rightF = LabelFrame(student, width = 200, height = 260, relief = SUNKEN)
    rightF.pack(side = RIGHT)
    # label Students
    personal_data = LabelFrame(rightF, text="اطلاعات استاد")
    personal_data.pack(side="left",fill="both", expand="yes")
    # label Professor
    company_data = LabelFrame(centerF, text=" ")
    company_data.pack(side="left",fill="both", expand="yes")
    #personal data
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "نام").pack(fill=X)
    fname_t = Entry(personal_data)
    fname_t.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "نام خانوادگي").pack(fill=X)
    lname_t = Entry(personal_data)
    lname_t.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "نام پدر").pack(fill=X)
    father_t = Entry(personal_data)
    father_t.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "تاريخ تولد").pack(fill=X)
    date_t = Entry(personal_data)
    date_t.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "شماره ملي").pack(fill=X)
    no_t = Entry(personal_data)
    no_t.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "تلفن ثابت").pack(fill=X)
    tel_t = Entry(personal_data)
    tel_t.pack(fill=X,ipady=5)
    #company data
    Label(company_data, font = ('B Nazanin', 15, 'bold'), text = "تلفن همراه").pack(fill=X)
    phone_t = Entry(company_data)
    phone_t.pack(fill=X,ipady=5)
    Label(company_data, font = ('B Nazanin', 15, 'bold'), text = "شماره پرسنلي").pack(fill=X)
    course_t = Entry(company_data)
    course_t.pack(fill=X,ipady=5)
    Label(company_data, font = ('B Nazanin', 15, 'bold'), text = "ميزان تحصيلات").pack(fill=X)
    Cno_t = Entry(company_data)
    Cno_t.pack(fill=X,ipady=5)
    Label(company_data, font = ('B Nazanin', 15, 'bold'), text = "گروه درسي").pack(fill=X)
    gl_t = Entry(company_data)
    gl_t.pack(fill=X,ipady=5)
    Label(company_data, font = ('B Nazanin', 15, 'bold'), text = "کد پستي").pack(fill=X)
    Pbox_t = Entry(company_data)
    Pbox_t.pack(fill=X,ipady=5)
    Label(company_data, font = ('B Nazanin', 15, 'bold'), text = "آدرس").pack(fill=X)
    address_t = Entry(company_data)
    address_t.pack(fill=X,ipady=5)
    #btns
    Button(leftF, text="ذخيره اطلاعات", height=15, width=25,
                      activebackground="blue", command=add_techer).pack(fill=X)
    Button(leftF, text="بستن", height=15, width=25,
                      activebackground="blue", command="").pack(fill=X)
    #pass
    student.mainloop()
    
def GUI_search_techer():
    def search_techer():
        teacher = DataBase()
        data = (teacher.show_teacher(sNo.get()))
        save = ""
        for i in data :
            save = save+ str(data[0][0])+ "- "+ str(data[0][2])+ " "+ str(data[0][3])+ " "+ str(data[0][4])+ " "+ str(data[0][5])+ " "+ str(data[0][6])+ " "+ str(data[0][7])+ " "+ str(data[0][8])+ " "+ str(data[0][9])+ " "+ str(data[0][10])+ " "+ str(data[0][11])+ " "+ str(data[0][12])+ " "+ str(data[0][13])+ "\n" 
            indent_show.insert(END, save)
    student = Tk()
    student.title("نرم افزار کنترل آموزشگاه زبان شکوه انديشه - نسخه 1.5")
    student.minsize(width=100, height=200)
    student.resizable(width=False, height=False)
    imgicon = PhotoImage(file='logo.gif')
    home.tk.call('wm', 'iconphoto', student._w, imgicon)
    titelF = Frame(student, width = 100, height = 100, relief = SUNKEN)
    titelF.pack(side = TOP)
    titelFF = Frame(student, width = 100, height = 100, relief = SUNKEN)
    titelFF.pack(side = BOTTOM)
    #top
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "شماره پرسنلي").pack(side = "right")
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "      ").pack(side = "right")
    sNo = Entry(titelF)
    sNo.pack(side = "right",ipady=5)
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "      ").pack(side = "right")
    Button(titelF, text="جست و جو", height=2, width=25,
                      activebackground="blue", command=search_techer).pack(fill=X)
    scrollbar = Scrollbar(titelFF)
    indent_show = Text(titelFF, height=20, width=90, bg = "white", relief = SUNKEN)
    scrollbar.pack(side=RIGHT, fill=Y)
    indent_show.pack(side=LEFT, fill=Y)
    scrollbar.config(command=indent_show.yview)
    indent_show.config(yscrollcommand=scrollbar.set)
    #pass
    student.mainloop()
    
def GUI_edit_techer():
    student = Tk()
    student.title("نرم افزار کنترل آموزشگاه زبان شکوه انديشه - نسخه 1.5")
    student.minsize(width=100, height=200)
    student.resizable(width=False, height=False)
    imgicon = PhotoImage(file='logo.gif')
    home.tk.call('wm', 'iconphoto', student._w, imgicon)
    titelF = Frame(student, width = 100, height = 100, relief = SUNKEN)
    titelF.pack(side = TOP)
    leftF = LabelFrame(student, width = 200, height = 260, relief = SUNKEN)
    leftF.pack(side = LEFT)
    centerF = LabelFrame(student, width = 260, height = 260, relief = SUNKEN)
    centerF.pack(side = LEFT)
    rightF = LabelFrame(student, width = 200, height = 260, relief = SUNKEN)
    rightF.pack(side = RIGHT)
    # label Students
    personal_data = LabelFrame(rightF, text="ويرايش اطلاعات استاد")
    personal_data.pack(side="left",fill="both", expand="yes")
    # label Professor
    company_data = LabelFrame(centerF, text=" ")
    company_data.pack(side="left",fill="both", expand="yes")
    #top
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "شماره پرسنلي").pack(side = "right")
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "      ").pack(side = "right")
    sNo = Entry(titelF)
    sNo.pack(side = "right",ipady=5)
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "      ").pack(side = "right")
    Button(titelF, text="جست و جو", height=2, width=25,
                      activebackground="blue", command="").pack(fill=X)
    #personal data
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "نام").pack(fill=X)
    fname = Entry(personal_data)
    fname.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "نام خانوادگي").pack(fill=X)
    lname = Entry(personal_data)
    lname.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "نام پدر").pack(fill=X)
    father = Entry(personal_data)
    father.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "تاريخ تولد").pack(fill=X)
    date = Entry(personal_data)
    date.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "شماره ملي").pack(fill=X)
    no = Entry(personal_data)
    no.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "تلفن ثابت").pack(fill=X)
    tel = Entry(personal_data)
    tel.pack(fill=X,ipady=5)
    #company data
    Label(company_data, font = ('B Nazanin', 15, 'bold'), text = "تلفن همراه").pack(fill=X)
    phone = Entry(company_data)
    phone.pack(fill=X,ipady=5)
    Label(company_data, font = ('B Nazanin', 15, 'bold'), text = "ميزان تحصيلات").pack(fill=X)
    company = Entry(company_data)
    company.pack(fill=X,ipady=5)
    Label(company_data, font = ('B Nazanin', 15, 'bold'), text = "شماره پرسنلي").pack(fill=X)
    company = Entry(company_data)
    company.pack(fill=X,ipady=5)
    Label(company_data, font = ('B Nazanin', 15, 'bold'), text = "گروه درسي").pack(fill=X)
    company = Entry(company_data)
    company.pack(fill=X,ipady=5)
    Label(company_data, font = ('B Nazanin', 15, 'bold'), text = "کد پستي").pack(fill=X)
    company = Entry(company_data)
    company.pack(fill=X,ipady=5)
    Label(company_data, font = ('B Nazanin', 15, 'bold'), text = "آدرس").pack(fill=X)
    company = Entry(company_data)
    company.pack(fill=X,ipady=5)
    #btns
    Button(leftF, text="ذخيره اطلاعات", height=15, width=25,
                      activebackground="blue", command="").pack(fill=X)
    Button(leftF, text="بستن", height=15, width=25,
                      activebackground="blue", command="").pack(fill=X)
    #pass
    student.mainloop()
    
def GUI_remove_techer():
    student = Tk()
    student.title("نرم افزار کنترل آموزشگاه زبان شکوه انديشه - نسخه 1.5")
    student.minsize(width=100, height=200)
    student.resizable(width=False, height=False)
    imgicon = PhotoImage(file='logo.gif')
    home.tk.call('wm', 'iconphoto', student._w, imgicon)
    titelF = Frame(student, width = 100, height = 100, relief = SUNKEN)
    titelF.pack(side = TOP)
    titelFF = Frame(student, width = 100, height = 100, relief = SUNKEN)
    titelFF.pack(side = BOTTOM)
    #top
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "شماره پرسنلي").pack(side = "right")
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "      ").pack(side = "right")
    sNo = Entry(titelF)
    sNo.pack(side = "right",ipady=5)
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "      ").pack(side = "right")
    Button(titelF, text="حذف", height=2, width=25,
                      activebackground="blue", command="").pack(fill=X)
    #pass
    student.mainloop()

def GUI_add_class():
    def add_class():
        clas = DataBase()
        clas.make_class_data(name_c.get(),code_c.get(),value_c.get(),sdate_c.get(),edate_c.get(),term_c.get())
        print ("ok")
    classs = Tk()
    classs.title("نرم افزار کنترل آموزشگاه زبان شکوه انديشه - نسخه 1.5")
    classs.minsize(width=100, height=200)
    classs.resizable(width=False, height=False)
    imgicon = PhotoImage(file='logo.gif')
    home.tk.call('wm', 'iconphoto', classs._w, imgicon)
    leftF = LabelFrame(classs, width = 200, height = 260, relief = SUNKEN)
    leftF.pack(side = LEFT)
    rightF = LabelFrame(classs, width = 200, height = 260, relief = SUNKEN)
    rightF.pack(side = RIGHT)
    # label Students
    personal_data = LabelFrame(rightF, text="اطلاعات کلاس")
    personal_data.pack(side="left",fill="both", expand="yes")
    #personal data
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "نام کلاس").pack(fill=X)
    name_c = Entry(personal_data)
    name_c.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "کد کلاس").pack(fill=X)
    code_c = Entry(personal_data)
    code_c.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "ظرفيت کلاس").pack(fill=X)
    value_c = Entry(personal_data)
    value_c.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "تاريخ شروع").pack(fill=X)
    sdate_c = Entry(personal_data)
    sdate_c.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "تاريخ پايان").pack(fill=X)
    edate_c = Entry(personal_data)
    edate_c.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "ترم").pack(fill=X)
    term_c = Entry(personal_data)
    term_c.pack(fill=X,ipady=5)
    #btns
    Button(leftF, text="ذخيره اطلاعات", height=15, width=25,
                      activebackground="blue", command=add_class).pack(fill=X)
    Button(leftF, text="بستن", height=15, width=25,
                      activebackground="blue", command="").pack(fill=X)
    #pass
    classs.mainloop()
    
def GUI_search_class():
    def search_class():
        clas = DataBase()
        data = (clas.show_class(sNo.get()))
        print (data)
        save = ""
        for i in data :
            save = save+ str(data[0][0])+ "- "+ str(data[0][1])+ " "+ str(data[0][2])+ " "+ str(data[0][3])+ " "+ str(data[0][4])+ " "+ str(data[0][5])+ " "+ str(data[0][6])+ "\n" 
            indent_show.insert(END, save)
    student = Tk()
    student.title("نرم افزار کنترل آموزشگاه زبان شکوه انديشه - نسخه 1.5")
    student.minsize(width=100, height=200)
    student.resizable(width=False, height=False)
    imgicon = PhotoImage(file='logo.gif')
    home.tk.call('wm', 'iconphoto', student._w, imgicon)
    titelF = Frame(student, width = 100, height = 100, relief = SUNKEN)
    titelF.pack(side = TOP)
    titelFF = Frame(student, width = 100, height = 100, relief = SUNKEN)
    titelFF.pack(side = BOTTOM)
    #top
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "کد کلاس").pack(side = "right")
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "      ").pack(side = "right")
    sNo = Entry(titelF)
    sNo.pack(side = "right",ipady=5)
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "      ").pack(side = "right")
    Button(titelF, text="جست و جو", height=2, width=25,
                      activebackground="blue", command=search_class).pack(fill=X)
    scrollbar = Scrollbar(titelFF)
    indent_show = Text(titelFF, height=20, width=90, bg = "white", relief = SUNKEN)
    scrollbar.pack(side=RIGHT, fill=Y)
    indent_show.pack(side=LEFT, fill=Y)
    scrollbar.config(command=indent_show.yview)
    indent_show.config(yscrollcommand=scrollbar.set)
    #pass
    student.mainloop()
    
def GUI_edit_class():
    student = Tk()
    student.title("نرم افزار کنترل آموزشگاه زبان شکوه انديشه - نسخه 1.5")
    student.minsize(width=100, height=200)
    student.resizable(width=False, height=False)
    imgicon = PhotoImage(file='logo.gif')
    home.tk.call('wm', 'iconphoto', student._w, imgicon)
    titelF = Frame(student, width = 100, height = 100, relief = SUNKEN)
    titelF.pack(side = TOP)
    leftF = LabelFrame(student, width = 200, height = 260, relief = SUNKEN)
    leftF.pack(side = LEFT)
    rightF = LabelFrame(student, width = 200, height = 260, relief = SUNKEN)
    rightF.pack(side = RIGHT)
    # label Students
    personal_data = LabelFrame(rightF, text="ويرايش اطلاعات کلاس")
    personal_data.pack(side="left",fill="both", expand="yes")
    #top
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "کد کلاس").pack(side = "right")
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "      ").pack(side = "right")
    sNo = Entry(titelF)
    sNo.pack(side = "right",ipady=5)
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "      ").pack(side = "right")
    Button(titelF, text="جست و جو", height=2, width=25,
                      activebackground="blue", command="").pack(fill=X)
    #personal data
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "نام کلاس").pack(fill=X)
    fname = Entry(personal_data)
    fname.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "کد کلاس").pack(fill=X)
    lname = Entry(personal_data)
    lname.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "ظرفيت کلاس").pack(fill=X)
    father = Entry(personal_data)
    father.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "تاريخ شروع").pack(fill=X)
    date = Entry(personal_data)
    date.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "تاريخ پايان").pack(fill=X)
    no = Entry(personal_data)
    no.pack(fill=X,ipady=5)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "ترم").pack(fill=X)
    tel = Entry(personal_data)
    tel.pack(fill=X,ipady=5)
    #btns
    Button(leftF, text="ذخيره اطلاعات", height=15, width=25,
                      activebackground="blue", command="").pack(fill=X)
    Button(leftF, text="بستن", height=15, width=25,
                      activebackground="blue", command="").pack(fill=X)
    #pass
    student.mainloop()

def GUI_remove_class():
    student = Tk()
    student.title("نرم افزار کنترل آموزشگاه زبان شکوه انديشه - نسخه 1.5")
    student.minsize(width=100, height=200)
    student.resizable(width=False, height=False)
    imgicon = PhotoImage(file='logo.gif')
    home.tk.call('wm', 'iconphoto', student._w, imgicon)
    titelF = Frame(student, width = 100, height = 100, relief = SUNKEN)
    titelF.pack(side = TOP)
    titelFF = Frame(student, width = 100, height = 100, relief = SUNKEN)
    titelFF.pack(side = BOTTOM)
    #top
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "کد کلاس").pack(side = "right")
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "      ").pack(side = "right")
    sNo = Entry(titelF)
    sNo.pack(side = "right",ipady=5)
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "      ").pack(side = "right")
    Button(titelF, text="حذف", height=2, width=25,
                      activebackground="blue", command="").pack(fill=X)
    #pass
    student.mainloop()

def GUI_add_student_class():
    def add_student_class():
        sc = DataBase()
        sc.add_student_in_cals(Cno_ac.get(),Sno_ac.get(),Tno_ac.get())
        print ("OK")
    student = Tk()
    student.title("نرم افزار کنترل آموزشگاه زبان شکوه انديشه - نسخه 1.5")
    student.minsize(width=100, height=200)
    student.resizable(width=False, height=False)
    imgicon = PhotoImage(file='logo.gif')
    home.tk.call('wm', 'iconphoto', student._w, imgicon)
    leftF = LabelFrame(student, width = 200, height = 260, relief = SUNKEN)
    leftF.pack(side = LEFT)
    rightF = LabelFrame(student, width = 200, height = 260, relief = SUNKEN)
    rightF.pack(side = RIGHT)
    # label Students
    personal_data = LabelFrame(rightF, text="ثبت دانشجو در کلاس")
    personal_data.pack(side="left",fill="both", expand="yes")
    #personal data
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "کد کلاس").pack(fill=X)
    Cno_ac = Entry(personal_data)
    Cno_ac.pack(fill=X,ipady=6)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "کد دانشجو").pack(fill=X)
    Sno_ac = Entry(personal_data)
    Sno_ac.pack(fill=X,ipady=6)
    Label(personal_data, font = ('B Nazanin', 15, 'bold'), text = "کد استاد").pack(fill=X)
    Tno_ac = Entry(personal_data)
    Tno_ac.pack(fill=X,ipady=6)
    #btns
    Button(leftF, text="ذخيره اطلاعات", height=5, width=30,
                      activebackground="blue", command=add_student_class).pack(fill=X)
    Button(leftF, text="بستن", height=5, width=30,
                      activebackground="blue", command="").pack(fill=X)
    #pass
    student.mainloop()
    
def GUI_remove__student_class():
    student = Tk()
    student.title("نرم افزار کنترل آموزشگاه زبان شکوه انديشه - نسخه 1.5")
    student.minsize(width=100, height=200)
    student.resizable(width=False, height=False)
    imgicon = PhotoImage(file='logo.gif')
    home.tk.call('wm', 'iconphoto', student._w, imgicon)
    titelF = Frame(student, width = 100, height = 100, relief = SUNKEN)
    titelF.pack(side = TOP)
    titelFF = Frame(student, width = 100, height = 100, relief = SUNKEN)
    titelFF.pack(side = BOTTOM)
    #top
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "کد دانشجو").pack(side = "right")
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "      ").pack(side = "right")
    sNo = Entry(titelF)
    sNo.pack(side = "right",ipady=5)
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "کد کلاس").pack(side = "right")
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "      ").pack(side = "right")
    sNo = Entry(titelF)
    sNo.pack(side = "right",ipady=5)
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "      ").pack(side = "right")
    Button(titelF, text="حذف", height=2, width=25,
                      activebackground="blue", command="").pack(fill=X)
    #pass
    student.mainloop()

def GUI_show_list_class():
    def search_class():
        clas = DataBase()
        teach = DataBase()
        data = (clas.show_class_list(sNo.get()))
        print (data)
        lenL = len(data)
        lenT = lenL - 1
        lenF = lenT 
        Csave = "Class Code : " + str(data[0]) + "\n"
        teacher = teach.show_teacher(data[lenT])
        Tsave = "Teacher Code : " + str(data[lenT]) + " - " + str(teacher[0][2])+" "+ str(teacher[0][3]) + "\n"
        save = ""
        for i in range (1,lenF) :
            save = save + str(data[i]) + "\n"
        ssave = Csave + save + Tsave
        indent_show.insert(END, ssave)
    student = Tk()
    student.title("نرم افزار کنترل آموزشگاه زبان شکوه انديشه - نسخه 1.5")
    student.minsize(width=100, height=200)
    student.resizable(width=False, height=False)
    imgicon = PhotoImage(file='logo.gif')
    home.tk.call('wm', 'iconphoto', student._w, imgicon)
    titelF = Frame(student, width = 100, height = 100, relief = SUNKEN)
    titelF.pack(side = TOP)
    titelFF = Frame(student, width = 100, height = 100, relief = SUNKEN)
    titelFF.pack(side = BOTTOM)
    #top
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "کد کلاس").pack(side = "right")
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "      ").pack(side = "right")
    sNo = Entry(titelF)
    sNo.pack(side = "right",ipady=5)
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "      ").pack(side = "right")
    Button(titelF, text="جست و جو", height=2, width=25,
                      activebackground="blue", command=search_class).pack(fill=X)
    scrollbar = Scrollbar(titelFF)
    indent_show = Text(titelFF, height=20, width=90, bg = "white", relief = SUNKEN)
    scrollbar.pack(side=RIGHT, fill=Y)
    indent_show.pack(side=LEFT, fill=Y)
    scrollbar.config(command=indent_show.yview)
    indent_show.config(yscrollcommand=scrollbar.set)
    #pass
    student.mainloop()

def GUI_remove__teacher_class():
    student = Tk()
    student.title("نرم افزار کنترل آموزشگاه زبان شکوه انديشه - نسخه 1.5")
    student.minsize(width=100, height=200)
    student.resizable(width=False, height=False)
    imgicon = PhotoImage(file='logo.gif')
    home.tk.call('wm', 'iconphoto', student._w, imgicon)
    titelF = Frame(student, width = 100, height = 100, relief = SUNKEN)
    titelF.pack(side = TOP)
    titelFF = Frame(student, width = 100, height = 100, relief = SUNKEN)
    titelFF.pack(side = BOTTOM)
    #top
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "شماره پرسنلي").pack(side = "right")
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "      ").pack(side = "right")
    sNo = Entry(titelF)
    sNo.pack(side = "right",ipady=5)
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "کد کلاس").pack(side = "right")
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "      ").pack(side = "right")
    sNo = Entry(titelF)
    sNo.pack(side = "right",ipady=5)
    Label(titelF, font = ('B Nazanin', 15, 'bold'), text = "      ").pack(side = "right")
    Button(titelF, text="حذف", height=2, width=25,
                      activebackground="blue", command="").pack(fill=X)
    #pass
    student.mainloop()


while 1:
    home = Tk()
    home.title("نرم افزار کنترل آموزشگاه زبان شکوه انديشه - نسخه 1.5")
    home.minsize(width=100, height=200)
    home.resizable(width=False, height=False)
    imgicon = PhotoImage(file='logo.gif')
    home.tk.call('wm', 'iconphoto', home._w, imgicon)
    titelF = Frame(home, width = 100, height = 100, relief = SUNKEN)
    titelF.pack(side = TOP)
    leftF = LabelFrame(home, width = 200, height = 260, relief = SUNKEN)
    leftF.pack(side = LEFT)
    centerF = LabelFrame(home, width = 260, height = 260, relief = SUNKEN)
    centerF.pack(side = LEFT)
    rightF = LabelFrame(home, width = 200, height = 260, relief = SUNKEN)
    rightF.pack(side = RIGHT)
    # label Students
    labelframe_Students = LabelFrame(leftF, text="دانشجويان")
    labelframe_Students.pack(side="left",fill="both", expand="yes")
    # label Professor
    labelframe_Professor = LabelFrame(leftF, text="اساتيد")
    labelframe_Professor.pack(side="left",fill="both", expand="yes")
    # logo
    logo = PhotoImage(file="logo.gif")
    w1 = Label(centerF, image=logo).pack(side="right", padx=2)
    # label User
    labelframe_User = LabelFrame(rightF, text="کاربر سيستم")
    labelframe_User.pack(side="right",expand="yes")
    # label Classes
    labelframe_Classes = LabelFrame(rightF, text="کلاس ها")
    labelframe_Classes.pack(side="right", expand="yes")
    #Titel
    Label(titelF, font = ('B Nazanin', 50, 'bold'), text = "آموزشگاه زبان شکوه انديشه", fg = 'steel blue', bd = 10, anchor = 'w').pack(fill=X)
    # Student
    Sing_s = Button(labelframe_Students, text="ثبت نام دانشجو", height=4, width=25,
                    activebackground="blue", command=GUI_add_student).pack(fill=X)
    Search_s = Button(labelframe_Students, text="جست و جو دانشجو", height=4, width=25,
                      activebackground="blue", command=GUI_search_student).pack(fill=X)
    Edit_s = Button(labelframe_Students, text="ويرايش دانشجو", height=4, width=25,
                    activebackground="blue", command="GUI_edit_student").pack(fill=X)
    Remove_s = Button(labelframe_Students, text="حذف دانشجو", height=4, width=25,
                      activebackground="blue", command="GUI_remove_student").pack(fill=X)
    # Professor
    Sing_p = Button(labelframe_Professor, text="ثبت استاد", height=4, width=10,
                    activebackground="blue", command=GUI_add_techer).pack(fill=X)
    Search_p = Button(labelframe_Professor, text="جست و جو استاد", height=4, width=25,
                      activebackground="blue", command=GUI_search_techer).pack(fill=X)
    Edit_p = Button(labelframe_Professor, text="ويرايش استاد", height=4, width=25,
                    activebackground="blue", command="GUI_edit_techer").pack(fill=X)
    Remove_p = Button(labelframe_Professor, text="حذف استاد", height=4, width=25,
                      activebackground="blue", command="GUI_remove_techer").pack(fill=X)
   # Classes
    Sing_c = Button(labelframe_Classes, text="ثبت کلاس", height=4, width=25,
                    activebackground="blue", command=GUI_add_class).pack(fill=X)
    Search_c = Button(labelframe_Classes, text="نمايش کلاس", height=4, width=25,
                      activebackground="blue", command=GUI_search_class).pack(fill=X)
    Edit_c = Button(labelframe_Classes, text="ويرايش کلاس", height=4, width=25,
                    activebackground="blue", command="GUI_edit_class").pack(fill=X)
    Remove_c = Button(labelframe_Classes, text="حذف کلاس", height=4, width=25,
                      activebackground="blue", command="GUI_remove_class").pack(fill=X)

    # User
    Sing_u = Button(labelframe_User, text="ثبت دانشجو در کلاس", height=4, width=25,
                    activebackground="blue", command=GUI_add_student_class).pack(fill=X)
    Search_u = Button(labelframe_User, text="حذف دانشجو از کلاس", height=4, width=25,
                      activebackground="blue", command="GUI_remove__student_class").pack(fill=X)
    Edit_u = Button(labelframe_User, text="نمايش ليست کلاس", height=4, width=25,
                    activebackground="blue", command=GUI_show_list_class).pack(fill=X)
    Remove_u = Button(labelframe_User, text="پرينت ليست کلاس", height=4, width=25,
                      activebackground="blue", command="GUI_remove__teacher_class").pack(fill=X)

    mainloop()
    break

from tkinter import *
import sqlite3
import time 
import math
import random 
import os 
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image

root = Tk()




#window 1



Roman = ('Times New Roman', 18)

space1 = '                   '
space2 = '              '

Label2 = Label(root, text= space1 + "School App 1.0"+ space2, padx=30, pady=20, bg='medium sea green', borderwidth=5, font=("Times New Roman",25))
Label2.grid(row=0, column=0, columnspan=3)


#config rows and columns

def addcourse():


    course = Toplevel()


    course_entry = Entry(course, width=30, font = ("Helvetica Neue", 20))
    course_entry.place(x=15, y=0)

    btn_course = Button(course, padx=180,text= "Submit",font =("Helvetica Neue", 20),bg="sky blue")
    btn_course.place(x = 20, y= 40)

    my_label2 = Label(course,width=40, text="Coming soon                                         ", font =("Helvetica Neue", 34))
    my_label2.place(x=10, y= 200) 

    course_entry.delete(0, END)


    course.title("Add A Course")
    course.geometry("500x600")
    course.resizable(False, False)

def background():
    pass





#=============================================main buttons ==============================================================
calculator_button = Button(root, text="Calculator", padx=30, pady=25, font=Roman, command=lambda:calculator())
calculator_button.grid(row=2, column=0, sticky="nsew")

courses = Button(root, text="Add Course", padx=30, pady=25, font=Roman, command=lambda:addcourse())
courses.grid(row=2, column=1, padx=2, sticky="nsew")

students = Button(root, text="Students", padx=30, pady=25, font=Roman, command=lambda: students())
students.grid(row=2, column=2, sticky="nsew")

grid_button = Button(root, text="    Graph   ", padx=30, pady=25, font=Roman, command =lambda: graph())
grid_button.grid(row=3, column=0, sticky="nsew")

quit_button = Button(root, text="     Quit       ", padx=30, pady=25, font=Roman, command=root.quit)
quit_button.grid(row=3, column=1, sticky="nsew")

staff = Button(root, text="  Staff    ", padx=30, pady=25, font=Roman, command=lambda: staff())
staff.grid(row=3, column=2, sticky="nsew")




#=================================================functions=============================================================





def students():
    global first1, age1, grade1, last1, e
    Students = Toplevel()

    first1 = Entry(Students,width=30, font=Roman)
    first1.grid(row=0, column=2)

    age1 = Entry(Students,width=30, font=Roman)
    age1.grid(row=1, column=2, pady=20)

    grade1 = Entry(Students,width=30, font=Roman)
    grade1.grid(row=2, column=2, pady=20)

    last1 = Entry(Students,width=30, font=Roman)
    last1.grid(row=3, column=2, pady=20)

    b6 = Button(Students,text="First Name",padx=30, pady=0,font=Roman, state=DISABLED)
    b6.grid(row=0, column=3)

    b7 = Button(Students,text="       Age      ",padx=25, pady=0,font=Roman, state=DISABLED)
    b7.grid(row=1, column=3)

    b8 = Button(Students,text="     Grade     ",padx=25, pady=0,font=Roman, state=DISABLED)
    b8.grid(row=2, column=3)

    b9 = Button(Students,text="  Last Name",padx=25, pady=0,font=Roman, state=DISABLED)
    b9.grid(row=3, column=3)

    b10 = Button(Students,text="       Add A student      ",padx=25, pady=30,font=("Times New Roman",30), state=DISABLED)
    b10.grid(row=4, column=2,padx=20)

    b11 = Button(Students,text="  Submit Record   ",padx=20, pady=40,font=Roman,bg='hot pink',command=lambda: submit())
    b11.grid(row=4, column=3)

    b12 = Button(Students, text="   Show Records  ", padx=30, pady=10, font=Roman,bg='#8aecff',command=lambda: query())
    b12.grid(row=5, column=3,pady=10)

    #delteting records uwu




    b13 = Button(Students, text='Delete ID',padx=40, pady=10,font=Roman,bg='spring green',command=lambda:delete())
    b13.place(x=274, y=410)

    e = Entry(Students, width=10,font=("Times New Roman",34))
    e.place(x=30, y=412)



    #=========================
    Students.title("Add a student")
    Students.geometry('736x500')


def staff():
    staff = Toplevel()


    d = '''This is a special project that I recentley worked on. It is not fully finished but this
    is just a project that used a nice GUI interface in python, and used an in-built database within a file in
    SQL. It also used the matplotlib module, and most importantly, the Tkinter module. I hope you enjoy playing around
    with this. Have fun!'''


    my_label69 = Label(staff, padx=100, pady=140,text='Made By: Maulik Verma',font=("Helvetica Neue",45))
    my_label69.place(x=500, y=0)

    my_label69 = Label(staff, padx=100, pady=140,text=d,font=("Helvetica Neue",20))
    my_label69.place(x=100, y=300)

    
    staff.title('Staff')
    staff.geometry("1800x700")
    staff.mainloop()


def calculator():
    global calculation_entry
    calculator1 = Toplevel()

    calculator1.title('Calculator')


    calculation_entry = Entry(calculator1, width=34,borderwidth=5, font=('Times New Roman', 19),fg='black' )
    calculation_entry.grid(row=0, column=0, columnspan=3, padx=20)

    seven = Button(calculator1, text='    7        ',padx=30, pady=25, borderwidth=3, font=Roman, command=lambda: calculations(7))
    seven.grid(row=2, column=0)

    eigth = Button(calculator1, text='    8    ',padx=30, pady=25, borderwidth=3, font=Roman,command=lambda: calculations(8))
    eigth.grid(row=2, column=1)

    nine = Button(calculator1, text='    9    ',padx=30, pady=25, borderwidth=3, font=Roman, command=lambda: calculations(9))
    nine.grid(row=2, column=2)

    four = Button(calculator1, text='    4    ',padx=40, pady=25, borderwidth=3, font=Roman, command=lambda: calculations(4))
    four.place(x=6, y=140)

    five = Button(calculator1, text='    5    ',padx=32, pady=25, borderwidth=3, font=Roman, command=lambda: calculations(5))
    five.place(x=170, y=140)

    six = Button(calculator1, text='    6    ',padx=28, pady=25, borderwidth=3, font=Roman, command=lambda: calculations(6))
    six.place(x=320, y=140)

    three = Button(calculator1, text='    3    ',padx=39, pady=25, borderwidth=3, font=Roman, command=lambda: calculations(3))
    three.place(x=9, y=240)

    two = Button(calculator1, text='    2    ',padx=32, pady=25, borderwidth=3, font=Roman, command=lambda: calculations(2))
    two.place(x=170, y=240)

    one = Button(calculator1, text='    1    ',padx=28, pady=25, borderwidth=3, font=Roman, command=lambda: calculations(1))
    one.place(x=320, y=240)

    zero = Button(calculator1, text='    0    ',padx=37, pady=25, borderwidth=3, font=Roman, command=lambda: calculations(1))
    zero.place(x=9, y=340)


    add_button = Button(calculator1, text='       +     ', padx=17, pady=25, borderwidth=3, font=Roman, command= add)
    add_button.place(x=320, y=340)         


    multilpy_button = Button(calculator1, text='        x       ', padx=17, pady=25, borderwidth=3, font=Roman, command= multiply)
    multilpy_button.place(x=9, y=440) 

    divide_button = Button(calculator1, text='        /       ', padx=14, pady=25, borderwidth=3, font=Roman, command= divide)
    divide_button.place(x=170, y=440) 

    subtract_button = Button(calculator1, text='        -       ', padx=14, pady=25, borderwidth=3, font=Roman, command= subtract)
    subtract_button.place(x=320, y=440) 


    equal_button = Button(calculator1, text='     =    ', padx=28, pady=25, borderwidth=3, font=Roman, command= equal)
    equal_button.place(x=170, y=340)

    calculator1.resizable(False, False)

    clear_button = Button(calculator1, text='      Clear     ', padx=150, pady=25, borderwidth=3, font=Roman, command= clear)
    clear_button.place(x=20, y=542)

    calculator1.geometry('470x650')

def clear():
    calculation_entry.delete(0, END)

def calculations(number):
    global calculation_entry
    current = calculation_entry.get()
    calculation_entry.delete(0, END)
    calculation_entry.insert(0, str(current) + str(number))


def add():
    global math, f_num, calculation_entry
    first_num = calculation_entry.get()
    f_num = int(first_num)
    calculation_entry.delete(0, END)
    math = 'addition'
def divide():
    global math, f_num, calculation_entry
    first_num = calculation_entry.get()
    f_num = int(first_num)
    calculation_entry.delete(0, END)
    math = 'divide'

def subtract():
    global math, f_num, calculation_entry
    first_num = calculation_entry.get()
    f_num = int(first_num)
    calculation_entry.delete(0, END)
    math = 'subtract'


def multiply():
    global math, f_num, calculation_entry
    first_num = calculation_entry.get()
    f_num = int(first_num)
    calculation_entry.delete(0, END)
    math = 'multiply'

def equal():
    global math, f_num, calculation_entry
    second_number = calculation_entry.get()
    calculation_entry.delete(0, END)

    if math =='addition':
        calculation_entry.insert(0, str(f_num + int(second_number)))
    if math =='multiply':
        calculation_entry.insert(0, str(f_num * int(second_number)))
    if math =='divide':
        calculation_entry.insert(0, str(f_num / int(second_number)))
    if math =='subtract':
        calculation_entry.insert(0, str(f_num - int(second_number)))







def graph():
    from matplotlib import pyplot as plt 
    x = [26,27,28,30,32,34,45, 50]
    dev_y = [60_000,70_000,80_000,90_000,100_000,110_000, 135_000, 140_000]

    #plotting more specific lines 

    py_plot_y = [63000,70000,85000,99000,105000,114000, 120000, 125000]

    africa = [24000,30000,34000,40000,43000,47000, 50000,52400]






    #plotting and other details 
    plt.plot(x, py_plot_y,color='blue',linestyle='--',label='Professors in Mass',marker='o')
    plt.plot(x, dev_y,label='All Professors in US',color='orange',marker='o')
    plt.plot(x, africa,label='African Professors',color='black',marker='o')

    plt.title('USD Capital Pay for US And Massachussets')
    plt.xlabel('Ages')
    plt.ylabel('Salary Per Year')


    #adding legends to represent data 


    plt.legend()

    plt.show()
    
    
#=================================================Classes================================================================


class Student:
    def __init__(self, name, grade, age, last):
        self.name = name
        self.grade = grade
        self.age = age
        self.last = last

    def get_grade(self):
        return self.grade

    


class Course:
    def __init__(self, name, max_students):
        self.name = name 
        self.max_students = max_students
        self.students = []

        
        


    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student.name + '  '+student.last)
            return True
        return False 

    def average(self):
        pass


    def return_students(self, Course):
        print(Course.students)
    
        

#+=======================================Objects of classes==============================================================

s1 = Student("Maulik", 100, 14, "Verma")
s2 = Student("Erwin",96, 32, "Smith")
s3 = Student("Levi",130,23, "Ackermann")
s4 = Student("Sapna",10000,39,"Verma")


Math = Course("Math", 5)
Math.add_student(s1)
Math.add_student(s2)
Math.add_student(s3)
Math.add_student(s4)





#================================================Main Config============================================================



#===============================================Database================================================================

schooldatabase = sqlite3.connect('SchoolDatabase.db')

cursor = schooldatabase.cursor()

"""
cursor.execute('''CREATE TABLE studentd (
            first text,
            age integer,
            grade integer,
            last text
            )''')
"""


def submit():
    global print_records

    schooldatabase = sqlite3.connect('SchoolDatabase.db')


    cursor = schooldatabase.cursor()
    records = cursor.fetchall()


    print_records = ''
    for record in records:
        if first1.get() == str(record[0]):
            if last1.get() == str(record[3]):

                messagebox.showerror("Hello", 'HELLo')
                pass

    cursor.execute("INSERT INTO studentd VALUES (:first1, :age1, :grade1, :last1)",
        {
        'first1': first1.get(),
        'age1': age1.get(),
        'grade1': grade1.get(),
        'last1': last1.get()
        })


        
    schooldatabase.commit()

    schooldatabase.close()



            



    first1.delete(0, END)
    grade1.delete(0, END)
    age1.delete(0, END)
    last1.delete(0, END)




def query():
    global record, print_records, records


    schooldatabase = sqlite3.connect('SchoolDatabase.db')

    cursor = schooldatabase.cursor()

    cursor.execute("SELECT *, oid FROM studentd")
    print_records = ''


    records = cursor.fetchall()
 
    for record in records:
        print_records += str(record[0]) + ''+ str(record[3])+ ' Grade:' +str(record[2])+ " Age:" +str(record[1])+' '+ ',ID: '+str(record[4])+ "\n"



    schooldatabase.commit()

    schooldatabase.close()

    global_label = Label(root, text= print_records,pady=20, padx=30, font=Roman)
    global_label.grid(row=2, column=3)
"""
    for record in records:
        if first1.get() == str(record[0]):
            if last1.get() == str(record[3]):
                messagebox.showerror("Hello", 'HELLo')
"""



 


def delete():
    schooldatabase = sqlite3.connect('SchoolDatabase.db')

    cursor = schooldatabase.cursor()


    cursor.execute("DELETE FROM studentd WHERE oid=" +e.get())


    e.delete(0, END)

    schooldatabase.commit()

    schooldatabase.close()







global_students = Label(root, text='                    Global Students                ',padx=30, pady=20, bg='hot pink', borderwidth=5, font=("Helvetica Neue",25))
global_students.grid(row=0, column=3)

schooldatabase.commit()

schooldatabase.close()



frame = LabelFrame(root, padx=50, pady=50, text="This my frame")
frame.grid(row=4, column=1)



root.title('Home Page of School Application')
root.geometry("1100x600")
root.resizable(False, False)
root.mainloop()
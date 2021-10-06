from flask import Blueprint, render_template, request, flash
from flask_mysqldb import MySQL
import mysql.connector

mydb = mysql.connector.connect(
       host = "127.0.0.1",
       user = "root",
       password = "izakme123",
       database =  "ssis_website",
       )
my_cursor = mydb.cursor()

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])

def register():
    my_cursor.execute("SELECT course_code FROM course")
    cour_c = my_cursor.fetchall()
    mydb.commit()

    my_cursor.execute("SELECT course.college_code FROM ssis_website.course")
    cor_coll = my_cursor.fetchall()

    if request.method == 'POST':

        my_cursor.execute("SELECT * FROM course")
        stud_cor = my_cursor.fetchall()
        mydb.commit()

        fname = request.form.get('firstname')
        lname = request.form.get('lastname')
        idnum = request.form.get('idnum')
        course = request.form.get('course')
        yrlvl = request.form.get('yrlvl')
        gender = request.form.get('gender')

        print(course)
        print(yrlvl)
        print(gender)

        if len(fname) == 0:
            flash('Please Complete the Name', category='error')
        elif len(lname) == 0:
            flash('Please Complete the Name', category='error')
        elif len(idnum) == 0:
            flash('Please Input an ID Number', category='error')
        elif course == None:
            flash('Please Select Course', category='error')
        elif yrlvl == None:
            flash('Please Select Year Level', category='error')
        elif gender == None:
            flash('Please Select Gender', category='error')
        else:
            my_cursor.execute("INSERT INTO students(id_number, first_name, last_name, gender, course_code, year) "
                              "VALUES(%s, %s, %s, %s, %s, %s)", (idnum, fname, lname, gender, course, yrlvl))
            mydb.commit()

            flash('Student Successfully Register', category='success')

    return render_template("registerstudent.html", cour_c=cour_c, cor_coll=cor_coll)
mydb.commit()


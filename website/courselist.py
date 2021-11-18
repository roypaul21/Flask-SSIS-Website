from flask import Blueprint, render_template, request, flash, url_for
import mysql.connector
from flask_mysqldb import MySQL
import os
from decouple import config

host = config('HOST', default='')
password = config('PASSWORD')
user = config('USER')
db = config('DATABASE')

mydb = mysql.connector.connect(
       host = host,
       user = user,
       password = password,
       database = db
       )

my_cursor = mydb.cursor()

course = Blueprint('course', __name__)

@course.route('/course')
def course_list():
    my_cursor.execute("""SELECT course.course_code, course.course_name, college.college_name, college.college_code FROM ssis_website.college
                          INNER JOIN ssis_website.course ON course.college_code = college.college_code""")
    cor_list = my_cursor.fetchall()

    my_cursor.execute("SELECT course.course_code FROM ssis_website.course")
    cour_c = my_cursor.fetchall()

    my_cursor.execute("SELECT college.college_code FROM ssis_website.college")
    cor_coll = my_cursor.fetchall()

    mydb.commit()

    return render_template("courses.html", cor_list = cor_list, cor_coll=cor_coll, cour_c=cour_c)

@course.route('/add-course', methods=['GET', 'POST'])
def add_course():

    my_cursor.execute("SELECT college_code FROM college")
    cor_coll = my_cursor.fetchall()
    mydb.commit()

    my_cursor.execute("SELECT course.course_code FROM ssis_website.course")
    cour_c = my_cursor.fetchall()


    if request.method == 'POST':

        corcode = request.form.get('course-code')
        corname = request.form.get('course-name')
        colcode = request.form.get('college-code')

        print(colcode)


        if len(corcode) < 1:
            flash('Please Input Course Code', category='error')
        elif len(corname) < 1:
            flash('Please Input Course Name', category='error')
        elif colcode == "--Select College":
            flash('Please Select College', category='error')
        else:
            my_cursor.execute("INSERT INTO course(course_code, course_name, college_code) VALUES(%s, %s, %s)", (corcode, corname, colcode))
            mydb.commit()
            flash('Course Successfully Register', category='success')

    return render_template("addcourse.html", cour_c=cour_c, cor_coll=cor_coll, )
mydb.commit()

@course.route('/updated_course', methods=['GET', 'POST'])
def updated_course():
    my_cursor.execute("""SELECT course.course_code, course.course_name, college.college_name, college.college_code FROM ssis_website.college
                              INNER JOIN ssis_website.course ON course.college_code = college.college_code""")
    cor_list = my_cursor.fetchall()

    my_cursor.execute("SELECT college_code FROM college")
    cor_coll = my_cursor.fetchall()
    mydb.commit()

    my_cursor.execute("SELECT course.course_code FROM ssis_website.course")
    cour_c = my_cursor.fetchall()

    if request.method =='POST':
        cc=request.form.get('course-code')
        cn=request.form.get('course-name')
        clc=request.form.get('college-code')

        if len(cn) == 0:
            flash("Please Input Course Name", category='error')
        elif clc == None:
            flash("Please Select College", category='error')
        else:
            my_cursor.execute("UPDATE ssis_website.course SET course.course_code=%s, course.course_name=%s, course.college_code=%s WHERE course.course_code=%s", (cc, cn, clc, cc))
            flash("Course Successfully Updated",category='success')
            mydb.commit()

        return render_template('courses.html', cour_c=cour_c, cor_coll=cor_coll, cor_list=cor_list)
mydb.commit()

@course.route('/delete_course', methods=['GET', 'POST'])
def delete_course():
    my_cursor.execute("""SELECT course.course_code, course.course_name, college.college_name, college.college_code FROM ssis_website.college
                                 INNER JOIN ssis_website.course ON course.college_code = college.college_code""")
    cor_list = my_cursor.fetchall()
    mydb.commit()

    my_cursor.execute("SELECT college_code FROM college")
    cor_coll = my_cursor.fetchall()
    mydb.commit()

    my_cursor.execute("SELECT course.course_code FROM ssis_website.course")
    cour_c = my_cursor.fetchall()

    mydb.commit()

    if request.method == 'POST':
       cc = request.form.get('course-code')
       print(cc)
       my_cursor.execute("DELETE FROM ssis_website.course WHERE course.course_code=%s", (request.form.get('course-code'),))

       flash("Course Successfully Remove", category='success')
       mydb.commit()


    return render_template("courses.html", cour_c=cour_c, cor_coll=cor_coll, cor_list=cor_list)
mydb.commit()



from flask import Blueprint, render_template, request, flash
from flask_mysqldb import MySQL
import os
from website import mysql


students = Blueprint('students', __name__)

@students.route('/students')
def record():
    my_cursor = mysql.connection.cursor()
    my_cursor.execute("""SELECT students.id_number, students.first_name, students.last_name, students.gender, course.course_name, students.year, course.course_code FROM ssis_website.course
                             INNER JOIN ssis_website.students ON students.course_code = course.course_code""")
    student_list = my_cursor.fetchall()

    my_cursor.execute("SELECT course.college_code FROM ssis_website.course")
    cor_coll = my_cursor.fetchall()


    my_cursor.execute("SELECT course.course_code FROM ssis_website.course")
    cour_c = my_cursor.fetchall()
    mysql.connection.commit()

    return render_template("studentrecord.html", records=student_list, cour_c=cour_c, cor_coll=cor_coll)

@students.route('/updated_students', methods=['GET', 'POST'])
def updated_students():
    my_cursor = mysql.connection.cursor()
    my_cursor.execute("SELECT course.college_code FROM ssis_website.course")
    cor_coll = my_cursor.fetchall()

    my_cursor.execute("SELECT course.course_code FROM ssis_website.course")
    cour_c = my_cursor.fetchall()
    mysql.connection.commit()

    if request.method == 'POST':
        idn = request.form.get('idnum')
        fname = request.form.get('first-name')
        lname = request.form.get('last-name')
        gender = request.form.get('gender')
        courses = request.form.get('course-code')
        yrlvl = request.form.get('yrlvl')


        if len(fname) == 0:
            flash('Please Complete the Name', category='error')
        elif len(lname) == 0:
            flash('Please Complete the Name', category='error')
        elif courses == None:
            flash('Please Select Course', category='error')
        elif yrlvl == None:
            flash('Please Select Year Level', category='error')
        elif gender == None:
            flash('Please Select Gender', category='error')
        else:
            my_cursor.execute("UPDATE ssis_website.students SET students.first_name=%s, students.last_name=%s, students.gender=%s, students.course_code=%s, students.year=%s WHERE students.id_number=%s",
                (fname, lname, gender, courses, yrlvl, idn))
            mysql.connection.commit()

            flash("Student Successfully Updated", category='success')


    my_cursor.execute("""SELECT students.id_number, students.first_name, students.last_name, students.gender, course.course_name, students.year, course.course_code FROM ssis_website.course
                                               INNER JOIN ssis_website.students ON students.course_code = course.course_code""")
    student_list = my_cursor.fetchall()

    return render_template("studentrecord.html", records=student_list, cour_c=cour_c, cor_coll=cor_coll)


@students.route('/delete_students', methods=['GET', 'POST'])
def delete_students():
    my_cursor = mysql.connection.cursor()
    my_cursor.execute("SELECT course.college_code FROM ssis_website.course")
    cor_coll = my_cursor.fetchall()

    my_cursor.execute("SELECT course.course_code FROM ssis_website.course")
    cour_c = my_cursor.fetchall()
    mysql.connection.commit()

    if request.method == 'POST':
        idn = request.form.get('idnum')

        print(idn)
        my_cursor.execute("DELETE FROM ssis_website.students WHERE students.id_number=%s",
                          (request.form.get('idnum'),))
        mysql.connection.commit()
        flash("Student Successfully Remove", category='success')

    my_cursor.execute("""SELECT students.id_number, students.first_name, students.last_name, students.gender, course.course_name, students.year, course.course_code FROM ssis_website.course
                                        INNER JOIN ssis_website.students ON students.course_code = course.course_code""")
    student_list = my_cursor.fetchall()

    return render_template("studentrecord.html", records=student_list, cour_c=cour_c, cor_coll=cor_coll)




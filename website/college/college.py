from flask import Blueprint, render_template, request, flash
from flask_mysqldb import MySQL
import os
from website import mysql


college = Blueprint('college', __name__)

@college.route('/college')
def collegelist():
    my_cursor = mysql.connection.cursor()
    my_cursor.execute("SELECT course.course_code FROM ssis_website.course")
    cour_c = my_cursor.fetchall()

    my_cursor.execute("SELECT college_code, college_name FROM college")
    cor_coll = my_cursor.fetchall()
    mysql.connection.commit()

    return render_template("colleges.html", cor_coll = cor_coll, cour_c=cour_c)

@college.route('/add-college', methods=['GET', 'POST'])
def add_college():
    my_cursor = mysql.connection.cursor()
    my_cursor.execute("SELECT course.course_code FROM ssis_website.course")
    cour_c = my_cursor.fetchall()

    my_cursor.execute("SELECT college_code FROM college")
    cor_coll = my_cursor.fetchall()
    mysql.connection.commit()

    if request.method == 'POST':
        colcode = request.form.get('college-code')
        colname = request.form.get('college-name')

        if len(colcode) < 1:
            flash("Please Input College Code", category="error")
        elif len(colname) == 0:
            flash("Please Input College Name", category="error")
        else:
            my_cursor.execute("INSERT INTO college(college_code, college_name) VALUES(%s, %s)",(colcode, colname))
            mysql.connection.commit()

            flash('College Successfully Register', category='success')

    return render_template("addcollege.html",  cor_coll = cor_coll, cour_c=cour_c)


@college.route('/update-college', methods=['GET', 'POST'])
def update_college():
    my_cursor = mysql.connection.cursor()
    my_cursor.execute("SELECT course.course_code FROM ssis_website.course")
    cour_c = my_cursor.fetchall()

    if request.method == 'POST':
        cn = request.form.get('college-name')
        cc = request.form.get('college-code')

        if len(cn) == 0:
            flash("Please Insert College Name", category='error')

        elif len(cc) == 0:
            flash("Please Insert College Name", category='error')

        else:
            flash("College Name Successfully Updated", category='success')
            my_cursor.execute("UPDATE ssis_website.college SET college_code=%s, college_name=%s WHERE college_code=%s", (cc, cn, cc))
            mysql.connection.commit()

            my_cursor.execute("SELECT college_code, college_name  FROM college")
            cor_coll = my_cursor.fetchall()

            return render_template("colleges.html", cor_coll=cor_coll, cour_c=cour_c)



@college.route('/delete-college', methods=['GET', 'POST'])
def delete_college():
    my_cursor = mysql.connection.cursor()
    my_cursor.execute("SELECT course.course_code FROM ssis_website.course")
    cour_c = my_cursor.fetchall()

    if request.method == 'POST':
        cc = request.form.get('college-code')

        my_cursor.execute("DELETE FROM ssis_website.college WHERE college.college_code=%s",
                          (request.form.get('college-code'),))
        mysql.connection.commit()

        flash("College Successfully Remove", category='success')
        my_cursor.execute("SELECT college_code, college_name FROM college")
        cor_coll = my_cursor.fetchall()

        return render_template("colleges.html", cor_coll=cor_coll, cour_c=cour_c)
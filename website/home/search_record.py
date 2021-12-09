from flask import Blueprint, render_template, request, flash
from flask_mysqldb import MySQL
import os
from website import mysql


search = Blueprint('search_record', __name__)

@search.route('/search_record', methods=['GET', 'POST'])
def search_record():
    global search_std
    my_cursor = mysql.connection.cursor()

    my_cursor.execute("SELECT course.course_code FROM ssis_website.course")
    cour_c = my_cursor.fetchall()

    my_cursor.execute("SELECT college_code FROM college")
    cor_coll = my_cursor.fetchall()
    mysql.connection.commit()

    if request.method == 'POST':
        id_nm = request.form.get('search-idnum')
        fnm = request.form.get('search-fname')
        lnm = str(request.form.get('search-lname'))
        gndr = str(request.form.get('drpgender'))
        crs = str(request.form.get('drpcourse'))
        clg = str(request.form.get('drpcollege-code'))
        yrl = str(request.form.get('drpyrlvl'))



        if len(id_nm) == 0 and len(fnm) == 0 and len(lnm) ==0 and gndr == '' and crs == '' and clg == '' and yrl == '':
               flash("Please Enter ID Number to Search", category='error')

        else:
               my_cursor.execute("""SELECT students.id_number,students.first_name,students.last_name,students.gender, course.course_name, students.year, students.course_code FROM ssis_website.students 
                                    INNER JOIN ssis_website.course ON course.course_code = students.course_code
                                    INNER JOIN ssis_website.college ON college.college_code = course.college_code
                                    WHERE students.id_number LIKE %s AND students.first_name LIKE %s AND students.last_name LIKE %s 
                                    AND students.gender LIKE %s AND students.course_code LIKE %s AND course.college_code LIKE %s AND students.year LIKE %s;""",
                                    ("%"+str(request.form.get('search-idnum')+"%"),("%"+(request.form.get('search-fname'))+"%"),("%"+lnm+"%"),("%"+gndr+"%"),("%"+crs+"%"),("%"+clg+"%"),("%"+yrl+"%")))

               search_std = my_cursor.fetchall()
               print(search_std)
               mysql.connection.commit()
               if not search_std:
                   flash("No Student Recorded According to your Search Fields (Search Again)", category='error')

               return render_template("search_record.html", cour_c=cour_c, cor_coll=cor_coll, search_std=search_std)
        return render_template("search_record.html", cour_c=cour_c, cor_coll=cor_coll, search_std=search_std)


@search.route('/delete_student', methods=['GET', 'POST'])
def delete_student():
    my_cursor = mysql.connection.cursor()

    my_cursor.execute("SELECT course.course_code FROM ssis_website.course")
    cour_c = my_cursor.fetchall()

    my_cursor.execute("SELECT college_code FROM college")
    cor_coll = my_cursor.fetchall()
    mysql.connection.commit()

    if request.method == 'POST':
        '''
        my_cursor.execute("""SELECT students.id_number,students.first_name,students.last_name,students.gender, course.course_name, students.year FROM ssis_website.students 
                                                           INNER JOIN ssis_website.course ON course.course_code = students.course_code
                                                           INNER JOIN ssis_website.college ON college.college_code = course.college_code
                                                           WHERE students.id_number LIKE %s """, (("%" + id_nm + "%"),))

        search_std = my_cursor.fetchall()
        '''

        idn = request.form.get('idnum')

        print(idn)
        my_cursor.execute("DELETE FROM ssis_website.students WHERE students.id_number=%s",
                          (request.form.get('idnum'),))

        flash("Student Successfully Remove", category='success')
        mysql.connection.commit()

        return render_template("search_record.html", cour_c=cour_c, cor_coll=cor_coll)


@search.route('/update_student', methods=['GET', 'POST'])
def update_student():
    if request.method == 'POST':
        my_cursor = mysql.connection.cursor()

        my_cursor.execute("SELECT course.course_code FROM ssis_website.course")
        cour_c = my_cursor.fetchall()

        my_cursor.execute("SELECT college_code FROM college")
        cor_coll = my_cursor.fetchall()
        mysql.connection.commit()

        idn = request.form.get('idnum')
        fname = request.form.get('first-name')
        lname = request.form.get('last-name')
        gender = request.form.get('gender')
        courses = request.form.get('course-code')
        yrlvl = request.form.get('yrlvl')
        '''
        my_cursor.execute("""SELECT students.id_number,students.first_name,students.last_name,students.gender, course.course_name, students.year, students.course_code FROM ssis_website.students 
                                                    INNER JOIN ssis_website.course ON course.course_code = students.course_code
                                                    INNER JOIN ssis_website.college ON college.college_code = course.college_code
                                                    WHERE students.id_number LIKE %s """, (("%" + id_nm + "%"),))


        search_std = my_cursor.fetchall()
        '''

        print(search_std)

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
            my_cursor.execute(
                "UPDATE ssis_website.students SET students.first_name=%s, students.last_name=%s, students.gender=%s, students.course_code=%s, students.year=%s WHERE students.id_number=%s",
                (fname, lname, gender, courses, yrlvl, idn))

            flash("Student Successfully Updated", category='success')
            mysql.connection.commit()

        return render_template("search_record.html", search_std = search_std, cour_c=cour_c, cor_coll=cor_coll)

    return render_template("search_record.html", search_std = search_std, cour_c=cour_c, cor_coll=cor_coll)



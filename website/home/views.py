from flask import Blueprint, render_template, request, flash
from flask_mysqldb import MySQL
import os
from website import mysql


views = Blueprint('views', __name__)

@views.route('/')
def home():
    my_cursor = mysql.connection.cursor()

    my_cursor.execute("SELECT course.course_code FROM ssis_website.course")
    cour_c = my_cursor.fetchall()

    my_cursor.execute("SELECT college_code FROM college")
    cor_coll = my_cursor.fetchall()
    mysql.connection.commit()

    return render_template("home.html", cour_c=cour_c, cor_coll=cor_coll)

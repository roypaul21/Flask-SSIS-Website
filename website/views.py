from flask import Blueprint, render_template, request, flash, url_for
from flask_mysqldb import MySQL
import mysql.connector
import os
from .config import HOST, USER, DATABASE, PASSWORD

mydb = mysql.connector.connect(
       host = HOST,
       user = USER,
       password = PASSWORD,
       database = DATABASE
       )

my_cursor = mydb.cursor()

views = Blueprint('views', __name__)

@views.route('/')
def home():
    my_cursor.execute("SELECT course.course_code FROM ssis_website.course")
    cour_c = my_cursor.fetchall()

    my_cursor.execute("SELECT college_code FROM college")
    cor_coll = my_cursor.fetchall()
    mydb.commit()

    return render_template("home.html", cour_c=cour_c, cor_coll=cor_coll)

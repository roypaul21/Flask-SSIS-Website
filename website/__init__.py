from flask import Flask
from flask_mysqldb import MySQL
from flask_mysql_connector import MySQL
from config import HOST, USER, DATABASE, PASSWORD, SECRET_KEY, CLOUD_NAME, API_KEY, API_SECRET
import cloudinary
mysql = MySQL()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        MYSQL_HOST=HOST,
        MYSQL_DATABASE=DATABASE,
        MYSQL_USER=USER,
        MYSQL_PASSWORD=PASSWORD,
    )

    cloudinary.config(
        cloud_name=CLOUD_NAME,
        api_key=API_KEY,
        api_secret=API_SECRET,
    )

    mysql.init_app(app)

    from .home.views import views
    from .student.auth import auth
    from .student.studentlist import students
    from .course.courselist import course
    from .college.college import college
    from .home.search_record import search

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(students, url_prefix='/')
    app.register_blueprint(course, url_prefix='/')
    app.register_blueprint(college, url_prefix='/')
    app.register_blueprint(search, url_prefix='/')

    return app
from flask import Flask
from flask_mysqldb import MySQL



def ssis_app():
    app = Flask(__name__)


    app.config['SECRET_KEY'] = 'ssis'

    
    from .views import views
    from .auth import auth
    from .studentlist import students
    from .courselist import course
    from .college import college
    from .search_record import search

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(students, url_prefix='/')
    app.register_blueprint(course, url_prefix='/')
    app.register_blueprint(college, url_prefix='/')
    app.register_blueprint(search, url_prefix='/')

    return app
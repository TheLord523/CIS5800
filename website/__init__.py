from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
DB_NAME = "database.db"
#migrate = Migrate(app, db)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'yeet'
    #SQL Alchemy database is stored in this location. f-strings are a new and improved way to format strings
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #Takes the database that we defined in line 4 and says this is the app we're gonna use 
    #with this database
    db.init_app(app)
    migrate = Migrate(app, db)

    #get blueprints imported
    from .views import views
    from .auth import auth
    #the url prefix is saying all of the URLS that are stored
    #insdie of these blueprint files, how do we access them?
    #Do we have to go to the prefix specifically?
    # / means no prefix
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    #create_database(app)
    #create_all() doesn't support the app argument no more
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) #look for the primary key and check if it's whatever we pass
    
    return app 

#check if database exists, and if it doesn't, create it.
#def create_database(app):
    #if not path.exists('website/' + DB_NAME):
        #db.create_all(app=app)
        #db.create_all(app)
        #print('Created Database!')
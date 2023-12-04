# Some set up for the application 

import os
from flask import Flask
from flaskext.mysql import MySQL

# create a MySQL object that we will use in other parts of the API
db = MySQL()

def create_app():
    app = Flask(__name__)
    
    # secret key that will be used for securely signing the session 
    # cookie and can be used for any other security related needs by 
    # extensions or your application
    app.config['SECRET_KEY'] = 'someCrazyS3cR3T!Key.!'

    # these are for the DB object to be able to connect to MySQL. 
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = open(os.path.join("..", "secrets", "db_root_password.txt")).readline().strip()
    app.config['MYSQL_DATABASE_HOST'] = 'db'
    app.config['MYSQL_DATABASE_PORT'] = 3306
    app.config['MYSQL_DATABASE_DB'] = 'taskwiz'  # Change this to your DB name

    # Initialize the database object with the settings above. 
    db.init_app(app)
    
    # Add the default route
    # Can be accessed from a web browser
    # http://ip_address:port/
    # Example: localhost:8001
    @app.route("/")
    def welcome():
        return "<h1>Welcome to the 3200 boilerplate app</h1>"
    
    @app.route("/test", methods=['GET'])
    def test():
        return "<h1>Test</h1>"

    # Import the various Blueprint Objects    
    from src.tasks.tasks import tasks
    from src.folders.folders import folders
    from src.job_applications.job_applications import job_apps
    from src.documents.documents import documents
    from src.messages.messages import messages
    from src.groups.groups import groups

    # Register the routes from each Blueprint with the app object
    # and give a url prefix to each
    app.register_blueprint(tasks,       url_prefix='/t')
    app.register_blueprint(folders,     url_prefix='/f')
    app.register_blueprint(job_apps,    url_prefix='/j')
    app.register_blueprint(documents,   url_prefix='/d')
    app.register_blueprint(messages,    url_prefix='/m')
    app.register_blueprint(groups,      url_prefix='/g')

    # Don't forget to return the app object
    return app
from flask import Blueprint, request, jsonify, make_response
from src import db


job_apps = Blueprint('job_apps', __name__)

# Get all job applications from the DB or create a new job application and add it to the DB
@job_apps.route('/job_apps', methods=['GET', 'POST'])
def request_job_apps():
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from JobApplication'
        cursor.execute(query)
        row_headers = [x[0] for x in cursor.description]
        json_data = []
        theData = cursor.fetchall()
        for row in theData:
            json_data.append(dict(zip(row_headers, row)))
        the_response = make_response(jsonify(json_data))
        the_response.status_code = 200
        the_response.mimetype = 'application/json'
        return the_response
    elif request.method == 'POST':
        the_data = request.json
        title = the_data['JobTitle']
        company = the_data['CompanyName']
        content = the_data['Content']
        userID = the_data['UserID']
        folderID = the_data['FolderID']
        query = 'insert into JopApplication (JobTitle, CompanyName, Content, UserID, FolderID) values ("{0}", "{1}", "{2}", {3}, {4})'.format(title, company, content, userID, folderID)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"

# Get details regarding a specific job application, update an application, or delete an application
@job_apps.route('/job_apps/<appID>', methods=['GET', 'PUT', 'DELETE'])
def request_job_app(appID):
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from JobApplication where ApplicationID = {0}'.format(appID)
        cursor.execute(query)
        row_headers = [x[0] for x in cursor.description]
        json_data = []
        theData = cursor.fetchall()
        for row in theData:
            json_data.append(dict(zip(row_headers, row)))
        the_response = make_response(jsonify(json_data))
        the_response.status_code = 200
        the_response.mimetype = 'application/json'
        return the_response
    elif request.method == 'PUT':
        the_data = request.json
        title = the_data['JobTitle']
        company = the_data['CompanyName']
        content = the_data['Content']
        userID = the_data['UserID']
        folderID = the_data['FolderID']
        query = 'update JopApplication set JobTitle = "{0}", CompanyName = "{1}", Content = "{2}", UserID = {3}, FolderID = {4} where ApplicationID = {5}'.format(title, company, content, userID, folderID, appID)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"
    elif request.method == 'DELETE':
        query = 'delete from JobApplication where ApplicationID = {0}'.format(appID)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"

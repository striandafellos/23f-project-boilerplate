from flask import Blueprint, request, jsonify, make_response
from src import db


classes = Blueprint('classes', __name__)

# Get all classes from the DB or create a new class and add it to the DB
@classes.route('/classes', methods=['GET', 'POST'])
def request_classes():
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from Class'
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
        title = the_data['Title']
        query = 'insert into Class (Title) values ("{0}")'.format(title)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"

# Get class details for a specific class, update a class, or delete a class
@classes.route('/classes/<classID>', methods=['GET', 'DELETE'])
def request_class(classID):
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from Class where ClassID = {0}'.format(classID)
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
    elif request.method == 'DELETE':
        query = 'delete from Class where ClassID = {0}'.format(classID)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"

from flask import Blueprint, request, jsonify, make_response
import json
from src import db


tasks = Blueprint('tasks', __name__)

# Get all files from the DB
@tasks.route('/tasks', methods=['GET'])
def get_tasks():
    cursor = db.get_db().cursor()
    query = 'select * from Task'
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

# Get folder details for folder with particular folderID
@tasks.route('/tasks/<TaskID>', methods=['GET'])
def get_task(taskID):
    cursor = db.get_db().cursor()
    query = 'select * from Task where TaskID = {0}'.format(taskID)
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
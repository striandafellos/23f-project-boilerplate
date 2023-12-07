from flask import Blueprint, request, jsonify, make_response
from src import db


tasks = Blueprint('tasks', __name__)

# Get all tasks from the DB or create a new task and add it to the DB
@tasks.route('/tasks', methods=['GET', 'POST'])
def request_tasks():
    if request.method == 'GET':
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
    elif request.method == 'POST':
        the_data = request.json
        title = the_data['Title']
        desc = the_data['TaskDescription']
        due = the_data['DueDate']
        completed = the_data['Completed']
        userID = the_data['UserID']
        plannerID = the_data['PlannerID']
        calendarID = the_data['CalendarID']
        query = 'insert into Task (Title, TaskDescription, DueDate, Completed, UserID, PlannerID, CalendarID) values ("{0}", "{1}", "{2}", {3}, {4}, {5}, {6})'.format(title, desc, due, completed, userID, plannerID, calendarID)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"

# Get task details for a specific task, update a task, or delete a task
@tasks.route('/tasks/<taskID>', methods=['GET', 'PUT', 'DELETE'])
def request_task(taskID):
    if request.method == 'GET':
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
    elif request.method == 'PUT':
        the_data = request.json
        title = the_data['Title']
        desc = the_data['TaskDescription']
        due = the_data['DueDate']
        completed = the_data['Completed']
        userID = the_data['UserID']
        plannerID = the_data['PlannerID']
        calendarID = the_data['CalendarID']
        query = 'update Task set Title = "{0}", TaskDescription = "{1}", DueDate = "{2}", Completed = {3}, UserID = {4}, PlannerID = {5}, CalendarID = {6} where TaskID = {7}'.format(title, desc, due, completed, userID, plannerID, calendarID, taskID)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"
    elif request.method == 'DELETE':
        query = 'delete from Task where TaskID = {0}'.format(taskID)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"

# Query all tasks by title
@tasks.route('/tasks/title/<title>', methods=['GET'])
def request_tasks_by_title(title):
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from Task where Title like {0}'.format(title)
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

# Get all tasks created by a specific user
@tasks.route('/tasks/uid/<uid>', methods=['GET'])
def request_tasks_by_user(uid):
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from Task where UserID = {0}'.format(uid)
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
from flask import Blueprint, request, jsonify, make_response
from src import db


planners = Blueprint('planners', __name__)

# Get all planners from the DB or create a new planner and add it to the DB
@planners.route('/planners', methods=['GET', 'POST'])
def request_planners():
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from Planner'
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
        planner_name = the_data['PlannerName']
        creator_id = the_data['UserID']
        query = 'insert into Planner (PlannerName, UserID) values ("{0}", {1})'.format(planner_name, creator_id)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"

# Get planner details for a specific planner, update a planner, or delete a planner
@planners.route('/planners/<plannerID>', methods=['GET', 'PUT', 'DELETE'])
def request_folder(plannerID):
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from Planner where PlannerID = {0}'.format(plannerID)
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
        planner_name = the_data['PlannerName']
        creator_id = the_data['UserID']
        query = 'update Planner set PlannerName = "{0}", UserID = {1} where PlannerID = {2}'.format(planner_name, creator_id, plannerID)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"
    elif request.method == 'DELETE':
        query = 'delete from Planner where PlannerID = {0}'.format(plannerID)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"

# Query all planners by name
@planners.route('/planners/name/<name>', methods=['GET'])
def request_planners_by_name(name):
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from Planner where PlannerName like {0}'.format(name)
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

# Get all planners created by a specific user
@planners.route('/planners/uid/<uid>', methods=['GET'])
def request_planners_by_user(uid):
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from Planner where UserID = {0}'.format(uid)
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

# Get all tasks or events associated with a specific planner
@planners.route('/planners/<plannerID>/items', methods=['GET'])
def request_planner_items(plannerID):
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        task_query = 'select * from Task where PlannerID = {0}'.format(plannerID)
        cursor.execute(task_query)
        row_headers = [x[0] for x in cursor.description]
        json_data = []
        task_data = cursor.fetchall()
        for row in task_data:
            json_data.append(dict(zip(row_headers, row)))
        event_query = 'select * from Event where PlannerID = {0}'.format(plannerID)
        cursor.execute(event_query)
        row_headers = [x[0] for x in cursor.description]
        event_data = cursor.fetchall()
        for row in event_data:
            json_data.append(dict(zip(row_headers, row)))
        the_response = make_response(jsonify(json_data))
        the_response.status_code = 200
        the_response.mimetype = 'application/json'
        return the_response

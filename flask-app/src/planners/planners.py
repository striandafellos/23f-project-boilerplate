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

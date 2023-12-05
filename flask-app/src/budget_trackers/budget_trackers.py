from flask import Blueprint, request, jsonify, make_response
from src import db


budget_trackers = Blueprint('budget_trackers', __name__)

# Get all budget trackers from the DB or create a new budget tracker and add it to the DB
@budget_trackers.route('/budget_trackers', methods=['GET', 'POST'])
def request_budget_trackers():
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from BudgetTracker'
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
        name = the_data['BudgetTrackerName']
        creator_id = the_data['UserID']
        query = 'insert into BudgetTracker (BudgetTrackerName, UserID) values ("{0}", {1})'.format(name, creator_id)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"
    
# Get budget tracker details for a specific tracker, update a tracker, or delete a tracker
@budget_trackers.route('/budget_trackers/<budgetID>', methods=['GET', 'PUT', 'DELETE'])
def request_budget_tracker(budgetID):
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from BudgetTracker where BudgetTrackerID = {0}'.format(budgetID)
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
        name = the_data['BudgetTrackerName']
        creator_id = the_data['UserID']
        query = 'update BudgetTracker set BudgetTrackerName = "{0}", UserID = {1} where BudgetTrackerID = {2}'.format(name, creator_id, budgetID)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"
    elif request.method == 'DELETE':
        query = 'delete from BudgetTracker where BudgetTrackerID = {0}'.format(budgetID)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"
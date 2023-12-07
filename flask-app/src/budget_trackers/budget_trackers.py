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

# Query all budget trackers by name
@budget_trackers.route('/budget_trackers/name/<name>', methods=['GET'])
def request_budget_trackers_by_name(name):
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from BudgetTracker where BudgetTrackerName like {0}'.format(name)
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

# Get all budget trackers created by a specific user
@budget_trackers.route('/budget_trackers/uid/<uid>', methods=['GET'])
def request_budget_trackers_by_user(uid):
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from BudgetTracker where UserID = {0}'.format(uid)
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

# Get all budget items from a specific tracker or add an item to a specific tracker
@budget_trackers.route('/budget_trackers/budget_items/<budgetID>', methods=['GET', 'POST'])
def request_budget_items(budgetID):
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from BudgetItem where BudgetTrackerID = {0}'.format(budgetID)
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
        name = the_data['ItemName']
        desc = the_data['ItemDescription']
        amount = the_data['ItemAmount']
        tracker_id = the_data['BudgetTrackerID']
        query = 'insert into BudgetItem (ItemName, ItemDescription, ItemAmount, BudgetTrackerID) values ("{0}", "{1}", {2}, {3})'.format(name, desc, amount, tracker_id)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"

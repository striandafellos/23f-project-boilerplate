from flask import Blueprint, request, jsonify, make_response
from src import db


budget_tracker = Blueprint('budget_tracker', __name__)

# Get all folders from the DB or create a new folder and add it to the DB
@budget_tracker.route('/budget_tracker', methods=['GET', 'POST'])
def request_budget_tracker():
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
        title = the_data['Title']
        creator_id = the_data['UserID']
        query = 'insert into BudgetTracker (Title, UserID) values ("{0}", {1})'.format(title, creator_id)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"
    
# Get folder details for a specific folder, update a folder, or delete a folder
@budget_tracker.route('/budget_tracker/<budgetID>', methods=['GET', 'PUT', 'DELETE'])
def request_folder(budgetID):
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from BudgetTracker where budgetID = {0}'.format(budgetID)
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
        creator_id = the_data['UserID']
        query = 'update BudgetTracker set Title = "{0}", UserID = {1} where BudgetID = {2}'.format(title, creator_id, budgetID)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"
    elif request.method == 'DELETE':
        query = 'delete from BudgetTracker where budgetID = {0}'.format(budgetID)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"
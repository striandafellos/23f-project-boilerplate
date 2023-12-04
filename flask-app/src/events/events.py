from flask import Blueprint, request, jsonify, make_response
from src import db


events = Blueprint('events', __name__)

# Get all events from the DB or create a new event and add it to the DB
@events.route('/events', methods=['GET', 'POST'])
def request_events():
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from Event'
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
        details = the_data['Details']
        date = the_data['EventDate']
        userID = the_data['UserID']
        plannerID = the_data['PlannerID']
        calendarID = the_data['CalendarID']
        query = 'insert into Event (Title, Details, EventDate, UserID, PlannerID, CalendarID) values ("{0}", "{1}", "{2}", {3}, {4}, {5})'.format(title, details, date, userID, plannerID, calendarID)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"

# Get event details for a specific event, update an event, or delete an event
@events.route('/events/<eventID>', methods=['GET', 'PUT', 'DELETE'])
def request_event(eventID):
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from Event where EventID = {0}'.format(eventID)
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
        details = the_data['Details']
        date = the_data['EventDate']
        userID = the_data['UserID']
        plannerID = the_data['PlannerID']
        calendarID = the_data['CalendarID']
        query = 'update Event set Title = "{0}", Details = "{1}", EventDate = "{2}", UserID = {3}, PlannerID = {4}, CalendarID = {5} where EventID = {6}'.format(title, details, date, userID, plannerID, calendarID, eventID)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"
    elif request.method == 'DELETE':
        query = 'delete from Event where EventID = {0}'.format(eventID)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"

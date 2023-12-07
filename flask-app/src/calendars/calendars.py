from flask import Blueprint, request, jsonify, make_response
from src import db


calendars = Blueprint('calendars', __name__)

# Get all calendars from the DB or create a new calendar and add it to the DB
@calendars.route('/calendars', methods=['GET', 'POST'])
def request_calendars():
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from Calendar'
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
        calendar_name = the_data['CalendarName']
        creator_id = the_data['UserID']
        query = 'insert into Calendar (CalendarName, UserID) values ("{0}", {1})'.format(calendar_name, creator_id)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"

# Get calendar details for a specific calendar, update a calendar, or delete a calendar
@calendars.route('/calendars/<calendarID>', methods=['GET', 'PUT', 'DELETE'])
def request_calendar(calendarID):
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from Calendar where CalendarID = {0}'.format(calendarID)
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
        calendar_name = the_data['CalendarName']
        creator_id = the_data['UserID']
        query = 'update Calendar set CalendarName = "{0}", UserID = {1} where CalendarID = {2}'.format(calendar_name, creator_id, calendarID)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"
    elif request.method == 'DELETE':
        query = 'delete from Calendar where CalendarID = {0}'.format(calendarID)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"

# Query all calendars by name
@calendars.route('/calendars/name/<name>', methods=['GET'])
def request_calendars_by_name(name):
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from Calendar where CalendarName like {0}'.format(name)
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

# Get all calendars created by a specific user
@calendars.route('/calendars/uid/<uid>', methods=['GET'])
def request_calendars_by_user(uid):
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from Calendar where UserID = {0}'.format(uid)
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

# Get all tasks or events associated with a specific calendar
@calendars.route('/calendars/<calendarID>/items', methods=['GET'])
def request_calendar_items(calendarID):
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        task_query = 'select * from Task where CalendarID = {0}'.format(calendarID)
        cursor.execute(task_query)
        row_headers = [x[0] for x in cursor.description]
        json_data = []
        task_data = cursor.fetchall()
        for row in task_data:
            json_data.append(dict(zip(row_headers, row)))
        event_query = 'select * from Event where CalendarID = {0}'.format(calendarID)
        cursor.execute(event_query)
        row_headers = [x[0] for x in cursor.description]
        event_data = cursor.fetchall()
        for row in event_data:
            json_data.append(dict(zip(row_headers, row)))
        the_response = make_response(jsonify(json_data))
        the_response.status_code = 200
        the_response.mimetype = 'application/json'
        return the_response

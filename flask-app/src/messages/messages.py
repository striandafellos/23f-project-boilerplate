from flask import Blueprint, request, jsonify, make_response
from src import db


messages = Blueprint('messages', __name__)

# Get all messages from the DB or create a new message and add it to the DB
@messages.route('/messages', methods=['GET', 'POST'])
def request_messages():
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from Message'
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
        sender_id = the_data['SenderID']
        recipient_id = the_data['RecipientID']
        message_body = the_data['MessageBody']
        date = the_data['DateSent']
        query = 'insert into Message (SenderID, RecipientID, MessageBody, DateSent) values ({0}, {1}, "{2}", "{3}")'.format(sender_id, recipient_id, message_body, date)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"

# Get message details for a specific message, update a message, or delete a message
@messages.route('/messages/<messageID>', methods=['GET', 'DELETE'])
def request_message(messageID):
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from Message where MessageID = {0}'.format(messageID)
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
        query = 'delete from Message where MessageID = {0}'.format(messageID)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"

# Query all messages by sender
@messages.route('/messages/sender/<uid>', methods=['GET'])
def request_messages_by_sender(uid):
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from Message where SenderID = {0}'.format(uid)
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

# Query all messages by recipient
@messages.route('/messages/recipient/<uid>', methods=['GET'])
def request_messages_by_recipient(uid):
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from Message where RecipientID = {0}'.format(uid)
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

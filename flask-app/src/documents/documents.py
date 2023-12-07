from flask import Blueprint, request, jsonify, make_response
from src import db


documents = Blueprint('documents', __name__)

# Get all documents from the DB or create a new document and add it to the DB
@documents.route('/documents', methods=['GET', 'POST'])
def request_documents():
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from Document'
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
        document_name = the_data['DocumentName']
        content = the_data['Content']
        creator_id = the_data['UserID']
        folder_id = the_data['FolderID']
        query = 'insert into Document (DocumentName, Content, UserID, FolderID) values ("{0}", "{1}", {2}, {3})'.format(document_name, content, creator_id, folder_id)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"

# Get document details for a specific document, update a document, or delete a document
@documents.route('/documents/<documentID>', methods=['GET', 'PUT', 'DELETE'])
def request_document(documentID):
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from Document where DocumentID = {0}'.format(documentID)
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
        document_name = the_data['DocumentName']
        content = the_data['Content']
        creator_id = the_data['UserID']
        folder_id = the_data['FolderID']
        query = 'update Document set DocumentName = "{0}", Content = "{1}", UserID = {2}, FolderID = {3} where DocumentID = {4}'.format(document_name, content, creator_id, folder_id, documentID)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"
    elif request.method == 'DELETE':
        query = 'delete from Document where DocumentID = {0}'.format(documentID)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"

# Query all documents by name
@documents.route('/documents/name/<name>', methods=['GET'])
def request_documents_by_name(name):
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from Document where DocumentName like {0}'.format(name)
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

# Get all documents created by a specific user
@documents.route('/documents/uid/<uid>', methods=['GET'])
def request_documents_by_user(uid):
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from Document where UserID = {0}'.format(uid)
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

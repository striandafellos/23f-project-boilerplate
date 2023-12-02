from flask import Blueprint, request, jsonify, make_response
import json
from src import db


folders = Blueprint('folders', __name__)

# Get all files from the DB
@folders.route('/folders', methods=['GET'])
def get_folders():
    cursor = db.get_db().cursor()
    query = 'select * from Folder'
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

# Get folder details for folder with particular folderID
@folders.route('/folders/<folderID>', methods=['GET'])
def get_folder(folderID):
    cursor = db.get_db().cursor()
    query = 'select * from Folder where FolderID = {0}'.format(folderID)
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
from flask import Blueprint, request, jsonify, make_response
import json
from src import db


folders = Blueprint('folders', __name__)

# Get all folders from the DB or create a new folder and add it to the DB
@folders.route('/folders', methods=['GET', 'POST'])
def request_folders():
    if request.method == 'GET':
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
    elif request.method == 'POST':
        the_data = request.json
        folder_name = the_data['FolderName']
        creator_id = the_data['UserID']
        query = 'insert into Folder (FolderName, UserID) values ("{0}", {1})'.format(folder_name, creator_id)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"

# Get folder details for a specific folder, update a folder, or delete a folder
@folders.route('/folders/<folderID>', methods=['GET', 'PUT', 'DELETE'])
def request_folder(folderID):
    if request.method == 'GET':
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
    elif request.method == 'PUT':
        the_data = request.json
        folder_name = the_data['FolderName']
        creator_id = the_data['UserID']
        query = 'update Folder set FolderName = "{0}", UserID = {1} where FolderID = {2}'.format(folder_name, creator_id, folderID)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"
    elif request.method == 'DELETE':
        query = 'delete from Folder where FolderID = {0}'.format(folderID)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"

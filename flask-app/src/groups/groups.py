from flask import Blueprint, request, jsonify, make_response
from src import db


groups = Blueprint('groups', __name__)

# Get all groups from the DB or create a new group
@groups.route('/groups', methods=['GET', 'POST'])
def request_groups():
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from UserGroup'
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
        group_name = the_data['GroupName']
        creator_id = the_data['CreatorID']
        query1 = 'insert into UserGroup (GroupName, CreatorID) values ("{0}", {1})'.format(group_name, creator_id)
        cursor = db.get_db().cursor()
        cursor.execute(query1)
        db.get_db().commit()
        # user who makes a group should automatically be placed into it
        query2 = 'select max(GroupID) as LatestGroup from GroupsAndUsers where UserID = {0}'.format(creator_id)
        cursor.execute(query2)
        row_headers = [x[0] for x in cursor.description]
        json_data = []
        theData = cursor.fetchall()
        for row in theData:
            json_data.append(dict(zip(row_headers, row)))
        the_response = make_response(jsonify(json_data))
        the_response.status_code = 200
        the_response.mimetype = 'application/json'
        group_id = the_response.json[0]['LatestGroup']
        query3 = 'insert into GroupsAndUsers (UserID, GroupID) values ({0}, {1})'.format(creator_id, group_id)
        cursor.execute(query3)
        db.get_db().commit()
        return "Success"

# Get group details for a specific group, update a group, or delete a group
@groups.route('/groups/<groupID>', methods=['GET', 'PUT', 'DELETE'])
def request_folder(groupID):
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        query = 'select * from UserGroup where GroupID = {0}'.format(groupID)
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
        group_name = the_data['GroupName']
        creator_id = the_data['UserID']
        query = 'update UserGroup set GroupName = "{0}", CreatorID = {1} where GroupID = {2}'.format(group_name, creator_id, groupID)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"
    elif request.method == 'DELETE':
        query = 'delete from UserGroup where GroupID = {0}'.format(groupID)
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        return "Success"

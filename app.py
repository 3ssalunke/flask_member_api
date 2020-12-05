from flask import Flask, request, jsonify
from db import database
from functools import wraps

app = Flask(__name__)

api_username = 'admin'
api_password = 'admin123'

def protected(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == api_username and auth.password == api_password:
            return f(*args, **kwargs)
        return jsonify({'message': 'authentication failed'}), 401
    return decorated


@app.route('/member', methods=['GET'])
@protected
def get_members():
    all_members = database.get_allmembers()
    return jsonify(all_members)
    

@app.route('/member/<int:member_id>', methods=['GET'])
@protected
def get_member(member_id):
    member = database.get_member_by_id(member_id)
    return jsonify(member)


@app.route('/member', methods=['POST'])
@protected
def add_member():
    new_member_data = request.get_json()
    name = new_member_data['name']
    email = new_member_data['email']
    level = new_member_data['level']
    database.insert_member(name, email, level)
    member = database.get_member_by_name(name)
    return jsonify(member)


@app.route('/member/<int:member_id>', methods=['PUT', 'PATCH'])
@protected
def update_member(member_id):
    new_member_data = request.get_json()
    name = new_member_data['name']
    email = new_member_data['email']
    level = new_member_data['level']
    database.update_member(name, email, level, member_id)
    member = database.get_member_by_id(member_id)
    return jsonify(member)


@app.route('/member/<int:member_id>', methods=['DELETE'])
@protected
def delete_member(member_id):
    database.delete_member(member_id)
    return jsonify({'message': 'member deleted succefully'})


if __name__ == '__main__':
    app.run(debug=True)
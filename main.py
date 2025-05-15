from flask import Flask, jsonify, request
from config import Config
from extensions import db
from models import User
import re

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def home():
    return "User Management System API"

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    required_fields = ['username', 'email', 'password', 'confirm_password']

    if not all(field in data for field in required_fields):
        return jsonify({'error': "Missing required fields"}), 400

    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_pattern, data['email']):
        return jsonify({'error': 'Invalid email format'}), 400

    if data['password'] != data['confirm_password']:
        return jsonify({'error': 'Passwords do not match'}), 400

    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already exists'}), 400

    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already exists'}), 400

    new_user = User(
        username=data['username'],
        email=data['email'],
    )
    new_user.set_password(data['password'])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

# update user details

@app.route('/users/<int:id>',methods = ['PUT'])
def update_user(id):
    data = request.get_json()
    user = User.query.get(id)
    if not user:
        return jsonify({'error':'No such user'}),404
    if 'username' in data:
        if User.query.filter_by(username=data['username']).first() and user.username != data['username']:
            return jsonify({'error':'Username already exist'}),400
        User.username = data['username']

    if 'email' in data:
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_pattern, data['email']):
            return jsonify({'error': 'Invalid email format'}), 400
        if User.query.filter_by(email=data['email']).first() and User.email != data['email']:
            User.email = data['email']
    db.session.commit()
    return jsonify({'message':"User details updated"}),200

# change password
@app.route('/users/<int:id>/change_password',methods = ['PUT'])
def change_password(id):
    data = request.get_json()
    user = User.query.get(id)
    if not user:
        return jsonify({'error':'User does not exist'})

    if data['old_password'] == user.password:
        if data['new_password'] == data['confirm_password']:
            User.password = data['new_password']
            db.session.commit()
            return jsonify({'message':'successfully changed password'}),200
        else:
            return jsonify({'error': 'passwords does not match'}), 400
    else:
        return jsonify({'error': 'Your old password is incorrect'}), 400

# deleting a user
@app.route('/users/<int:id>',methods = ['DELETE'])
def del_user(id):
    user = User.query.get(id)

    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message':'successfully deleted'}),200
    else:
        return jsonify({'error': 'no user of such kind'}), 404

# get all users
@app.route('/users',methods=['GET'])
def all_users():
    users = User.query.all()
    if users:
       user_list =[]
       for user in users:
            user_list.append(user.to_dict(include_password=Truegit ))
       return jsonify(user_list),200
    else:
        return jsonify({'error':'no registered user'}),404

# get a specific user
@app.route('/users/<int:id>',methods=['GET'])
def single_user(id):
    user = User.query.filter_by(id=id).first()
    if user:
        return jsonify(user.to_dict()),200
    else:
        return jsonify({'error':'no such user'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

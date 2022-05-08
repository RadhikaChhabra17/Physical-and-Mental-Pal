from flask import Flask, jsonify, request, redirect
from flask.helpers import url_for
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin
from werkzeug.security import generate_password_hash

app = Flask(__name__)
cors = CORS(app)
app.config['MONGO_URI'] = 'mongodb+srv://HealthPal:HealthPal@cluster0.6hpjx.mongodb.net/HealthPal?retryWrites=false&w=majority'
app.config['CORS_Headers'] = 'Content-Type'
mongo = PyMongo(app)

@app.route('/', methods = ['GET'])
def retrieveAll():
    holder = list()
    currentCollection = mongo.db.users
    for i in currentCollection.find():
        holder.append({'name':i['name'], 'email' : i['email']})
    return jsonify(holder)

@app.route('/<name>', methods = ['GET'])
@cross_origin()
def retrieveFromName(name):
    currentCollection = mongo.db.users
    data = currentCollection.find_one({"name" : name})
    return jsonify({'name' : data['name']})

@app.route('/postData', methods = ['POST'])
def postData():
    currentCollection = mongo.db.users
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    password_hash = generate_password_hash(password)
    currentCollection.insert_one({'name' : name, 'email' : email, 'password' : password_hash})
    return jsonify({'name' : name, 'email' : email})

@app.route('/deleteData/<name>', methods = ['DELETE'])
def deleteData(email):
    currentCollection = mongo.db.users
    currentCollection.delete_one({'email' : email})
    return redirect(url_for('retrieveAll'))

@app.route('/update/<name>', methods = ['PUT'])
def updateData(name):
    currentCollection = mongo.db.Husers
    updatedName = request.json['name']
    currentCollection.update_one({'name':name}, {"$set" : {'name' : updatedName}})
    return redirect(url_for('retrieveAll'))

if __name__ == '__main__':
    app.run(debug = True)
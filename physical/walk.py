from flask import Flask, jsonify, request, redirect
from flask.helpers import url_for
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin

walk = Flask(__name__)
cors = CORS(walk)
walk.config['MONGO_URI'] = 'mongodb+srv://HealthPal:HealthPal@cluster0.6hpjx.mongodb.net/HealthPal?retryWrites=false&w=majority'
walk.config['CORS_Headers'] = 'Content-Type'
mongo = PyMongo(walk)

@walk.route('/walkData', methods = ['POST'])
def postData():
    currentCollection = mongo.db.walk
    username = request.json['uname']
    duration = request.json['q1']
    distance = request.json['q2']
    preference = request.json['q3']
    currentCollection.insert_one({'uname' : username, 'q1' : duration, 'q2' : distance, 'q3' : preference})
    return jsonify({'uname' : username, 'q1' : duration})


if __name__ == '__main__':
    walk.run(debug = True)
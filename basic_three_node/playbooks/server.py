from os import path
from flask import Flask, request, send_from_directory
from flask.wrappers import Request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast


app = Flask(__name__)
api = Api(app)

# class Data(Resource):


@app.route('/data',methods = ['POST', 'GET'])
def getdata():
    if request.method == 'GET':
        data = pd.read_csv('input_data/metadata.csv')  # read CSV
        print(data)
        data = data.to_dict()  # convert dataframe to dictionary
        # data = "hello blessed"
        return {'data': data}, 200  # return data and 200 OK code

    if request.method == 'POST':
            print('setting config with')
            print(request.get_json())
            return {'done':"good"}, 200  # return data and 200 OK code

@app.route('/model',methods = ['POST', 'GET'])
def getmodel():
    print('model node request received')
    return send_from_directory('input_data', 'model.h5',  as_attachment = True)



 
# api.add_resource(Data, '/data')  # '/users' is our entry point for Users
# api.add_resource(Data, '/model')  # '/users' is our entry point for Users


if __name__ == '__main__':
    app.run()  # run our Flask app
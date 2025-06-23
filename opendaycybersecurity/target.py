import threading
from flask import Flask, make_response, jsonify, render_template
from flask import request
import numpy as np
from flask_cors import CORS
import json
import os
import opendaycybersecurity
#base_folder = os.sep.join(opendaycybersecurity.__file__.split(os.sep)[:-2] + ['bin'])
#os.chdir(base_folder)
template_folder = os.sep.join(opendaycybersecurity.__file__.split(os.sep)[:-2] + ['bin','templates'])
app = Flask(__name__,template_folder=template_folder)
CORS(app)
    
@app.route("/rotate.html")
def rotate_form():
    print(os.getcwd())
    return render_template('rotate.html')
    
@app.route("/move.html")
def move_form():
    print(os.getcwd())
    return render_template('move.html')    
   

@app.route('/movecontrol', methods=['POST', 'GET'])
def movecontrol(): 
    d = json.load(open('secrets.json'))
    if (request.args['username']==d['activity2']['username']) and (request.args['password']==d['activity2']['password']):
        return "Access granted. Moving robot %d cm" % int(request.args['distance'])
    #print(str(request.args['username']))#.form['username']+" --> "+request.form['password'])
    return "Access denied.", 401 #
    

@app.route('/rotationcontrol', methods=['POST', 'GET'])
def rotationcontrol(): 
    d = json.load(open('secrets.json'))
    if (request.args['username']==d['activity1']['username']) and (request.args['password']==d['activity1']['password']):
        if int(request.args['angle'])!=5:
            print("SUCCESS!")
            opendaycybersecurity.hints.hint_track.rotationcontrol_success()    
        return "Access granted. Rotating robot %d degrees" % int(request.args['angle'])

    #print(str(request.args['username']))#.form['username']+" --> "+request.form['password'])
    return "Access denied.", 401 #
    #return "Welcome"    

@app.route('/checksystem', methods=['POST', 'GET'])
@app.route('/view', methods=['POST', 'GET'])
@app.route('/sonar', methods=['POST', 'GET'])
@app.route('/scan', methods=['POST', 'GET'])
@app.route('/sleep', methods=['POST', 'GET'])
@app.route('/wake', methods=['POST', 'GET'])
@app.route('/microphone', methods=['POST', 'GET'])
@app.route('/refresh', methods=['POST', 'GET'])
@app.route('/scan', methods=['POST', 'GET'])
@app.route('/tactics', methods=['POST', 'GET'])
@app.route('/ai', methods=['POST', 'GET'])
@app.route('/detect', methods=['POST', 'GET'])
@app.route('/beep', methods=['POST', 'GET'])
@app.route('/gyro', methods=['POST', 'GET'])
@app.route('/target', methods=['POST', 'GET'])
def catch(): 
    print("catch!")
    return "none\n"

def worker(port):
    print("Starting target FLASK server")
    app.run(host="0.0.0.0", port=port)#, debug=False, use_reloader=False)

def start_target(port=5000):
   
    t = threading.Thread(target=worker,args=(port,))
    t.start()
    return t

import threading
from flask import Flask, make_response, jsonify, render_template
from flask import request
import numpy as np
import urllib.request
from flask_cors import CORS
import json
import os
import opendaycybersecurity
#base_folder = os.sep.join(opendaycybersecurity.__file__.split(os.sep)[:-2] + ['bin'])
#os.chdir(base_folder)
template_folder = os.sep.join(opendaycybersecurity.__file__.split(os.sep)[:-2] + ['bin','templates'])
app = Flask(__name__,template_folder=template_folder)
CORS(app)

port = 0
server = ''

@app.route("/rotate.html")
def rotate_form():
    return render_template('rotate.html')
    
@app.route("/move.html")
def move_form():
    return render_template('move.html')    

@app.route("/email.html")
def email_form():
    return render_template('email.html',server="127.0.0.1:%d" % port)    
    
@app.route("/admin.html")
def admin_form():
    return render_template('email_admin.html',server="127.0.0.1:%d" % port)

   
@app.route("/drop.html")
def drop_form():
    return render_template('drop.html')  

import os
client_id = int.from_bytes(os.urandom(5))


emails = {}
@app.route('/recordemail',methods=['POST','GET'])
def recordemail():
    global emails
    #request.args
    args = request.args.to_dict()
    print(args)
    mpa = dict.fromkeys(range(32))
    msg = args['message'].translate(mpa)
    sub = args['subject'].translate(mpa)
    recipient = args['recipient'].translate(mpa)
    sender = args['sender'].translate(mpa)
    if recipient not in emails: emails[recipient] = []
    emails[recipient].append({'sender':sender,'sub':sub,'msg':msg})
    return "done", 200

@app.route('/collectemail',methods=['POST','GET'])
def collectemail():
    global emails
    print("EMAILS")
    print(emails)

    args = request.args.to_dict()
    #request.args
    #print(request.args)
    mpa = dict.fromkeys(range(32))
    recipient = args['recipient'].translate(mpa)
    if recipient not in emails: return []
    msg = jsonify(emails[recipient])
    del emails[recipient]
    return msg
    
@app.route('/sendemail', methods=['POST', 'GET'])
def sendemail(): 
    global server
    #request.args
    print(request.args)
    mpa = dict.fromkeys(range(32))
    args = request.args.to_dict()
    msg = args['message'].translate(mpa)
    sub = args['subject'].translate(mpa)
    if 'recipient' in args:
        recipient = args['recipient'].translate(mpa)
        sender = 0    
    else:
        recipient = 0
        sender = client_id
    try:
        items = {'subject':sub, 'message':msg, 'recipient':recipient, 'sender':sender}
        import requests
        contents = requests.get('http://'+server+'/recordemail', params=items)
        #contents = urllib.request.urlopen("http://127.0.0.1:5001/recordemail?"+query_string) #subject=%s&message=%s&recipient=%s&sender=%s"% (sub,msg,recipient,sender))
    except Exception as e:
        print(e)
        return "failed to send email (%s)" % str(e), 503 #jsonify('Failed to send email.',status=503)
    return jsonify('Success')

@app.route('/setid/<int:newid>')
def setid(newid):
    global client_id
    msg = "Done (%d->%d)" % (client_id,newid)
    client_id = newid
    return msg

@app.route('/checkemail', methods=['POST', 'GET'])
def checkemail():
    global server
    try:
        contents = urllib.request.urlopen("http://"+server+"/collectemail?recipient=%s"% (client_id))
    except:
        return "failed to check email", 503 #jsonify('Failed to check email.',status=503)
    return contents


@app.route('/dropcontrol', methods=['POST', 'GET'])
def dropcontrol(): 
    d = json.load(open('secrets.json'))
    if (request.args['username']==d['activity3']['username']) and (request.args['password']==d['activity3']['password']):
        return "Access granted. Dropping ball-bearing"
    return "Access denied.", 401 #
   

@app.route('/movecontrol', methods=['POST', 'GET'])
def movecontrol(): 
    d = json.load(open('secrets.json'))
    if (request.args['username']==d['activity2']['username']) and (request.args['password']==d['activity2']['password']):
        return "Access granted. Moving robot %0.2f cm" % float(request.args['distance'])
    return "Access denied.", 401 #
    

@app.route('/rotationcontrol', methods=['POST', 'GET'])
def rotationcontrol(): 
    d = json.load(open('secrets.json'))
    #if ('username' not in request.args) or ('password' not in request.args) or ('angle' not in request.args):
    #    print("Missing Arguments")
    #    return "Missing arguments (did you fill in all the form fields?)"

    if (request.args['username']==d['activity1']['username']) and (request.args['password']==d['activity1']['password']):
        try:
            if float(request.args['angle'])!=1.0113:
                print("rotationcontrol endpoint accessed successfully")
            return "Access granted. Rotating robot %0.2f degrees" % float(request.args['angle'])
        except:
            return "Control failed (did you fill all the form fields correctly?)"
    return "Access denied.", 401

#@app.route('/email/',methods=['POST','GET'])
#def getemail(

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
    return "none\n"

def worker(port):
    print("Starting target FLASK server")
    app.run(host="0.0.0.0", port=port)

def start_target(remoteserver,localport=5000):
    global server
    server = remoteserver
    global port
    port = localport
    t = threading.Thread(target=worker,args=(port,))
    t.start()
    return t

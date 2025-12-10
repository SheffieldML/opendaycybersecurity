import threading
import random
from flask import Flask, make_response, jsonify, render_template
from flask import request
import datetime
import numpy as np
import urllib.request
from flask_cors import CORS
import json
import os
import opendaycybersecurity
#base_folder = os.sep.join(opendaycybersecurity.__file__.split(os.sep)[:-2] + ['bin'])
#os.chdir(base_folder)
template_folder = os.sep.join(opendaycybersecurity.__file__.split(os.sep)[:-2] + ['bin','templates'])
static_folder = os.sep.join(opendaycybersecurity.__file__.split(os.sep)[:-2] + ['bin','static'])
app = Flask(__name__,template_folder=template_folder,static_folder="static")
CORS(app)

port = 0
#server = ''

@app.route("/rotate.html")
def rotate_form():
    return render_template('rotate.html')
    
@app.route("/move.html")
def move_form():
    return render_template('move.html')    

@app.route("/email.html")
def email_form():
    return render_template('email.html',server="127.0.0.1:%d" % port)
    
@app.route("/full.html")
def full_form():

    global move_success
    global turn_success
    print(move_success, turn_success)
    if move_success and turn_success:
        return render_template('full.html',server="127.0.0.1:%d" % port)
    else:
        return render_template('full_access_denied.html')
    
#@app.route("/admin.html")
#def admin_form():
#    return render_template('email_admin.html',server="127.0.0.1:%d" % port)

   
#@app.route("/drop.html")
#def drop_form():
#    return render_template('drop.html')  

#import os
#client_id = int.from_bytes(os.urandom(5),byteorder='big')


#emails = {}
#@app.route('/recordemail',methods=['POST','GET'])
#def recordemail():
#    global emails
#    #request.args
#    args = request.args.to_dict()
#    print(args)
#    mpa = dict.fromkeys(range(32))
#    msg = args['message'].translate(mpa)
#    sub = args['subject'].translate(mpa)
#    recipient = args['recipient'].translate(mpa)
#    sender = args['sender'].translate(mpa)
#    if recipient not in emails: emails[recipient] = []
#    emails[recipient].append({'sender':sender,'sub':sub,'msg':msg})
#    return "done", 200

#@app.route('/collectemail',methods=['POST','GET'])
#def collectemail():
#    global emails
#    print("EMAILS")
#    print(emails)
#
#    args = request.args.to_dict()
#    #request.args
#    #print(request.args)
#    mpa = dict.fromkeys(range(32))
#    recipient = args['recipient'].translate(mpa)
#    if recipient not in emails: return []
#    msg = jsonify(emails[recipient])
#    del emails[recipient]
#    return msg
    
#@app.route('/oldsendemail', methods=['POST', 'GET'])
#def oldsendemail(): 
#    global server
#    #request.args
#    print(request.args)
#    mpa = dict.fromkeys(range(32))
#    args = request.args.to_dict()
#    msg = args['message'].translate(mpa)
#    sub = args['subject'].translate(mpa)
#    if 'recipient' in args:
#        recipient = args['recipient'].translate(mpa)
#        sender = 0    
#    else:
#        recipient = 0
#        sender = client_id
#    try:
#        items = {'subject':sub, 'message':msg, 'recipient':recipient, 'sender':sender}
#        import requests
#        contents = requests.get('http://'+server+'/recordemail', params=items)
#        #contents = urllib.request.urlopen("http://127.0.0.1:5001/recordemail?"+query_string) #subject=%s&message=%s&recipient=%s&sender=%s"% (sub,msg,recipient,sender))
#    except Exception as e:
#        print(e)
#        return "failed to send email (%s)" % str(e), 503 #jsonify('Failed to send email.',status=503)
#    return jsonify('Success')

email_reply = None
email_countdown = datetime.datetime.now()
move_success = False
turn_success = False

@app.route('/sendemail', methods=['POST', 'GET'])
def sendemail(): 
    print("Sending!")
    global email_countdown
    global email_reply
    #request.args
    print(request.args)
    mpa = dict.fromkeys(range(32))
    args = request.args.to_dict()
    msg = args['message'].translate(mpa)
    sub = args['subject'].translate(mpa)
    email_countdown = datetime.datetime.now() + datetime.timedelta(0,random.randrange(3,6))
    if (len(msg)>50) and (len(sub)>3):
        email_reply = True
        
    else:
        email_reply = False
    return jsonify('Success')

#@app.route('/setid/<int:newid>')
#def setid(newid):
#    global client_id
#    msg = "Done (%d->%d)" % (client_id,newid)
#    client_id = newid
#    return msg

#@app.route('/checkemail', methods=['POST', 'GET'])
#def checkemail():
#    global server
#    try:
#        contents = urllib.request.urlopen("http://"+server+"/collectemail?recipient=%s"% (client_id))
#    except:
#        return "failed to check email", 503 #jsonify('Failed to check email.',status=503)
#    return contents


@app.route('/checkemail', methods=['POST', 'GET'])
def checkemail():
    d = json.load(open('secrets.json'))
    global email_reply
    print(email_reply)
    if email_reply is None:
        print("Email reply is none")
        return jsonify([]) #no emails
        #return "no emails", 404
    else:
        if datetime.datetime.now()>email_countdown:
            if email_reply:
                email_reply = None
                return jsonify([{'sub':d['success_email_subject'], 'msg':d['success_email_message']}])
            else:
                email_reply = None
                return jsonify([{'sub':d['sorry_email_subject'], 'msg':d['sorry_email_message']}])
        else:
            return jsonify([])
        #return "failed to check email", 503 #jsonify('Failed to check email.',status=503)
    return contents
    
#@app.route('/dropcontrol', methods=['POST', 'GET'])
#def dropcontrol(): 
#    d = json.load(open('secrets.json'))
#    if (request.args['username']==d['activity3']['username']) and (request.args['password']==d['activity3']['password']):
#        return "Access granted. Dropping ball-bearing"
#    return "Access denied.", 401 #
   


def move_robot(distance):
    print("MOVING ROBOT: %0.2fm" % distance)
    os.system('ros2 run com_offer_holder_days forward.py --ros-args -p dist:=%0.3f &' % distance)
    
def turn_robot(angle):
    print("TURNING ROBOT: %d degrees" % angle)
    os.system('ros2 run com_offer_holder_days turn.py --ros-args -p angle:=%d &' % int(angle))

@app.route('/movecontrol', methods=['POST', 'GET'])
def movecontrol(): 
    d = json.load(open('secrets.json'))
    if (request.args['username']==d['activity2']['username']) and (request.args['password']==d['activity2']['password']):
        move_robot(float(request.args['distance']))
        global move_success
        if float(request.args['distance'])!=0.0: #the synthetic user always sends a '0.0' -- we don't want that user allowing us access.
            move_success = True
        return "Access granted. Moving robot %0.3f m" % float(request.args['distance'])
    return "Access denied.", 401
    

@app.route('/fullcontrol', methods=['POST', 'GET'])
def fullcontrol(): 
    global move_success
    global turn_success
    if not move_success or not turn_success:
        return jsonify([]), 401
    
    if request.args['button']=='fastforward':
        move_robot(0.5)
    if request.args['button']=='forward':
        move_robot(0.05)
    if request.args['button']=='backward':
        move_robot(-0.05)
    if request.args['button']=='left':
        turn_robot(20)
    if request.args['button']=='right':
        turn_robot(-20)
    return jsonify([]), 200


@app.route('/rotationcontrol', methods=['POST', 'GET'])
def rotationcontrol(): 
    d = json.load(open('secrets.json'))
    #if ('username' not in request.args) or ('password' not in request.args) or ('angle' not in request.args):
    #    print("Missing Arguments")
    #    return "Missing arguments (did you fill in all the form fields?)"

    if (request.args['username']==d['activity1']['username']) and (request.args['password']==d['activity1']['password']):
        try:
            turn_robot(int(request.args['angle']))
            global turn_success
            if int(request.args['angle'])!=0: #sythetic user always sends 0 degree -- this avoids that user from enabling access
                turn_success = True
            return "Access granted. Rotating robot %0d degrees" % int(request.args['angle'])
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

import threading
from flask import Flask, make_response, jsonify, render_template
from flask import request
import numpy as np
from flask_cors import CORS
import json
import os
import time
import psutil

global hint_track

import opendaycybersecurity
#base_folder = os.sep.join(opendaycybersecurity.__file__.split(os.sep)[:-2] + ['bin'])
#os.chdir(base_folder)
template_folder = os.sep.join(opendaycybersecurity.__file__.split(os.sep)[:-2] + ['bin','templates'])

app = Flask(__name__,template_folder=template_folder)


CORS(app)


@app.route("/")
def home():
    return render_template('hints.html')
    
   
@app.route("/getmessage")
def getmessage():
    if len(hint_track.message_queue)==0:
        return ""
    else:
        return hint_track.message_queue.pop(0)
        


def worker(port):
    print("Starting target FLASK server")
    app.run(host="0.0.0.0", port=port)#,template_folder=template_folder)#, debug=False, use_reloader=False)

def start_hints(port=5001):
    t = threading.Thread(target=worker,args=(port,))
    t.start()
    return t
    
class HintTrack:
    def __init__(self):
        self.target_port = 9999
        self.hint = 0
        self.message_queue = []
        base_folder = os.sep.join(opendaycybersecurity.__file__.split(os.sep)[:-2] + ['bin'])
        #os.chdir(base_folder)
        print("Opening %s" % (base_folder+'/hints.json'))
        self.messages = json.load(open(base_folder+'/hints.json','rb'))        
        #self.add_message()
        self.countdown = 1
        self.t = threading.Thread(target=self.worker)
        #self.jump_forward_to_stage('filter')
        self.t.start()
        
        
    def worker(self):
        while True:
            while self.countdown>0:
                time.sleep(1)
                self.countdown-=1
                print(self.countdown)
                self.wireshark_check() #check if they've sorted wireshark
            self.add_message() #send the next message!
            
            
    def add_message(self):
        """
        Adds the next message from the hints.json file to the message queue, and increments the hint counter.
        """
        
        msg = self.messages[self.hint]['message']
        msg = msg.replace('$target_link$','http://127.0.0.1:%d/rotate.html' % self.target_port)
        msg = msg.replace('$target_link2$','http://127.0.0.1:%d/move.html' % self.target_port)        
        
        msg = "<hr/><p style='color:#dddddd'>Hint %d</p><br/>" % (self.hint+1) + msg
        print(self.hint)
        
        self.message_queue.append(msg)
        self.countdown=self.messages[self.hint]['wait']
        self.hint+=1 #on to the next hint...

    def jump_forward_to_stage(self,stage_name):
        for i,m in enumerate(self.messages):
            if m['stage']==stage_name:
                if self.hint<i:
                    print("Jumping forward to stage %d (%s)" % (i,stage_name))
                    self.hint = i
                    self.countdown = 0
                
    #A series of checks to see what stage they are at!
    def wireshark_check(self): 
        try:
            if any([psutil.Process(pid).name()=='wireshark' for pid in psutil.pids()]):
                self.jump_forward_to_stage("loopback")
        except:
            print("Exception occured while looking for wireshark process")



    def rotationcontrol_success(self):
        self.jump_forward_to_stage("intro_challenge2")
        
hint_track = HintTrack()        

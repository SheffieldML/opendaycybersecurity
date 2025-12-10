import requests
import time
import numpy as np
import threading
import json

class SimulatedClient:
    def __init__(self,target_port = 5000, rate=0.1):
        """
        Creates a simulated client that sends HTTP requests to our target API, repeatedly.
        These consist of lots of queries, almost all don't contain the password
        (this means we need to filter them in wireshark).
        
        target_port = where the simulatedclient needs to send its packets
        rate = how frequently to send them (in seconds) + noise
        """
        self.queries = ['checksystem?all=1','view?camera=1&systemcheck=3','sonar?report=1&both=1','scan?range=40&reversed=10','sleep?time=5','wake?time=50','microphone?enable=0','refresh','scan?range=10','tactics?process=1','ai?enable=0','detect?range=40','beep?volume=0&length=10','gyro?enable=0','target?range=100','checksystem?all=0','view?camera=0&systemcheck=0','sonar?report=0&both=1'] * 3 #duplicate lots of times...
        self.queries += ['rotationcontrol','movecontrol']
        self.target_port = target_port
        self.rate = rate
        self.secrets = json.load(open('secrets.json'))
        
        
    def worker(self):
        print("Simulated client query rate, averages 2 times %0.2f s/query" % self.rate)
        idx = 0
        time.sleep(1) #wait one second before starting
        print("Simulated client sending queries")
        while True:    
            idx+=1
            if idx>=len(self.queries): idx=0        
            #print("Sending query...")
            querystring = self.queries[idx]
            try:
                if querystring == 'rotationcontrol':
                    params = {
                        'username': self.secrets['activity1']['username'],
                        'password': self.secrets['activity1']['password'],
                        'angle': 0, 
                    }
                    #print("Sending simulated client rotationcontrol command")
                    r = requests.get("http://127.0.0.1:%d/rotationcontrol" % self.target_port, params=params)
                    continue
                if querystring == 'movecontrol':
                    params = {
                        'username': self.secrets['activity2']['username'],
                        'password': self.secrets['activity2']['password'],
                        'distance': 0.0,
                    }
                    #print("Sending simulated client movecontrol command")                    
                    r = requests.get("http://127.0.0.1:%d/movecontrol" % self.target_port, params=params)
                    continue

                r = requests.get("http://127.0.0.1:%d/%s" % (self.target_port,self.queries[idx]))
            except Exception as e: #probably a problem connecting... keep going
                print("Failed to send")
                print(e)
                pass
            time.sleep(self.rate+np.random.rand()*self.rate*2)
            
    def start(self):
        print("Starting Simulated Client")
        t = threading.Thread(target=self.worker)
        t.start()
        return t 

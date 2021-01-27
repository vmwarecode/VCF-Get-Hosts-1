#Get all Hosts
#Get list of all hosts available.
import requests
import json
import sys
import os
import pprint
sys.path.append(os.path.abspath(__file__ + '/../../'))
from Utils.utils import Utils

class GetHosts:
    def __init__(self):
        print('Get Hosts')
        self.utils = Utils(sys.argv)
        self.hostname = sys.argv[1]
    

    def get_hosts(self):
        get_hosts_url = 'https://'+self.hostname+'/v1/hosts/'
        response = self.utils.get_request(get_hosts_url)
        pprint.pprint(response)

if __name__== "__main__":
    GetHosts().get_hosts()

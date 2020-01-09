import requests
import json
import phProj
import phRun

class Ph:

    def __init__(self, apiKey):
        self.apiKey = apiKey

    def getProj(self, projToken, offset=0, limit =20, includeOptions=1):
        params = {
            "api_key": self.apiKey,
            "offset": offset,
            "limit": limit,
            "include_options": includeOptions
        }
        return phProj.PhProj(self, requests.get('https://www.parsehub.com/api/v2/projects/' + projToken, params=params).json())

    def runProj(self, projToken, startUrl=0, startTemplate=0, sendEmail=0):
        params = {
            "api_key": self.apiKey,
            "start_url": startUrl,
            "start_template": startTemplate,
            "send_email": sendEmail
        }
        return phRun.PhRun(self, requests.post("https://www.parsehub.com/api/v2/projects/"+ projToken +"/run", data=params).json())

    def getProjList(self, offset=0, includeOptions=1):

        params = {
            "api_key": self.apiKey,
            "offset": offset,
            "limit": limit,
            "include_options": "1"
        }
        return requests.get('https://www.parsehub.com/api/v2/projects', params=params).json()

    def getRun(self, runToken):
        params = {
            "api_key": self.apiKey
        }
        return phRun.PhRun(self, requests.get('https://www.parsehub.com/api/v2/runs/'+ runToken, params=params).json())

    def getRunData(self, runToken):
        params = {
            "api_key": self.apiKey,
            "format": "csv"
        }
        return requests.get('https://www.parsehub.com/api/v2/runs/'+ runToken +'/data', params=params).json()

    def getLastReadyRun(self, projToken, format="json"):
        params = {
            "api_key": self.apiKey,
            "format": format
        }
        return requests.get('https://www.parsehub.com/api/v2/projects/'+projToken+'/last_ready_run/data', params=params).json()

    def cancelRun(self, runToken):
        params = {
            "api_key": self.apiKey
        }
        return phRun.PhRun(self, requests.post("https://www.parsehub.com/api/v2/runs/"+runToken+"/cancel", data=params).json())

    def deleteRun(self, runToken):
        params = {
            "api_key": self.apiKey
        }
        return phRun.PhRun(self, requests.delete('https://www.parsehub.com/api/v2/runs/'+runToken, params=params).json())


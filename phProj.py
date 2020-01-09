import ph
import phRun
import json

class PhProj:

    def __init__(self, p, data):
        self.p = p
        self.data = data

    def getProjToken(self):
        return self.data["token"]
    def getTitle(self):
        return self.data["title"]
    def getMainTemplate(self):
        return self.data["main_template"]
    def getMainSite(self):
        return self.data["main_site"]
    def getOptions(self):
        return self.data["options_json"]
    def getLastRunToken(self):
        return self.data["last_run"]["run_token"]
    def getLastReadyRunToken(self):
        return self.data["last_ready_run"]["run_token"]

    def run(self, startUrl=0, startTemplate=0, sendEmail=0):
        if startUrl == 0:
            startUrl = self.getMainSite()
        if startTemplate == 0:
            startTemplate = self.getMainTemplate()
        return self.p.runProj(self.getProjToken(), startUrl, startTemplate, sendEmail)

    def update(self):
        newProj = self.p.getProj(self.getProjToken())
        self.__dict__.update(newProj.__dict__)
import ph
import json

class PhRun:

    def __init__(self, p, data):
        self.p = p
        self.data = data

    def getProjToken(self):
        return self.data["project_token"]
    def getRunToken(self):
        return self.data["run_token"]
    def getStatus(self):
        return self.data["status"]
    def getDataReady(self):
        return self.data["data_ready"]
    def getStartTime(self):
        return self.data["start_time"]
    def getEndTime(self):
        return self.data["end_time"]
    def getPages(self):
        return self.data["pages"]
    def getMd5sum(self):
        return self.data["md5sum"]
    def getStartUrl(self):
        return self.data["start_url"]
    def getStartTemplate(self):
        return self.data["start_template"]
    def getStartValue(self):
        return self.data["start_value"]

    def cancel(self):
        return self.p.cancelRun(self.getRunToken())

    def delete(self):
        return self.p.deleteRun(self.getRunToken())

    def getData(self):
        return self.p.getRunData(self.getRunToken())

    def update(self):
        newRun = self.p.getRun(self.getRunToken())
        self.__dict__.update(newRun.__dict__)
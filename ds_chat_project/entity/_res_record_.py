class ResRecord(object):
    def __init__(self,id=None,status_code=None,headers=None,res_text=None,create_time=None):
        self.id = id
        self.status_code = status_code
        self.headers = headers
        self.res_text = res_text
        self.create_time = create_time

    def getId(self):
        return self.id

    def getStatusCode(self):
        return self.status_code

    def getHeaders(self):
        return self.headers

    def getRes_text(self):
        return self.res_text

    def getCreateTime(self):
        return self.create_time
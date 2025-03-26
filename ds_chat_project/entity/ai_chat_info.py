class AIChatInfo(object):
    def __init__(self,id=None,problem_info=None,res_info=None,create_time=None):
        self.id = id
        self.problem_info = problem_info
        self.res_info = res_info
        self.create_time = create_time

    def getId(self):
        return self.id

    def getProblemInfo(self):
        return self.problem_info

    def getResInfo(self):
        return self.res_info

    def getCreateTime(self):
        return self.create_time

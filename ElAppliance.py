import datetime
class ElApplience:
    def __init__(self,dailyUsageMin,dailyUsageMax,timeMin = "00:00",timeMax ="23:59"):
        self.dailyUsageMin = dailyUsageMin
        self.dailyUsageMax = dailyUsageMax
        self.timeMin = timeMin
        self.timeMax = timeMax

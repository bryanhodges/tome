config = {
    dbConnection = "Driver={ODBC Driver 13 for SQL Server};Server=tcp:tome.database.windows.net,1433;Database=tome;Uid=lj553650;Pwd=Duff153z;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
}

class Config(object):

    def __init__(self):
        self.config = config

    def getConfigValue(self, key):
        return self.config[key]
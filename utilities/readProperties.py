import configparser

config = configparser.RawConfigParser()
# config.read(".\\config.ini")
config.read("C:\\python-selenium\\nopcommerceApp\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get("common info","baseURL")
        return url
    @staticmethod
    def getUserEmail():
        username = config.get("common info","userName")
        return username
    @staticmethod
    def getpassword():
        password = config.get("common info","password")
        return password

    @staticmethod
    def invalidemail():
        invalidEmail = config.get("common info", "invalidUserName")
        return invalidEmail









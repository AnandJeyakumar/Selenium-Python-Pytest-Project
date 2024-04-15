import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="C:\\python-selenium\\nopcommerceApp\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        loggerValue = logging.getLogger()
        loggerValue.setLevel(logging.INFO)
        loggerValue.info('Logging configuration successful')
        return loggerValue


# loggerValue = LogGen.loggen()
# print(loggerValue)

class PrintInfo:

    @staticmethod
    def printError(error):
        message = 'A error has been find : ' + error
        PrintInfo.display_error(message)
        exit()
    
    def display_error(message):
        print(f"\033[31mError: {message}\033[0m")  

    @staticmethod
    def printInfo(message):
        message = message
        PrintInfo.display_info(message)
    
    def display_info(message):
        print(f"\033[32mInfo: {message}\033[0m")  
class Password:
    def __init__(self, password):
        self.__password = password

    def verify(self, string):
        if self.__password == string:
            return True
        else:
            return False
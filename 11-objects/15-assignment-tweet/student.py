# Write your code here
class Tweet:
    def __init__(self, message, max_length):
        if max_length < 1:
            raise ValueError()

        self.__message = message[:max_length]
        self.__max_length = max_length

    def get_message(self):
        return self.__message
    
    def get_max_length(self):
        return self.__max_length

    def set_message(self, value):
        if len(value) > self.__max_length:
            self.__message = value[:self.__max_length]
        else:
            self.__message = value
    
    def set_max_length(self, value):
        if value < 1:
            raise ValueError()
        
        self.__max_length = value
        if len(self.__message) > self.__max_length:
            self.__message = self.__message[:self.__max_length]

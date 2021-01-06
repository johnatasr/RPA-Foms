from models import input as InputModel

class InputRepository:
    def __init__(self, name, value):
        self.model = InputModel()
        self.__value = value
        self.__key = name

    def get_name(self):
        return self.__name

    def get_key(self):
        return self.__key

    def get_value(self):
        return self.__value
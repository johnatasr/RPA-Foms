class Input:
    def __init__(self, name, value):
        self.__name = name
        self.__value = value
        self.__key = name

    def get_name(self):
        return self.__name

    def get_key(self):
        return self.__key

    def get_value(self):
        return self.__value
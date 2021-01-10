

class Form:
    def __init__(self):
        self.__id = None
        self.__url = None
        self.__key = None
        self.__value = None
        self.modelCreated = False
        self.modelTable: str = self.__name__.lower()

    def get_id(self):
        return self.__id

    def __set_id(self, id):
        self.__id = id

    def get_url(self):
        return self.__url

    def set_url(self, name):
        self.__url = name

    def get_key(self):
        return self.__key

    def set_key(self, key):
        self.__key = key

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    def get_model_table(self):
        return self.modelTable

    def get_all_values(self):
        if not all(self.__url, self.__key, self.__value):
            return [self.__url, self.__key, self.__value]
        else:
            return f"Empty Model: {self.__name__}"

    def format_update_set(self):
        return f"name={self.get_name()},key={self.get_key()},value={self.get_value()}"

    def create_model(self, url, key, value) -> object:
        self.__url = url
        self.__key = key
        self.__value = value
        return Form








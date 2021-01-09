from connections import database as DB


class Input:
    def __init__(self):
        self.dataConnection = DB()
        self.__id = None
        self.__name = None
        self.__key = None
        self.__value = None
        self.modelCreated = False
        self.modelTable: str = self.__name__.lower()

    def get_id(self):
        return self.__id

    def __set_id(self):
        pass

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

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

    def get_by_id(self):
        return self.dataConnection.select(Input(), f'where id = {self.get_id()}')

    def get_all(self):
        return self.dataConnection.select(Input())

    def get_all_values(self):
        if not all(self.__name, self.__key, self.__value):
            return [self.__name, self.__key, self.__value]
        else:
            return f"Empty Model: {self.__name__}"

    def format_update_set(self):
        return f"name={Input.get_name()},key={Input.get_key()},value={Input.get_value()}"

    def create(self, name, key, value):
        Input.set_name(name)
        Input.set_key(key)
        Input.set_value(value)
        created_params = self.dataConnection.insert(Input())
        Input.__set_id(created_params['id'])
        self.modelCreated = True

    def update(self, name, key, value):
        Input.set_name(name)
        Input.set_key(key)
        Input.set_value(value)
        self.dataConnection.update(Input(), self.format_update_set())

    def delete(self):
        self.dataConnection.delete(self.get_id())







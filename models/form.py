

class Form:
    def __init__(self):
        self.id = None
        self.url = None
        self.key = None
        self.value = None
        self.modelCreated = False
        self.modelTable: str = self.__class__.__name__.lower()

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_url(self):
        return self.url

    def set_url(self, name):
        self.url = name

    def get_key(self):
        return self.key

    def set_key(self, key):
        self.key = key

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_model_table(self):
        return self.modelTable

    def get_all_values(self):
        if all([self.url, self.key, self.value]):
           return [self.url, self.key, self.value]
        else:
            return f"Empty Model: {self.__name__}"

    def create_model(self, url: str, key: str, value: str) -> object:
        self.set_url(url)
        self.set_key(key)
        self.set_value(value)
        return self

    def update_query_set(self) -> str:
        query: str = f"key='{self.key}', value='{self.value}'"
        return query

    @staticmethod
    def create_table() -> str:
        query: str = "CREATE TABLE IF NOT EXISTS form ( " \
                     "id INTEGER PRIMARY KEY, " \
                     "url VARCHAR(500), " \
                     "key VARCHAR(200), " \
                     "value VARCHAR(200))"
        return query







from models import form as FormModel
from connections import database as DB


class InputRepository:
    def __init__(self):
        self.dataConnection: object = DB()
        self.model: object = FormModel()
        self.listObjects: list = []

    def create_database(self) -> None:
        query: str = "CREATE TABLE IF NOT EXISTS form input ( " \
                     "id INTEGER PRIMARY KEY, " \
                     "url VARCHAR(500), " \
                     "key VARCHAR(200), " \
                     "value VARCHAR(200)"
        self.dataConnection.start(query)

    def get_all(self) -> list:
        return self.dataConnection.select(self.model.get_model_table(), None)

    def get_by_id(self, id: str) -> list:
        self.model.__set_id(id)
        return self.dataConnection.select(self.model, f'where id = {self.model.get_id()}')

    def create(self, url: str, key: str, value: str) -> str:
        self.model.set_url(url)
        self.model.set_key(key)
        self.model.set_value(value)
        created_params: list = self.dataConnection.insert(self.model)

        if 'id' in created_params:
            self.model.__set_id(created_params['id'])
            return self.model.get_id()

        self.model = None

    def update(self, name: str, key: str, value: str) -> None:
        self.model.set_url(name)
        self.model.set_key(key)
        self.model.set_value(value)
        self.dataConnection.update(self.model, self.model.format_update_set())
        self.model = None

    def delete(self, id: str) -> None:
        if self.model is not None:
            self.model = None
        self.model.__set_id(id)
        self.dataConnection.delete(self.model)

from models.form import Form
from connections.database import Database as DB


class FormRepository:
    def __init__(self):
        self.dataConnection = DB()
        self.model: object = Form()
        self.listObjects: list = []

    def create_database(self) -> None:
        self.dataConnection.start(self.model.create_table())

    def get_all(self) -> list:
        return self.dataConnection.select(self.model, None)

    def get_by_id(self, id: str) -> list:
        self.model.__set_id(id)
        return self.dataConnection.select(self.model, f'where id = {self.model.get_id()}')

    def create(self, url: str, key: str, value: str) -> str:
        self.model.create_model(url, key, value)
        self.dataConnection.insert(self.model)

    def update(self, name: str, key: str, value: str) -> None:
        self.model.set_url(name)
        self.model.set_key(key)
        self.model.set_value(value)
        self.dataConnection.update(self.model, self.model.format_update_set())
        self.model = None

    def delete(self, id: str) -> None:
        self.model.set_id(id)
        self.dataConnection.delete(self.model)

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

    def update(self, id: int, url: str, key: str, value: str) -> None:
        self.model.create_model(url, key, value)
        self.model.set_id(id)
        self.dataConnection.update(self.model)
        self.model = None

    def delete(self, id: str) -> None:
        self.model.set_id(id)
        self.dataConnection.delete(self.model)

    def truncate(self) -> None:
        self.dataConnection.delete(self.model, truncate=True)

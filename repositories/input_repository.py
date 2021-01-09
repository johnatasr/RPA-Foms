from models import input as InputModel


class InputRepository:
    def __init__(self, name, value):
        self.model = InputModel()

    def get_all(self):
        return self.model.get_all()

    def insert_input(self, ):
        return self.model.

    def get_value(self):
        return self.__value
import sqlite3
from models import input


class Database:

    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = None
        self.query = None
        self.model = None

    def start(self) -> None:
        self.cursor = self.connection.cursor()
        self.query =  "CREATE TABLE IF NOT EXISTS input (id INTEGER PRIMARY KEY, name VARCHAR(200), key VARCHAR(200), value VARCHAR(4)"
        self.cursor.execute(self.query)
        self.connection.commit()
        self.connection.close()

    def insert(self, model, obj_model):
        try:
            values_str, cols_values, objs_variables = "", "", vars(obj_model)
            objs_variables.remove('dataConnection', 'modelTable')

            for value in obj_model.get_all_values():
                values_str = values_str + ',' + value

            for cols_value in objs_variables:
                cols_values = cols_values + ',' + cols_value

            self.query = f'insert into {model} ({values_str}) values({values_str})'
            self.cursor.execute(self.query)
            rows = self.cursor.fetchall()
            self.connection.commit()
            self.connection.close()

            return rows



        except ValueError as error:
            print(error)

    def update(self, obj_model):
        try:
            values_str, cols_values, objs_variables = "", "", vars(obj_model)
            objs_variables.remove('dataConnection', 'modelTable', 'modelCreated')

            for value in obj_model.get_all_values():
                values_str = values_str + ',' + value

            for cols_value in objs_variables:
                cols_values = cols_values + ',' + cols_value

            self.query = f'update {obj_model.modelTable} set title=?,author=?,year=?,isbn=? where id=?  ({values_str}) values({values_str})'

            self.cursor.execute()

            self.connection.commit()
            self.connection.close()

        except ValueError as error:
            print(error)

    def delete(self):
        pass

    def run_query(self, model, query):
        self.model = model
        self.query = query

        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query)
        self.connection.commit()
        self.connection.close()





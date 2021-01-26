import sqlite3
from models import form


class Database:

    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = None
        self.query = None
        self.start()

    def start(self) -> None:
        self.cursor = self.connection.cursor()

    def select(self, obj_model, args):
        try:
            if args:
                self.query = f'select * from {obj_model.get_model_table()} {args}'

            self.query = f'select * from {obj_model.get_model_table()}'
            rows = self.__run_query_with_return(self.query)

            return rows
        except ValueError as error:
            print(error)

    def insert(self, obj_model):
        try:
            values_str, cols_values, objs_variables = "", "", vars(obj_model)
            objs_variables.remove('dataConnection', 'modelTable', 'modelCreated')

            for value in obj_model.get_all_values():
                values_str = values_str + ',' + value

            for cols_value in objs_variables:
                cols_values = cols_values + ',' + cols_value

            self.query = f'insert into {obj_model.get_model_table()} ({cols_values}) values({values_str})'
            rows = self.__run_query_with_return(self.query)

            return rows
        except ValueError as error:
            print(error)

    def update(self, obj_model, str_set):
        try:
            self.query = f'update {obj_model.modelTable} set {str_set} where id= {obj_model.get_id()}'
            self.run_query(self.query)
            self.query = None

        except ValueError as error:
            print(error)

    def delete(self, obj_model):
        try:
            self.query = f'DELETE FROM {obj_model.get_model_table()} WHERE id={obj_model.get_id()}'
            self.run_query(self.query)
            self.query = None

        except ValueError as error:
            print(error)

    def __run_query_with_return(self, query):
        try:
            self.cursor = self.connection.cursor()
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            self.connection.commit()
            self.connection.close()

            return rows

        except Exception as error:
            print(error)

    def __run_query(self, query):
        try:
            self.cursor = self.connection.cursor()
            self.cursor.execute(query)
            self.connection.commit()
            self.connection.close()

        except Exception as error:
            print(error)






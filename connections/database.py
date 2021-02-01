import sqlite3
from models import form


class Database:

    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = None
        self.query = None

    def start(self, query) -> None:
        self.cursor = self.connection.cursor()
        self.__run_query(query)

    @staticmethod
    def mount_insert_paramters(interact, string_value) -> str:
        first = True
        for value in interact:
            if first:
                string_value = string_value + f"'{value}'"
                first = False
            else:
                string_value = string_value + ', ' + f"'{value}'"

        return string_value

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
            values_str, cols_values, objs_variables = '', '', vars(obj_model)
            model_table: str = objs_variables['modelTable']
            columns = []
            for item in objs_variables:
                if item not in ['id', 'modelCreated', 'modelTable']:
                    columns.append(item)

            values_str = self.mount_insert_paramters(
                obj_model.get_all_values(), values_str)

            cols_values = self.mount_insert_paramters(columns, cols_values)

            self.query = f'insert into {model_table} ({cols_values}) values({values_str})'
            self.__run_query(self.query)

        except ValueError as error:
            print(error)

    def update(self, obj_model):
        try:
            self.query = f'update {obj_model.modelTable()} set {obj_model.update_query_set()} where id= {obj_model.get_id()}'
            self.__run_query(self.query)
            self.query = None

        except ValueError as error:
            print(error)

    def delete(self, obj_model):
        try:
            self.query = f'DELETE FROM {obj_model.get_model_table()} WHERE id={obj_model.get_id()}'
            self.__run_query(self.query)

        except ValueError as error:
            print(error)

    def __run_query_with_return(self, query):
        try:
            self.cursor = self.connection.cursor()
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            self.connection.commit()

            return rows

        except Exception as error:
            print(error)

    def __run_query(self, query):
        try:
            self.cursor = self.connection.cursor()
            self.cursor.execute(query)
            self.connection.commit()

        except Exception as error:
            print(error)






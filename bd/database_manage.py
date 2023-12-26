import sqlite3 as sq


class Database:
    def __init__(self):
        self.connection = sq.connect("main_data_base.db")
        self.cursor = self.connection.cursor()

    def _get_data(self, table, get_data, parameter_data_name, parameter_data):
        self.cursor.execute(f'SELECT {get_data} FROM {table} WHERE {parameter_data_name} = ?', parameter_data)
        return self.cursor.fetchone()

    def _get_all_data(self, table):
        self.cursor.execute(f'SELECT * FROM {table}')
        return self.cursor.fetchall()

    def _get_all_data_by_parameter(self, table, parameter_data_name, parameter_data):
        self.cursor.execute(f"SELECT * FROM {table} WHERE {parameter_data_name} = ?", parameter_data)
        return self.cursor.fetchall()

    def _create_data(self, table, name_data, pattern_data, data):
        self.cursor.execute(f'INSERT INTO {table} {name_data} VALUES {pattern_data}', data)
        self.connection.commit()

    def _update_data(self, table, name_update_data, parameter_data_name, data):
        self.cursor.execute(f'UPDATE {table} SET {name_update_data} = ? WHERE {parameter_data_name} = ?', data)
        self.connection.commit()

    def _delete_data(self, table, parameter_data_name, parameter_data):
        self.cursor.execute(f'DELETE FROM {table} WHERE {parameter_data_name} = ?', parameter_data)
        self.connection.commit()



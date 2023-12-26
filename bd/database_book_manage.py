from database_manage import Database


class Book(Database):
    def get_username(self, table_id):
        return self._get_data('book', 'username', 'table_id', (table_id,))[0]

    def get_all(self):
        return self._get_all_data('book')

    def change_name(self, table_id, new_username):
        self._update_data('book', 'username', 'table_id', (new_username, table_id))

    def get_all_tables(self, username):
        return self._get_all_data_by_parameter('book', 'username', (username,))

    def table_is_booked(self, table_id):
        try:
            if self.get_username(table_id) != None:
                return True
            else:
                return False
        except TypeError:
            return False

    def clear_book(self, table_id):
        self._update_data('book', 'username', 'table_id', (None, table_id))

    def get_max_table_id(self):
        data = self.get_all()
        sort_list = []
        for i in data:
            sort_list.append(i[1])
        try:
            return max(sort_list)
        except ValueError:
            return 0

    def create_book(self, username, table_id):
        if self.table_is_booked(table_id) == False:
            self._create_data('book', '(username, table_id)', '(?, ?)', (username, table_id))
        else:
            print('Столик уже заказан!')

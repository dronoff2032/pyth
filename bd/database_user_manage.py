from database_manage import Database



class User(Database):
    def get_password(self, username):
        return self._get_data('users', 'password', 'username', (username,))[0]

    def get_access_level(self, username):
        return self._get_data('users', 'access_level', 'username', (username,))[0]

    def get_balance(self, username):
        return self._get_data('users', 'balance', 'username', (username,))[0]

    def get_all_users(self):
        return self._get_all_data('users')

    def user_exist(self, username):
        if self._get_data('users', 'username', 'username', (username,)) != None:
            return True
        else:
            return False

    def change_username(self, username, new_username):
        self._update_data('users', 'username', 'username', (new_username, username))

    def change_password(self, username, new_password):
        self._update_data('users', 'password', 'username', (new_password, username))

    def change_access_level(self, username, new_access_level):
        self._update_data('users', 'access_level', 'username', (new_access_level, username))

    def change_balance(self, username, new_balance):
        self._update_data('users', 'balance', 'username', (new_balance, username))

    def delete_user(self, username):
        self._delete_data('users', 'username', (username,))

    def create_user(self, username, password, access_level, balance):
        if not self.user_exist(username):
            self._create_data('users', '(username, password, access_level, balance)', '(?, ?, ?, ?)', (username, password, access_level, balance))
        else:
            print('Такой пользователь уже существует!')
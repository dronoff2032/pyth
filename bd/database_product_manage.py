from database_manage import Database


class Product(Database):
    def get_cost(self, product_name):
        try:
            return self._get_data('products', 'cost', 'product_name', (product_name,))[0]
        except TypeError:
            return 0

    def get_all_products(self):
        return self._get_all_data('products')

    def product_exist(self, product_name):
        if self._get_data('products', 'product_name', 'product_name', (product_name,)) != None:
            return True
        else:
            return False

    def change_cost(self, product_name, new_cost):
        self._update_data('products', 'cost', 'product_name', (new_cost, product_name))

    def delete_product(self, product_name):
        self._delete_data('products', 'product_name', (product_name,))

    def create_product(self, product_name, cost):
        if self.product_exist(product_name) == False:
            self._create_data('products', '(product_name, cost)', '(?, ?)', (product_name, cost))
        else:
            print('Такой пользователь уже существует!')
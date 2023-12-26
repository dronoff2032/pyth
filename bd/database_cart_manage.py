from database_manage import Database


class Cart(Database):
    def get_all(self):
        return self._get_all_data('cart')

    def get_all_orders_in_cart(self, username):
        return self._get_all_data_by_parameter('cart', 'username', (username,))

    def order_in_cart_exist(self, username, product):
        if self._get_data('cart', 'product', 'username = ? AND product', (username, product)) != None:
            return True
        else:
            return False

    def delete_order(self, username, product):
        self._delete_data('cart', 'username = ? AND product', (username, product))

    def create_order(self, username, product):
        if self.order_in_cart_exist(username, product) == False:
            self._create_data('cart', '(username, product)', '(?, ?)', (username, product))
        else:
            print('Такой заказ в корзине уже существует!')

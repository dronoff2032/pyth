import database_user_manage, database_product_manage, database_cart_manage, database_book_manage
db_user = database_user_manage.User()
db_product = database_product_manage.Product()
db_cart = database_cart_manage.Cart()
db_book = database_book_manage.Book()
import uuid
import random

some_random_string = str(uuid.uuid4())
some_random_int = random.randint(100000000000000000000, 1000000000000000000000)
username = some_random_string
password = some_random_string
access_level = some_random_string
balance = 0


def auth():
    global some_random_string
    global username
    global password
    global access_level
    global balance

    print('\n\n\n\n\nДобро пожаловать в ресторан! Выберите что хотите сделать, введя число нужного действия. \n - Зарегестрироваться (1) \n - Войти (2) \n - Выйти из программы (3) ')

    first_choice = ''
    while first_choice not in ['1', '2', '3']:
        first_choice = str(input('Ввод: '))

    if first_choice == '1':
        print('\n\n\n\n\nВы выбрали регистрацию. Нажмите клавишу Enter чтобы перейти назад.')
        while db_user.user_exist(username) or username == some_random_string and username != '':
            username = input('Введите имя пользователя: ')
            if db_user.user_exist(username):
                print(f'Имя пользователя "{username}" уже существует!')
        if username == '':
            username = some_random_string
            auth()
        print(f'\n\n\n\n\nВы выбрали имя пользователя {username}. Придумайте пароль больше 8 символов и меньше 64.')
        while len(password) < 8 or len(password) > 64 or password == some_random_string:
            password = input('Введите пароль: ')
            if len(password) < 8 or len(password) > 64:
                print('Пароль должен быть больше 8 символов и меньше 64.')
        db_user.create_user(username, password, 1, 0)
        print(f'Вы успешно зарегестрировались как {username}. Нажмите Enter чтобы перейти на главное меню.')
        username = some_random_string
        password = some_random_string
        input()
        auth()
    elif first_choice == '2':
        print('\n\n\n\n\nВы выбрали вход. Нажмите клавишу Enter чтобы перейти назад.')
        while not db_user.user_exist(username) and username != '':
            username = input('Введите имя пользователя: ')
            if not db_user.user_exist(username) and username != '':
                print(f'Имя пользователя "{username}" не существует!')
        if username == '':
            username = some_random_string
            auth()
        print(f'\n\n\n\n\nВведите пароль для имени пользователя {username} или нажмите Enter чтобы перейти на главное меню.')
        while password != db_user.get_password(username) and password != '':
            password = input('Введите пароль: ')
            if password != db_user.get_password(username):
                print('Неверный пароль!')
        if password == '':
            username = some_random_string
            password = some_random_string
            auth()
        access_level = db_user.get_access_level(username)
        balance = db_user.get_balance(username)
        print(f'Вы успешно вошли как "{username}"! Нажмите Enter чтобы продолжить.')
        input()
        main_page()

    elif first_choice == '3':
        exit(0)

def main_page():
    global some_random_string
    global username
    global password
    global access_level
    global balance
    print(f'\n\n\n\n\nДобро пожаловать в ресторан! Ваш баланс составляет {balance} рублей. Введите номер действия из списка ниже. ')
    print(' - Заказать еду (1) \n - Просмотреть список заказаной еды (2) \n - Забронировать столик (3) \n - Просмотреть список забронированых столиков (4)')
    main_page_choice = 0
    if access_level == 0:
        print(' - Управление пользователями (5) \n - Управление списком продуктов (6) \n - Управление заказами еды (7) \n - Управление забронироваными столиками (8) \n - Настройки аккаунта (9) \n - Выйти (10)')
        while main_page_choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
            main_page_choice = str(input('Ввод: '))
            if main_page_choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
                print('Выберите число 1-9.')
        if main_page_choice == '5':
            users_manage()
        elif main_page_choice == '6':
            products_manage()
        elif main_page_choice == '7':
            food_order_manage()
        elif main_page_choice == '8':
            book_manage()
        elif main_page_choice == '9':
            manage_account()
        elif main_page_choice == '10':
            password = some_random_string
            username = some_random_string
            auth()
    elif access_level == 1:
        print(' - Настройки аккаунта (5) \n - Выйти (6)')
        while main_page_choice not in ['1', '2', '3', '4', '5', '6']:
            main_page_choice = str(input('Ввод: '))
            if main_page_choice not in ['1', '2', '3', '4', '5', '6']:
                print('Выберите число 1-6.')
        if main_page_choice == '5':
            manage_account()
        elif main_page_choice == '6':
            password = some_random_string
            username = some_random_string
            auth()
    if main_page_choice == '1':
        order_product()
    elif main_page_choice == '2':
        manage_orders()

    elif main_page_choice == '3':
        book_table()

    elif main_page_choice == '4':
        book_manage()


def order_product():
    global username
    global balance
    print('Хотите ли вы отсортировать список по цене? \n - Да \n - Нет')
    sort_choose = ''
    while sort_choose not in ['Да', 'Нет']:
        sort_choose = input('Введите решение: ')
    print(f'\n\n\n\n\nВыберите позицию из меню, которую вы хотите заказать и напишите её название. Если хотите вернутся назад то нажмите Enter.')
    products = db_product.get_all_products()
    if sort_choose == 'Да':
        products = sorted(products, key=lambda x: x[1])
    for i in products:
        print(f'\nНаименование позиции: {i[0]}. Цена: {i[1]} рублей')
    products_names_list = []
    for i in products:
        products_names_list.append(i[0])
    order_product_choose = some_random_string
    while order_product_choose not in products_names_list and order_product_choose != '':
        order_product_choose = input('Ввод: ')
        if order_product_choose not in products_names_list:
            print('Товар не найден в списке!')
    if order_product_choose == '':
        order_product_choose = some_random_string
        main_page()
    if db_product.get_cost(order_product_choose) > balance:
        order_product_choose = some_random_string
        print('Недостаточно средств на счете! Нажмите Enter чтобы вернутся.')
        input()
        main_page()
    elif db_cart.order_in_cart_exist(username, order_product_choose):
        order_product_choose = some_random_string
        print('Вы уже приобретали данную позицию! Нажмите Enter чтобы вернутся.')
        input()
        main_page()
    else:
        db_cart.create_order(username, order_product_choose)
        balance -= db_product.get_cost(order_product_choose)
        db_user.change_balance(username, balance)
        print(f'Вы успешно приобрели позицию "{order_product_choose}". Вы потратили {db_product.get_cost(order_product_choose)} рублей. Нажмите Enter чтобы вернутся.')
        input()
        order_product_choose = some_random_string
        main_page()

def manage_orders():
    global username
    print(f'\n\n\n\n\nЕсли вы хотите отменить какой-либо заказ то введите его название, или если хотите вернутся назад то нажмите Enter.')
    orders = db_cart.get_all_orders_in_cart(username)
    for i in orders:
        print(f' - {i[1]}')
    orders_name_list = []
    for i in orders:
        orders_name_list.append(i[1])
    manage_orders_choose = some_random_string
    while manage_orders_choose not in orders_name_list and manage_orders_choose != '':
        manage_orders_choose = input('Ввод: ')
        if manage_orders_choose not in orders_name_list:
            print('Позиция не найдена среди ваших заказов.')
    if manage_orders_choose == '':
        manage_orders_choose = some_random_string
        main_page()
    db_cart.delete_order(username, manage_orders_choose)
    print(f'Вы успешно отменили заказ "{manage_orders_choose}". Нажмите Enter чтобы вернутся.')
    input()
    manage_orders_choose = some_random_string
    main_page()

def book_table():
    print(f'\n\n\n\n\nВыберите столик который вы хотите забронировать и напишите его номер. Если хотите вернутся назад то нажмите Enter.')
    book = sorted(db_book.get_all(), key=lambda x: x[1])
    sorted_book = list(map(lambda x: ('Занят' if x[0] is not None and x[0] != '' else 'Свободен', x[1]), book))
    for i in sorted_book:
        print(f' - Номер столика: {i[1]}, статус - "{i[0]}"')
    book_id_list = []
    for i in book:
        book_id_list.append(str(i[1]))
    book_table_choose = some_random_string
    def check(book_table_choose):
        if book_table_choose == '':
            return False
        elif book_table_choose not in book_id_list or db_book.table_is_booked(book_table_choose):
            return True
    while check(book_table_choose):
        book_table_choose = input('Ввод: ')
        if book_table_choose not in book_id_list:
            print('Введите номер стола для брони!')
        elif db_book.table_is_booked(book_table_choose):
            print('Столик уже забронирован!')
    if book_table_choose == '':
        book_table_choose = some_random_string
        main_page()
    db_book.change_name(book_table_choose, username)
    print(f'Вы успешно заказали столик "{book_table_choose}". Нажмите Enter чтобы вернутся.')
    input()
    book_table_choose = some_random_string
    main_page()

def book_manage():
    print(f'\n\n\n\n\nЕсли вы хотите отменить бронь для одного из столиков напишите его номер. Если хотите вернутся назад то нажмите Enter.')
    booked_tables = db_book.get_all_tables(username)
    booked_tables_result = ''
    for i in booked_tables:
        booked_tables_result += f'{i[1]} '
    print(f'Список номеров заказанных столиков: {booked_tables_result}')
    booked_tables_id = []
    for i in booked_tables:
        booked_tables_id.append(str(i[1]))
    booked_tables_id.append('')
    book_manage_choose = some_random_int
    while book_manage_choose not in booked_tables_id:
        book_manage_choose = str(input('Ввод: '))
        if book_manage_choose not in booked_tables_id:
            print('Введите id из списка!')
    if book_manage_choose == '':
        book_manage_choose = some_random_int
        main_page()
    else:
        db_book.clear_book(book_manage_choose)
        print(f'Вы отменили заказ "{book_manage_choose}". Нажмите Enter чтобы продолжить.')
        input()
        book_manage_choose = some_random_int
        main_page()

def manage_account():
    global username
    print(f'\n\n\n\n\nВыберите номер действия или если хотите вернутся назад, то нажмите Enter. \n - Изменить имя пользователя (1) \n - Изменить пароль (2) \n - Пополнить счет (3)')
    manage_account_choose = some_random_string
    while manage_account_choose not in ['1', '2', '3', '']:
        manage_account_choose = str(input('Ввод: '))
        if manage_account_choose not in ['1', '2', '3', '']:
            print('Введите число: ')
    if manage_account_choose == '':
        manage_account_choose = some_random_string
        main_page()
    elif manage_account_choose == '1':
        print(f'\n\n\n\n\nВы выбрали изменение имени пользователя. Введите новое или нажмите Enter чтобы выйти.')
        change_username_choose = some_random_string
        while db_user.user_exist(change_username_choose) or change_username_choose == some_random_string and change_username_choose != '':
            change_username_choose = input('Введите новое имя пользователя: ')
            if db_user.user_exist(change_username_choose):
                print('Это имя пользователя уже существует!')
        if change_username_choose == '':
            manage_account_choose = some_random_string
            change_username_choose = some_random_string
            main_page()
        else:
            db_user.change_username(username, change_username_choose)
            print(f'Вы успешно сменили имя пользователя с "{username}" на "{change_username_choose}". Нажмите Enter чтобы пройти дальше.')
            username = change_username_choose
            input()
            change_username_choose = some_random_string
            manage_account_choose = some_random_string
            main_page()
    elif manage_account_choose == '2':
        global password
        print(f'\n\n\n\n\nВы выбрали изменение пароля. Введите новый или нажмите Enter чтобы выйти.')
        change_password_choose = some_random_string
        while len(change_password_choose) < 8 or len(change_password_choose) > 64 and change_password_choose == some_random_string and change_password_choose != '':
            change_password_choose = input('Выберите новый пароль: ')
            if len(change_password_choose) < 8 or len(change_password_choose) > 64:
                print('Пароль должен быть больше 8 символов и меньше 64.')
        if change_password_choose == '':
            change_password_choose = some_random_string
            main_page()
        else:
            db_user.change_password(username, change_password_choose)
            password = change_password_choose
            print(f'Пароль для аккаунта "{username}" был изменен! Нажмите Enter чтобы выйти.')
            input()
            change_password_choose = some_random_string
            main_page()
    elif manage_account_choose == '3':
        global balance
        print(f'\n\n\n\n\nВы выбрали пополнение счета. Введите сумму пополнения.')
        change_balance_choose = some_random_int
        while change_balance_choose < 1 or change_balance_choose == some_random_int:
            try:
                change_balance_choose = int(input('Введите сумму пополнения: '))
            except ValueError:
                print('Введите целое число!')
            if change_balance_choose < 1:
                print('Введите сумму больше 0!')
        db_user.change_balance(username, balance+change_balance_choose)
        balance += change_balance_choose
        print('Выполняется запрос в банк...')
        print('Ответ получен: операция подтверждена.')
        print(f'Вы пополнили счет на {change_balance_choose} рублей, теперь ваш новый баланс равен {balance} рублей. Нажмите Enter чтобы выйти.')
        input()
        manage_account_choose = some_random_string
        change_balance_choose = some_random_int
        main_page()

def users_manage():
    print(f'\n\n\n\n\nВы хотите создать нового пользователя или редактировать существующих? Выбеите вариант ответа или нажмите Enter чтобы выйти. \nСоздать нового (1) \nРедактировать существующего (2)')
    users_create_choose = some_random_string
    while users_create_choose not in ['1', '2', '']:
        users_create_choose = str(input('Ввод: '))
    if users_create_choose == '':
        users_create_choose = some_random_string
        main_page()
    elif users_create_choose == '2':
        print(f'\n\n\n\n\nСтраница управления пользователями. Введите имя пользователя для редактирования.')
        users = db_user.get_all_users()
        for i in users:
            print(f' - Имя пользователя {i[0]}, Пароль: {i[1]}, Уровень доступа: {i[2]}, Баланс: {i[3]}')
        users_name_list = []
        for i in users:
            users_name_list.append(i[0])
        user_edit_choose = some_random_string
        while user_edit_choose not in users_name_list and user_edit_choose != '':
            user_edit_choose = str(input('Введите имя пользователя: '))
            if user_edit_choose not in users_name_list:
                print('Введите существующего пользователя!')
        print(f'Вы выбрали пользователя {user_edit_choose}. Выберите что хотите сделать или нажмите Enter чтобы выйти. \n - Изменить имя пользователя (1) \n - Изменить пароль пользователя (2) \n - Изменение уровня доступа (3) \n - Изменить баланс пользователя (4) \n - Удалить пользователя (5)')
        user_edit_choose_2 = ''
        while user_edit_choose_2 not in ['1', '2', '3', '4', '5']:
            user_edit_choose_2 = str(input('Ввод: '))
            if user_edit_choose_2 not in ['1', '2', '3', '4', '5']:
                print('Введите число от 1 до 5.')
            if user_edit_choose_2 == '1':
                print(f'\n\n\n\n\nВведите новое имя пользователя.')
                new_username = some_random_string
                while new_username == some_random_string or db_user.user_exist(new_username):
                    new_username = str(input('Ввод: '))
                    if db_user.user_exist(new_username):
                        print('Такой пользователь уже суествует.')
                db_user.change_username(user_edit_choose, new_username)
                print(f'Изменено имя пользователя с {user_edit_choose} на {new_username}. Нажмите Enter чтобы выйти.')
                input()
                users_create_choose = some_random_string
                user_edit_choose = some_random_string
                new_username = some_random_string
                main_page()
            elif user_edit_choose_2 == '2':
                print(f'\n\n\n\n\nВведите новый пароль.')
                new_password = some_random_string
                while new_password == some_random_string or len(new_password) < 8 or len(new_password) > 64:
                    new_password = str(input('Ввод: '))
                    if len(new_password) < 8 or len(new_password) > 64:
                        print('Пароль долен быть больше 8 и меньше 64 символов.')
                db_user.change_password(user_edit_choose, new_password)
                print(f'Пароль пользователя {user_edit_choose} был изменен. Нажмите Enter чтобы выйти.')
                input()
                users_create_choose = some_random_string
                user_edit_choose = some_random_string
                new_password = some_random_string
                main_page()
            elif user_edit_choose_2 == '3':
                print(f'\n\n\n\n\nВыберите уровень доступа: 0 (высший), 1 (покупатель).')
                new_access_level = some_random_string
                while new_access_level == some_random_string or new_access_level not in ['0', '1']:
                    new_access_level = str(input('Ввод: '))
                    if new_access_level not in ['0', '1']:
                        print('Введите корректный уровень доступа.')
                db_user.change_access_level(user_edit_choose, new_access_level)
                print(f'Уровень доустпа пользователя {user_edit_choose} был изменен. Нажмите Enter чтобы выйти.')
                input()
                user_edit_choose_2 = ''
                main_page()
            elif user_edit_choose_2 == '4':
                print(f'\n\n\n\n\nВведите новый баланс пользователя.')
                new_balance = some_random_int
                while new_balance < 1 or new_balance == some_random_int:
                    try:
                        new_balance = int(input('Введите сумму пополнения: '))
                    except ValueError:
                        print('Введите целое число!')
                    if new_balance < 1:
                        print('Введите сумму больше 0!')
                db_user.change_balance(user_edit_choose, new_balance)
                print(f'Баланс пользователя {user_edit_choose} был установлен значение {new_balance}. Нажмите Enter чтобы выйти.')
                input()
                user_edit_choose_2 = ''
                new_balance = some_random_int
                main_page()
            elif user_edit_choose_2 == '5':
                db_user.delete_user(user_edit_choose)
                print(f'Пользователь {user_edit_choose} был удален. Нажмите Enter чтобы выйти.')
                input()
                user_edit_choose = some_random_string
                main_page()
    elif users_create_choose == '1':
        create_user()

def create_user():
    print('\n\n\n\n\nВведите имя пользователя.')
    create_username = some_random_string
    while create_username == some_random_string or db_user.user_exist(create_username):
        create_username = str(input('Ввод: '))
        if db_user.user_exist(create_username):
            print('Такой пользователь уже существует.')
    print(f'Выбрано имя пользователя "{create_username}". \nВведите пароль пользователя.')
    create_password = some_random_string
    while create_password == some_random_string or len(create_password) < 8 or len(create_password) > 64:
        create_password = str(input('Ввод: '))
        if len(create_password) < 8 or len(create_password) > 64:
            print('Пароль долен быть больше 8 и меньше 64 символов.')
    print(f'Вы выбрали пароль пользователя. Выберите уровень доступа пользователя 0 (высший), 1 (покупатель).')
    create_access_level = some_random_string
    while create_access_level == some_random_string or create_access_level not in ['0', '1']:
        create_access_level = str(input('Ввод: '))
        if create_access_level not in ['0', '1']:
            print('Введите корректный уровень доступа.')
    print(f'Вы выбрали уровень доступа {create_access_level}. Введите баланс пользователя.')
    create_balance = some_random_int
    while create_balance < 1 or create_balance == some_random_int:
        try:
            create_balance = int(input('Введите баланс: '))
        except ValueError:
            print('Введите целое число!')
        if create_balance < 1:
            print('Введите сумму больше 0!')
    print(f'Вы установили баланс {create_balance}. \nБыл создан аккаунт {create_username}. Нажмите Enter чтобы выйти.')
    db_user.create_user(create_username, create_password, create_access_level, create_balance)
    input()
    create_username = some_random_string
    create_password = some_random_string
    create_access_level = some_random_string
    create_balance = some_random_int
    main_page()

def products_manage():
    print(f'\n\n\n\n\nВы хотите создать новый продукт или редактировать существующие? Выбеите вариант ответа или нажмите Enter чтобы выйти. \nСоздать новый (1) \nРедактировать существующий (2)')
    products_create_choose = some_random_string
    while products_create_choose not in ['1', '2', '']:
        products_create_choose = str(input('Ввод: '))
    if products_create_choose == '':
        products_create_choose = some_random_string
        main_page()
    elif products_create_choose == '1':
        print(f'\n\n\n\n\nВы выбрали создание новой продуктовой позиции. Введите наименование.')
        create_product_name = some_random_string
        while create_product_name == some_random_string or db_product.product_exist(create_product_name):
            create_product_name = str(input('Введите наименование: '))
            if db_product.product_exist(create_product_name):
                print('Такой продукт уже  существует!')
        print(f'Вы выбрали "{create_product_name}". \nВведите стоимость.')
        create_cost = some_random_int
        while create_cost < 1 or create_cost == some_random_int:
            try:
                create_cost = int(input('Ввод: '))
            except ValueError:
                print('Введите целое число!')
            if create_cost < 1:
                print('Введите сумму больше 0!')
        db_product.create_product(create_product_name, create_cost)
        print(f'Создана позиция продукта под названием "{create_product_name}" и с ценой {create_cost} рублей. \nНажмите Enter чтобы выйти.')
        input()
        create_product_name = some_random_string
        create_cost = some_random_int
        main_page()

    elif products_create_choose == '2':
        print('\n\n\n\n\nВы выбрали страницу управления существующими позициями продуктов. Введите имя продукта для редактирования или нажмите Enter чтобы выйти.')
        products = db_product.get_all_products()
        for i in products:
            print(f'Имя продукта: "{i[0]}", стоимость: {i[1]} рублей')
        products_name_list = []
        for i in products:
            products_name_list.append(i[0])
        current_product = some_random_string
        while current_product not in products_name_list and current_product != '':
            current_product = str(input('Ввод: '))
            if current_product not in products_name_list:
                print('Введите позицию из списка!')
        print(f'\n\n\n\n\nВы выбрали позицию для редактирования "{current_product}". Выберите что хотите сделать: \n - Изменить стоимость (1) \n - Удалить позицию (2)')
        products_create_choose_2 = some_random_string
        while products_create_choose_2 not in ['1', '2'] or products_create_choose_2 == some_random_string:
            products_create_choose_2 = str(input('Ввод: '))
            if products_create_choose_2 not in ['1', '2']:
                print('Введите число 1 или 2!')
        if products_create_choose_2 == '1':
            print('\n\n\n\n\nВы выбрали изменение стоимости позиции. Введите новую.')
            new_cost = some_random_int
            while new_cost < 1 or new_cost == some_random_int:
                try:
                    new_cost = int(input('Введите стоимость: '))
                except ValueError:
                    print('Введите целое число!')
                if new_cost < 1:
                    print('Введите сумму больше 0!')
            db_product.change_cost(current_product, new_cost)
            print(f'Вы изменили стоимость позиции {current_product}, на {new_cost}. Нажмите Enter чтобы выйти.')
            input()
            new_cost = some_random_int
            current_product = some_random_string
            main_page()
        elif products_create_choose_2 == '2':
            db_product.delete_product(current_product)
            print(f'Позиция "{current_product}" была успешно удалена. Нажмите Enter чтобы выйти.')
            input()
            main_page()

def food_order_manage():
    print(f'\n\n\n\n\nВы хотите зарегестрировать новый заказ или просмотреть существующие? Выбеите вариант ответа или нажмите Enter чтобы выйти. \nЗаказать новый (1) \nРедактировать существующий (2)')
    food_order_create_choose = some_random_string
    while food_order_create_choose not in ['1', '2', '']:
        food_order_create_choose = str(input('Ввод: '))
    if food_order_create_choose == '':
        food_order_create_choose = some_random_string
        main_page()
    elif food_order_create_choose == '1':
        print('\n\n\n\n\nВы выбрали регестрирование нового заказа. Введите имя пользователя, на которое вы хотите сделать заказ или нажмите Enter чтобы выйти.')
        create_user = some_random_string
        while create_user == some_random_string or not db_user.user_exist(create_user) and create_user != '':
            create_user = str(input('Ввод: '))
            if not db_user.user_exist(create_user):
                print('Такой пользователь не существует!')
        if create_user == '':
            create_user = some_random_string
            main_page()
        else:
            print(f'Вы выбрали имя пользователя "{create_user}". \nВведите наименование позиции, которую вы хотите заказать.')
            create_product = some_random_string
            while create_user == some_random_string or not db_product.product_exist(create_product):
                create_product = str(input('Ввод: '))
                if not db_product.product_exist(create_product):
                    print('Такой продукт не существует!')
            db_cart.create_order(create_user, create_product)
            print(f'На имя пользователя "{create_user}" был заказан продукт "{create_product}". Нажмите Enter чтобы выйти.')
            input()
            create_user = some_random_string
            create_product = some_random_string
            main_page()
    elif food_order_create_choose == '2':
        print('\n\n\n\n\nВы выбрали просмотр существующих заказов. Введите имя пользователя чтобы отфильтровать только его заказы или нажмите Enter чтобы выйти.')
        food_orders = db_cart.get_all()
        for i in food_orders:
            print(f'Наименование продукта: "{i[1]}", имя пользователя заказчика: "{i[0]}"')
        food_orders_username_list = []
        for i in food_orders:
            food_orders_username_list.append(i[0])
        current_username = some_random_string
        while current_username not in food_orders_username_list and current_username != '':
            current_username = str(input('Ввод: '))
            if current_username not in food_orders_username_list:
                print('Введите имя пользователя из списка!')
        if current_username == '':
            current_username = some_random_string
            main_page()
        else:
            print(f'\n\n\n\n\nВыберите заказ который хотите отменить или нажмите Enter чтобы выйти.')
            users_food_orders = db_cart.get_all_orders_in_cart(current_username)
            for i in users_food_orders:
                print(f' - {i[1]}')
            users_food_orders_names = []
            for i in users_food_orders:
                users_food_orders_names.append(i[1])
            current_product = some_random_string
            while current_product not in users_food_orders_names and current_product != '':
                current_product = str(input('Ввод: '))
                if current_product not in users_food_orders_names:
                    print('Введите продукт для отмены из списка!')
            if current_product == '':
                current_product = some_random_string
                main_page()
            else:
                db_cart.delete_order(current_username, current_product)
                print(f'Продукт "{current_product}" был удален из заказов пользователя "{current_username}". Нажмите Enter чтобы выйти.')
                input()
                current_product = some_random_string
                current_username = some_random_string
                main_page()

def book_manage():
    print(f'\n\n\n\n\nВы хотите забронировать новый столик или просмотреть существующие? Выбеите вариант ответа или нажмите Enter чтобы выйти. \nЗабронировать новый новый (1) \nРедактировать существующий (2)')
    book_create_choose = some_random_string
    while book_create_choose not in ['1', '2', '']:
        book_create_choose = str(input('Ввод: '))
    if book_create_choose == '':
        book_create_choose = some_random_string
        main_page()
    elif book_create_choose == '1':
        print('\n\n\n\n\nВы выбрали регистрацию новой брони. Введите номер столика Enter чтобы выйти.')
        current_table_id_create = some_random_int
        create_books = db_book.get_all()
        books_ids = []
        for i in create_books:
            books_ids.append(str(i[1]))
        while current_table_id_create not in books_ids and current_table_id_create != '':
            current_table_id_create = str(input('Ввод: '))
        print(f'Вы выбрали место под номером {current_table_id_create}. Введите имя пользователя, на которого хотите забронировать столик.')
        create_user = some_random_string
        while create_user == some_random_string or not db_user.user_exist(create_user):
            create_user = str(input('Ввод: '))
            if not db_user.user_exist(create_user):
                print('Такой пользователь не существует!')
        db_book.create_book(create_user, current_table_id_create)
        print(f'Столик под номером {current_table_id_create} был забронирован для пользователя "{create_user}". Нажмите Enter чтобы выйти.')
        input()
        book_create_choose = some_random_string
        create_user = some_random_string
        main_page()



    elif book_create_choose == '2':
        print('\n\n\n\n\nВы выбрали редактирование существующей брони. Введите номер столика для удаления или нажмите Enter чтобы выйти.')
        books = db_book.get_all()
        sorted_books = list(filter(lambda x: x[0] is not None, books))
        for i in sorted_books:
            print(f'Имя пользователя "{i[0]}", номер столика: {i[1]}')
        books_table_ids = []
        for i in sorted_books:
            books_table_ids.append(f"{i[1]}")
        current_table_id = some_random_string
        while current_table_id not in books_table_ids and current_table_id != '':
            current_table_id = str(input('Ввод: '))
            if current_table_id not in books_table_ids and current_table_id != '':
                print('Введите номер столика из списка!')
        if current_table_id == '':
            current_table_id = some_random_string
            main_page()
        else:
            db_book.clear_book(current_table_id)
            print(f'Для столика под номером {current_table_id} была отменена бронь, нажмите Enter чтобы выйти.')
            input()
            current_table_id = some_random_string
            main_page()

auth()
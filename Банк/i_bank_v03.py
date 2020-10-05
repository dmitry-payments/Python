import datetime

EMPLOYEE_PASSWORD = "123"


class Transaction:
    TRANSFER = 1
    PUT_ACCOUNT = 2
    WITHDRAW = 3

    def __init__(self, type, amount, target=None):
        self.type = type
        self.date = datetime.datetime.now()
        self.amount = amount
        self.target = target

    def get_info(self):
        return f"{self.date} {self.type}: {self.amount} руб."


class Account:
    def __init__(self, name, surname, passport8, birth_date, phone_number, start_balance=0):
        self.name = name
        self.surname = surname
        self.passport8 = passport8
        self.birth_date = birth_date
        self.phone_number = phone_number
        self.balance = start_balance
        self.history = []

    def transfer(self, target_accaunt, amount):
        if self.balance >= amount:
            self.balance -= amount
            target_accaunt.balance += amount

            transaction = Transaction(Transaction.TRANSFER, amount, target_accaunt)
            self.history.append(transaction)
            return True
        return False

    def get_info(self):
        # Иванов И.баланс: 21283 руб
        return f"{self.surname} {self.name[0]}. баланс: {self.balance} руб."


class CreditAccount(Account):
    def __init__(self, name, surname, passport8, birth_date, phone_number, credit_limit, start_balance=0):
        # Account.__init__(name, surname, passport8, birth_date, phone_number, start_balance)
        super().__init__(name, surname, passport8, birth_date, phone_number, start_balance)
        self.credit_limit = credit_limit

    def transfer(self, target_accaunt, amount):
        if self.balance + self.credit_limit >= amount:
            self.balance -= amount
            target_accaunt.balance += amount
            return True
        return False

    def get_info(self):
        return f"<K> {super().get_info()}"


def start_menu():
    while True:
        print("Укажите вашу роль:")
        print("1. Сотрудник банка")
        print("2. Клиент")
        print("3. Завершить работу")

        choice = input(":")
        if choice == "3":
            break
        elif choice == "1":
            if employee_access():
                employee_menu()
            else:
                print("Указан неверный пароль, укажите роль и повторите попытку...")
        elif choice == "2":
            account = client_access(accounts)
            if account:
                client_menu(account)
            else:
                print("Указан несуществующий пасспорт, укажите роль и повторите попытку...")
        else:
            print("Указан некорректный пункт меню, повторите выбор...")


def employee_access():
    password = input("Пароль: ")
    if password == EMPLOYEE_PASSWORD:
        return True

    return False


def client_access(accounts):
    """
    Находит аккаунт с введеным номером паспорта
    Или возвращает False, если аккаунт не найден
    """
    try:
        passport = int(input("Номер паспорта: "))
    except ValueError:
        return False
    for account in accounts:
        if passport == account.passport8:
            return account

    return False


def create_new_account():
    print("Укажите данные клиента")
    name = input("Имя:")
    surname = input("Фамилия:")
    passport = input("Номер паспорта: ")
    birth_day = input("Дата рождения: ")
    phone_number = input("Номер телефона: ")
    account = Account(name, surname, passport, birth_day, phone_number)
    accounts.append(account)


def create_new_credit_account():
    print("Укажите данные клиента")
    name = input("Имя:")
    surname = input("Фамилия:")
    passport = input("Номер паспорта: ")
    birth_day = input("Дата рождения: ")
    phone_number = input("Номер телефона: ")
    credit_limit = input("Кредитный лимит: ")
    account = CreditAccount(name, surname, passport, birth_day, phone_number, credit_limit)

    accounts.append(account)


def close_account():
    pass


def view_accounts_list():
    for account in accounts:
        print(account.get_info())


def view_account_by_passport():
    pass


def employee_menu():
    while True:
        print("***********Меню сотрудника*************")
        print("1. Создать новый счет")
        print("6. Создать новый кредитный счет")
        print("2. Закрыть счет")
        print("3. Посмотреть список счетов")
        print("4. Посмотреть счет по номеру паспорта")
        print("5. Exit")
        choice = input(":")
        if choice == "1":
            create_new_account()
        elif choice == "2":
            close_account()
        elif choice == "3":
            view_accounts_list()
        elif choice == "4":
            view_account_by_passport()
        elif choice == "5":
            return
        elif choice == "6":
            create_new_credit_account()

    # input("Press Enter")


def view_client_account():
    pass


def put_account():
    pass


def withdraw():
    """
    Снять со счета
    """


def transfer(account: Account):
    target_phone = input("Телефон целевого клиента: ")
    target_account = None

    for account in accounts:
        if target_phone == account.phone_number:
            target_account = account
            break

    if not target_account is None:
        amount = int(input("Сумма перевода: "))
        account.transfer(target_account, amount)
    else:
        print("Пользователь с указанным номером не найден")


def client_menu(account: Account):
    while True:
        print(f"***********Меню клиента {account.surname}*************")
        print("1. Состояние счета")
        print("2. Пополнить счет")
        print("3. Снять со счета")
        print("4. Перевести деньги другому клиенту банка")
        print("5. Exit")
        choice = input(":")
        if choice == "1":
            view_client_account()
        elif choice == "2":
            put_account()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            transfer(account)
        elif choice == "5":
            return
    # input("Press Enter")


if __name__ == "__main__":
    accounts = [
        Account("Иван", "Петров", 25478458, "12.04.1975", "+79206001245"),
        Account("Алексей", "Дроздов", 24578154, "10.11.1985", "+79226101447"),
        Account("Петр", "Груздев", 78402568, "02.11.1992", "+79236101442"),
        CreditAccount("Алексей", "Кредитный", 78402560, "02.11.1992", "+79236101440", 1200),
    ]
    start_menu()

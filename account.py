class Account:

    def __init__(self, account_name: str, account_balance=0) -> None:
        self.__account_name = account_name
        self.__account_balance = account_balance

    def deposit(self, amount) -> bool:
        if self.__account_balance > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount) -> bool:
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.__account_balance

    def get_name(self) -> str:
        return self.__account_name

class Account:
    """
    A class to represent bank account deposits and withdrawals
    """

    def __init__(self, account_name: str, account_balance=0) -> None:
        """
        :param account_name: Name of account owner
        :param account_balance: Starting amount of account
        """
        self.__account_name = account_name
        self.__account_balance = account_balance

    def deposit(self, amount: float) -> bool:
        """
        Method that increments the account balance by the specified amount
        :param amount: Amount to be added to account balance
        :return: Successful/unsuccessful deposit transaction
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Method that decrements account balance by specified amount
        :param amount: Amount to be withdrawn from account balance
        :return: Successful/unsuccessful withdrawal transaction
        """
        if amount <= 0:
            return False
        elif amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Method to access account balance
        :return: Amount in account balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method to access name of account owner
        :return: Name of account owner
        """
        return self.__account_name

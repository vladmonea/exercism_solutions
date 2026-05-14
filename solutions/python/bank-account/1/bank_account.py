import threading


class BankAccount(object):
    def __init__(self):
        self.is_account_open = False
        self.lock = threading.Lock()

    @property
    def balance(self):
        if self.is_account_open:
            return self._balance
        else:
            raise ValueError("Cannot view closed account balance!")

    @balance.setter
    def balance(self, value):
        if self.is_account_open:
            if value >= 0:
                self._balance = value
            else:
                raise ValueError("This is bankrupting us!")
        else:
            raise ValueError("Cannot change closed account balance!")

    def get_balance(self):
        return self.balance

    def open(self):
        if not self.is_account_open:
            self.is_account_open = True
            self.balance = 0
        else:
            raise ValueError("Cannot open already open account!")

    def deposit(self, amount):
        self.lock.acquire()
        if amount < 0:
            raise ValueError("Cannot withdraw negative sum!")
        self.balance += amount
        self.lock.release()

    def withdraw(self, amount):
        self.lock.acquire()
        if amount < 0:
            raise ValueError("Cannot withdraw negative sum!")
        self.balance -= amount
        self.lock.release()

    def close(self):
        self.balance = 0
        self.is_account_open = False

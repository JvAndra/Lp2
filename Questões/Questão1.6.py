class Account:
    
    def __init__(self, id, name, balance = 0):
        self.__id = id
        self.__name = name
        self.__balance = balance
    
    def get_id(self):
        return self.__id
    
    def get_balance(self):
        return self.__balance

    def get_name(self):
        return self.__name
    
    def credit(self, amount):
        self.__balance += amount
        return self.__balance
    
    def debit(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Amount exceeded Balance")
        return self.__balance
    
    def transferTo(self, another,amount):
        if isinstance(another,Account):
            if another.__id != self.__id:
                if amount <= self.__balance:
                    self.__balance -= amount
                    another.__balance += amount
                else:
                    print("Amount exceeded Balance")
            else:
                print("Não é possível transferir pra si mesmo.")
        return self.__balance 
    
    def __str__(self):
        return f"Conta [id = {self.__id}, nome = {self.__name}, saldo = {self.__balance}]"
    
a1 = Account("A101", "Tan Ah Teck", 88)
print(a1)
a2 = Account("A102", "Kumar")
print(a2)

print("ID:", a1.get_id())
print("Nome:", a1.get_name())
print("Saldo:", a1.get_balance())

a1.credit(100)
print(a1)
a1.debit(50)
print(a1)
a1.debit(500)
print(a1)

a1.transferTo(a2,100)
print(a1)
print(a2)
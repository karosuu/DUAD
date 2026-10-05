class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def add_money(self, balance):
        self.balance = self.balance + balance

    def withdraw(self, balance):
        if balance > 0 and balance <= self.balance:
            self.balance = self.balance - balance

        elif balance > self.balance:
            print("Fondos insuficientes")

        else:
            print("El monto que ingreso no es valido")


# Crea una cuenta nueva
class SavingAccount(BankAccount):
    def __init__(self, balance, min_balance):
        # Super inicializa el balance de la clase padre
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw(self, balance):
        if self.balance - balance <= self.min_balance:
            raise ValueError("No puede retirar mas del minimo.")

        else:
            # Ejecuta el withdraw de BankAccount usando balance y aplica las validaciones
            super().withdraw(balance)


# Solicita al usuario la cantidad de dinero a ingresar
def amount_to_add(my_account):
    print("----Agrega y retira dinero de la cuenta----")

    amount_to_add = float(input("Ingrese la cantidad que desea depositar: "))
    # Llama al método add_money del objeto my_account y le pasa la cantidad ingresada
    my_account.add_money(amount_to_add)


def withdraw_money(my_account):
    amount_to_withdraw = float(input("\nIngrese el monton que desea retirar: "))
    my_account.withdraw(amount_to_withdraw)


# Crea una cuenta bancaria con un balance inicial de 500
my_account = BankAccount(500)
saving_account = SavingAccount(my_account.balance, 100)
amount_to_add(saving_account)
print(f"El balance actual es: {saving_account.balance}")

try:
    withdraw_money(saving_account)
except ValueError as error:
    print(error)
print(f"El balance actual es: {saving_account.balance}")

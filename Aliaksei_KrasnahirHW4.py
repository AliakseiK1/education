#1. написать программу которая:
#    запрашивает у пользователя логин
#2. Есть **функция** котороя выводит сумму на счете
#3. Декорируем эту функцию декоратором который проверяет если пользовател - админ (получили на первом этапе, то выводит сумму счета (выполняет функ из п 2)
#4. Если не админ - Сумму не выводить (функцию даже не выполнять) а выводить - доступ запрещен 

user_name = str(input("\nИмя пользователя: ")) # Ввести имя пользователя

def account_ballance():
        print("23.34$") #создаём функцию, которая выводит захардкоданный баланс счёта

def decologin(account_balance):
   def wrapper_decorator():
    account_balance(user_name)
    if user_name == "Valera":
        print (account_balance)
    else: print("В доступе отказано!")
    return wrapper_decorator

@decologin
def account_balance(user_name):
    print(f'Hello {user_name}')
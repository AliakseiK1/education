#1. написать программу которая:
#    запрашивает у пользователя логин
#2. Есть **функция** котороя выводит сумму на счете
#3. Декорируем эту функцию декоратором который проверяет если пользовател - админ (получили на первом этапе, то выводит сумму счета (выполняет функ из п 2)
#4. Если не админ - Сумму не выводить (функцию даже не выполнять) а выводить - доступ запрещен 

user_name = str(input("\nИмя пользователя: ")) # Ввести имя пользователя

account_ballance = "23.34$"

#def account_ballance():
        #print("23.34$") #создаём функцию, которая выводит захардкоданный баланс счёта


#user = Valera - only admin for the application

def decologin(*args, **kwargs):
   def wrapper_decorator(*args, **kwargs):
    if user_name != "Valera":
        return "В доступе отказано!"
    return wrapper_decorator

@decologin
def account_ballance1():
    print(account_ballance)

account_ballance1()
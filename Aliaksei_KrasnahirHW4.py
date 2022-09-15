#1. написать программу которая:
#    запрашивает у пользователя логин
#2. Есть **функция** котороя выводит сумму на счете
#3. Декорируем эту функцию декоратором который проверяет если пользовател - админ (получили на первом этапе, то выводит сумму счета (выполняет функ из п 2)
#4. Если не админ - Сумму не выводить (функцию даже не выполнять) а выводить - доступ запрещен 

user_name = str(input("\nИмя пользователя: "))

#def account_ballance(*args, **kwargs):
#  if user_name == "admin":
#  print("23.34$") #создаём функцию, которая выводит захардкоданный баланс счёта

#user = admin - only admin for the application


def decologin(account_ballance):
   def wrapper_decorator(*args, **kwargs):
        if user_name != "admin":
            print ("В доступе отказано!")
            return
        value = account_ballance(*args, **kwargs)
        return value
   return wrapper_decorator

@decologin
def account_ballance():
    print("\nНа вашем балансе 23.34$")
account_ballance()
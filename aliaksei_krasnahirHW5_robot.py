#Homework related to calculation of robot movement


#Version 1 - Simplified

import math

print("\nДобро пожаловать в систему управления роботом!\n")
print("Для того, чтобы задать максимальные значения перемещения влево, вправо, вверх, вниз, введите значения ниже:\n")

up_steps_to_enter = int(input("\nУкажите, на сколько шагов вверх должен подняться робот (целое число): "))
down_steps_to_enter = int(input("\nУкажите, на сколько шагов вниз должен опуститься робот (целое число): "))
left_steps_to_enter = int(input("\nУкажите, на сколько шагов влево должен сместиться робот (целое число): "))
right_steps_to_enter = int(input("\nУкажите, на сколько шагов вправо должен подняться робот (целое число): "))

side_a = up_steps_to_enter - down_steps_to_enter

side_b = left_steps_to_enter - right_steps_to_enter

hypotenuse_с = int(math.sqrt(side_a ** 2 + side_b ** 2))
#hypotenuse_с = str(hypotenuse_с)
print("\nРобот отошел на расстояние, равное {0} шаг(ов)" .format(hypotenuse_с))

"""
#Version 2 - advanced

import array


spisok = []
input_value = input("\nУкажите, на сколько шагов сместиться роботу согласно правилам ниже:"
+ "\n - 1. Сместиться вверх = \'U*\', где \'*\' - любое целое число"
+ "\n - 2. Сместиться вниз = \'D*\', где \'*\' - любое целое число"
+ "\n - 3. Сместиться влево = \'L*\', где \'*\' - любое целое число"
+ "\n - 4. Сместиться вправо = \'R*\', где \'*\' - любое целое число"
+ "\nЧтобы закончить ввод, нажмите Enter...\n: ")

while input_value != "":
    input_value = input("\nУкажите, на сколько шагов сместиться роботу согласно правилам ниже:"
+ "\n - 1. Сместиться вверх = \'U*\', где \'*\' - любое целое число"
+ "\n - 2. Сместиться вниз = \'D*\', где \'*\' - любое целое число"
+ "\n - 3. Сместиться влево = \'L*\', где \'*\' - любое целое число"
+ "\n - 4. Сместиться вправо = \'R*\', где \'*\' - любое целое число"
+ "\nЧтобы закончить ввод, нажмите Enter...\n: ")
    spisok.append(input_value)
    if input_value == "":
        print("Ввод закончен")
        continue
    
print(spisok)
spisok1 = spisok[0:-1]
print(spisok1["U"])



print("Количество \"нд\"=", spisok.startwith ("U"))

print("Количество \"нд\"=", spisok.count ("U"))
print("Количество \"ам\"=", spisok.count("D"))
print("Количество \"о\"=", spisok.count("L"))
print("Количество \"о\"=", spisok.count("R"))
"""
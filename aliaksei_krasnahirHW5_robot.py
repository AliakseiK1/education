#Homework related to calculation of robot movement

"""
import sys

print("Enter the array:\n")   
userInput = sys.stdin.readlines()
print(userInput)

"""

"""
a = input().split()

print(a)

for a 

"""
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
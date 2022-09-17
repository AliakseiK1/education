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

up_steps_to_enter = int(input("\nУкажите, на сколько шагов вверх должен подняться робот (целое положительное число): "))
down_steps_to_enter = int(input("\nУкажите, на сколько шагов вниз должен опуститься робот (целое положительное число): "))
left_steps_to_enter = int(input("\nУкажите, на сколько шагов влево должен сместиться робот (целое положительное число): "))
right_steps_to_enter = int(input("\nУкажите, на сколько шагов вправо должен подняться робот (целое положительное число): "))

a = abs(up_steps_to_enter - down_steps_to_enter)
print(a)
b = abs(left_steps_to_enter - right_steps_to_enter)
print(b)
distanse = math.sqrt(a ** 2 + b ** 2)
print(distanse)
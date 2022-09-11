#Если нет ни одого нуля - вывести: "Нет нулевых значений!!!"(Без if - использовать лень)
print("\nДействие 1")
print("\n")

first_value_to_input = int(input("\nВеедите первое число: "))
second_value_to_input = int(input("\nВеедите второе число: "))
third_value_to_input = int(input("\nВеедите третье число: "))

first_output = ((first_value_to_input * second_value_to_input * third_value_to_input == 0) or "Нет нулевых значений!!!")
print(first_output)


#Вывести первое ненулевое значение.
#Если введены все нули - вывести "Введены все нули!" (цикл не использовать) без if - использовать лень
print("\nДействие 2")
print("\n")

#second_output = ((abs(first_value_to_input) + abs(second_value_to_input) + abs(third_value_to_input) > 0) or "Введены все нули!") or first_value_to_input or second_value_to_input or third_value_to_input
second_output = first_value_to_input or second_value_to_input or third_value_to_input or "Введены все нули!"

print(second_output)

#Если первое значение  больше чем сумма второго и третьего вывести a - b - c
print("\nДействие 3")
print("\n")

third_output = (first_value_to_input > (second_value_to_input + third_value_to_input)) or (first_value_to_input - second_value_to_input - third_value_to_input) 

print(third_output)

#Если первое значение меньше чем сумма второго и третьего вывести b + c - a
print("\nДействие 4")
print("\n")

forth_output = (first_value_to_input > (second_value_to_input + third_value_to_input)) or (second_value_to_input + third_value_to_input - first_value_to_input) 

print(forth_output)

#1. Если первое значение больше 50 и при этом одно из оставшихся значение больше первого вывести "Вася"
print("\nДействие 5")
print("\n")

fifth_output = (first_value_to_input < 50 and ((second_value_to_input - first_value_to_input > 0) or (third_value_to_input - first_value_to_input > 0))) or "Bacя"

print(fifth_output)

#1. Если первое значение больше 5 или оба из оставшихся значений равны 7 вывести "Петя"
print("\nДействие 6")
print("\n")

sixth_output = first_value_to_input < 5 or ((second_value_to_input < 7 and second_value_to_input > 7) and (second_value_to_input == third_value_to_input)) or "Петя"

print(sixth_output)
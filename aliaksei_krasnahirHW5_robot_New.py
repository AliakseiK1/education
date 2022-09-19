import math

x = 0 #start point for robot on axis X
y = 0 #start point for robot on axis Y

input_value = input("\nУкажите, на сколько шагов сместиться роботу согласно правилам ниже:" 
+ "\n - 1. Сместиться вверх = \'u *\', где \'*\' - любое целое число"
+ "\n - 2. Сместиться вниз = \'d *\', где \'*\' - любое целое число"
+ "\n - 3. Сместиться влево = \'l *\', где \'*\' - любое целое число"
+ "\n - 4. Сместиться вправо = \'r *\', где \'*\' - любое целое число"
+ "\nЧтобы закончить ввод, введите \'e\', нажмите Enter...\n: ").split() #definition of input: first function
if input_value[0] in ("u","d"):
    y = y - int(input_value[1])
else:
    if input_value[0] in ("r","l"):
     x = x - int(input_value[1])

while True:
    input_value = input("\nУкажите, на сколько шагов сместиться роботу согласно правилам ниже:"
+ "\n - 1. Сместиться вверх = \'u *\', где \'*\' - любое целое число"
+ "\n - 2. Сместиться вниз = \'d *\', где \'*\' - любое целое число"
+ "\n - 3. Сместиться влево = \'l *\', где \'*\' - любое целое число"
+ "\n - 4. Сместиться вправо = \'r *\', где \'*\' - любое целое число"
+ "\nЧтобы закончить ввод, введите \'e\', нажмите Enter...\n: ").split() #definition of input in function
    if input_value[0] in ("u","d"):
       y = y - int(input_value[1])
    elif input_value[0] in ("r","l"):
           x = x - int(input_value[1])
    else:
        if input_value[0] in ("e"):
         break
side_a = x

side_b = y

hypotenuse_с = int(math.sqrt(side_a ** 2 + side_b ** 2))
#hypotenuse_с = str(hypotenuse_с)
print("\nРобот отошел на расстояние, равное {0} шаг(ов)" .format(hypotenuse_с))

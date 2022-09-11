print("\nДобро пожаловать в BMI калькулятор")

hight = float(input("\nВведите свой рост, см: "))
weight = float(input("\nВведите свой вес, кг: "))
sex = str(input("\nВаш пол (m или w): "))

#формула: I = W(кг)/H(м)*0.01(перевод в метры)**2

bmi_index = int(weight/(hight * 0.01)**2)

#Стандартная шкала: 16 - 40

start = int(16)
finish = int(40)

print("\n")

print("Ваш индекс на шкале BMI:")
print("|", "-" * (bmi_index - start+2), "|", "-" * (finish-bmi_index+1), "|")
print(start, ">" * (bmi_index - start), bmi_index, ">" * (finish-bmi_index), finish)


input("\nЧтобы посмотреть рекомендации, нажмите Enter..")

#if bmi_index < 16:
#    print('\nВыраженный дефицит массы тела')
#elif 16 <= bmi_index < 18.5:
#    print('\nНедостаточная масса тела (дефицит)')
#elif 18.5 <= bmi_index < 25:
#    print('\nНорма')
#elif 25 <= bmi_index < 30:
#    print('\nИзбыточная масса тела (состояние, предшествующее ожирению))')
#elif 30 <= bmi_index < 35:
#    print('\nОжирение 1-й степени)')
#elif 35 <= bmi_index < 40:
#    print('\nОжирение 2-й степени)')
#else:
#    print('\nОжирение 3-й степени')

if sex == "m":
    if bmi_index < 16:
            print('\nСрочно наберите массу!')
    elif 16 <= bmi_index < 25:
            print('\nЗапишитесь в тренажерный зал!')
    elif 25 <= bmi_index < 40:
            print('\nПробуйте сбалансировать питание!')
else:
    if bmi_index < 16:
            print('\nПопробуйте сменить диету на более колорийную')
    elif 16 <= bmi_index < 25:
            print('\nЗаймитесь фитнесом!')
    elif 25 <= bmi_index < 40:
            print('\nНачните с пробежек по утрам!')




input ("\nЧтобы выйти, нажмите Enter..")
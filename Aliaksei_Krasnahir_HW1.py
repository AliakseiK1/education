init_text = "Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!"
print("\nИсходная строка:\n")
print(init_text)


input("\nЗадание 1 \nЧтобы посчитать количество символов, нажмите Enter..")
print("Количество =",len(init_text))
input("\nЧтобы продолжить, нажмите Enter..")

input("\nЗадание 2 \nЧтобы инвертировать строку, нажмите Enter")
print(init_text[::-1])
input("\nЧтобы продолжить, нажмите Enter..")

input("\nЗадание 3 \nЧтобы начать каждое слово с заглавной буквы, нажмите Enter..")
print(init_text.title())
input("\nЧтобы продолжить, нажмите Enter..")

input("\nЗадание 4 \nЧтобы сделать все буквы прописными, нажмите Enter..")
print(init_text.upper())
input("\nЧтобы продолжить, нажмите Enter..")

input("\nЗадание 5 \nЧтобы найти число вхождений \"нд\", \"ам\", \"о\" в строку, нажмите Enter..")
print("Количество \"нд\"=", init_text.count("нд"))
print("Количество \"ам\"=", init_text.count("ам"))
print("Количество \"о\"=", init_text.count("о"))
input("\nЧтобы продолжить, нажмите Enter..")

input("\nЗадание 6 \nЧтобы перейти к собственным упражнениям, нажмите Enter..")
input("\nЗадание 6.1 \nЧтобы размножить текст, нажмите Enter..")
print(init_text *3)
input("\nЗадание 6.2 \nЧтобы немного поменять текст, нажмите Enter..")
print(init_text.replace("человека", "гуманойда"))
input("\nЗадание 6.3 \nЧтобы 3 раза прозвучал звуковой сигнал (у меня работает только в терминале Мака :( ), нажмите Enter..")
print("\a","\a","\a")
input("\nЧтобы продолжить, нажмите Enter..")

input("\nЗадание 7 \nЧтобы инвертировать слова в фразе, нажмите Enter..")


split_text_step1 = init_text[0].split(' ')  #добавляет пробел в начале строки
split_text_step1 = init_text.split(sep = ' ') #делает индекс из строки. критерий создания - пробел
split_text_step1 = split_text_step1[::-1] #инвертирует индекс
split_text_step2 = ' '.join(split_text_step1) # Удаление лишлих символов
print(split_text_step2)
print("\nИсходная строка:\n")
print(init_text)

input("\n\nНажмите Enter, чтобы выйти..")

# new comment to check commiting of changes into Feature branch to see changes
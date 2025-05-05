# 1 завдання
#name = input("Введи своє ім'я:")
#age = input("Введи свій вік:")
#print(f"Привіт {name}, тобі {age}!")
# 2 завдання
#age = int(input("Введи свій вік:"))
#if age >= 18:
 #   print("Вхід дозволено!")
#else:
 #   print("Вхід заборонено!")
 # 3 завдання

 #import random

#secret_number = random.randint(1, 10)

#attempts = 3

#print("Я загадав число від 1 до 10. Спробуй вгадати його! У тебе три спроби!")

#for i in range(attempts):
 #   guess = int(input(f"Спроба {i + 1}: Введи число:"))
  #  if guess == secret_number:
   #     print("Вітаю! Ти вгадав число!")
    #    break

    #elif guess > secret_number:
     #   print("Менше")
    #else:
     #   print('Більше')

#else:
 #   print(f"Спроби закінчились. Загадане число було: {secret_number}")

 # 4 завдання

#start = int(input("Введи початкове число (з):"))
#end = int(input("Введи кінцеве число (по):"))

#for number in range(start, end+1):
 #   print(number)

#5 завдання

#n = int(input("Введи число n:"))

#for number in range(n, 0, -1):
 #   if number % 2 == 0:
  #      print(number, end= ' ')

  #  6 завдання
#n = int(input("Введи число n: "))
#factorial = 1

#for i in range(1, n + 1):
 #   factorial *= i
  #  print(f"Факторіал числа {n} дорівнює {factorial}.")

  # 7 завдання

#score = int(input("Введи свою кількість балів:"))

#if score >= 90:
 #   print("Відмінно! (5)")
#elif score >= 75:
 #    print("Добре! (4)")
#elif score >= 60:
 #   print("Задовільно (3)")
#elif score >= 0:
 #   print("Незадовільно! (2)")
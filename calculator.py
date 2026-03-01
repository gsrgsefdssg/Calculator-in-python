while True:
 a = int(input("Введи число: "))
 b = input("Введи знак: ")
 c = int(input("Введи второе число: "))
 if b == '+':
     vivod = a + c
     print("Ответ: ", vivod)
 elif b == '-':
     vivod = a - c
     print("Ответ: ", vivod)
 elif b == '/':
     vivod = a / c
     print("Ответ: ", vivod)
 elif b == '*':
     vivod = a * c
     print("Ответ: ", vivod)
 else:
     print("Такого нету!")
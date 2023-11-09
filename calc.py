import math

try:
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите Второе число: "))

    print("[+] Сложение")
    print("[-] Вычитание")
    print("[*] Умножение")
    print("[/] Деление")
    print("[**] Возведение в степень")
    print("[sqr] Извлечение квадратного корня")
    print("[fac] Вычисление факториала")
    print("[sin] Синус угла")
    print("[cos] Косинус угла")
    print("[tan] Тангенс угла")

    choice = input("Выберите действие: ")

    if choice == "+":
        print("Результат - ", number1 + number2)
    elif choice == "-":
        print("Результат - ", number1 - number2)
    elif choice == "*":
        print("Результат - ", number1 * number2)
    elif choice == "/":
        print("Результат - ", number1 / number2)
    elif choice == "**":
        print("Результат - ", number1 ** number2)
    elif choice == "sqr":
        print("Результат - ", number1 ** 0.5)
    elif choice == "fac":
        print("Результат - ", math.factorial(int(number1)))
    elif choice == "sin":
        print("Результат - ", math.sin(number1))
    elif choice == "cos":
        print("Результат - ", math.cos(number1))
    elif choice == "tan":
        print("Результат - ", math.tan(number1))
    else:
        print("Нет такого действия.")

except ValueError:
    print("Вводить можно только числа..")
except ZeroDivisionError:
    print("На ноль делить нельзя..")
except KeyboardInterrupt:
    print("\nВыход..")
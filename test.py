print("=== Улучшенный калькулятор ===")
try:
    a = float(input("Первое число: "))
    b = float(input("Второе число: "))
    print(f"Сумма: {a + b}")
    print(f"Разность: {a - b}")
    print(f"Произведение: {a * b}")
    if b != 0:
        print(f"Деление: {a / b}")
    else:
        print("Деление на 0 невозможно!")
except ValueError:
    print("Ошибка: Только числа (5, 3.14)!")
print("=== Готово! ===")

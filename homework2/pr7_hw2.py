# Ввод десятичного числа с клавиатуры
decimal_number = int(input("Введите десятичное число: "))

# Перевод в двоичную систему
binary_number = bin(decimal_number)

# Перевод в восьмеричную систему
octal_number = oct(decimal_number)

# Вывод результатов
print(f"Двоичное представление: {binary_number[2:]}")
print(f"Восьмеричное представление: {octal_number[2:]}")

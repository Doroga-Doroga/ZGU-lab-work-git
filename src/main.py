print("Hello, World!")

def add_numbers(x, y):
  """
  Эта функция складывает два числа и возвращает результат.

  Args:
    x: Первое число.
    y: Второе число.

  Returns:
    Сумма x и y.
  """
  return x + y

# Пример использования:
num1 = 5
num2 = 10
result = add_numbers(num1, num2)
print(f"Сумма {num1} и {num2} равна {result}") # Вывод: Сумма 5 и 10 равна 15

num3 = -3
num4 = 7
result = add_numbers(num3, num4)
print(f"Сумма {num3} и {num4} равна {result}") # Вывод: Сумма -3 и 7 равна 4

num5 = 2.5
num6 = 1.2
result = add_numbers(num5, num6)
print(f"Сумма {num5} и {num6} равна {result}") # Вывод: Сумма 2.5 и 1.2 равна 3.7


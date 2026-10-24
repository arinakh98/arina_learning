# Читаем первую строку и разбиваем её по пробелам
vector1_str = input().split()
# Читаем вторую строку
vector2_str = input().split()

# Превращаем строки в числа с плавающей точкой (float)
x1, y1, z1 = map(float, vector1_str)
x2, y2, z2 = map(float, vector2_str)

# Считаем скалярное произведение
result = (x1 * x2) + (y1 * y2) + (z1 * z2)

# Выводим результат
print(result)

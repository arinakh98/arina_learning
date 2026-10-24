vector1 = input().split()
vector2 = input().split()

x1, y1, z1 = map(float, vector1)
x2, y2, z2 = map(float, vector2)

result = (x1 * x2) + (y1 * y2) + (z1 * z2)
print(result)

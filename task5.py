# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math

xy = ["Xa","Ya", "Xb", "Yb"]
coordinates = [int(input(f"Введите значение {xy[i]}: ")) for i in range(4)]

def distance(coord):
    result = ((coord[2] - coord[0]) ** 2) + ((coord[3] - coord[1]) ** 2)
    return round(math.sqrt(result), 2)

print(f"Расстояние в 2D пространстве -> {distance(coordinates)}")

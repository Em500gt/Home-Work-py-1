# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

xy = ["x","y"]
coordinates = [int(input(f"Введите значение {xy[i]}: ")) for i in range(2)]
if coordinates[0] == 0 or coordinates[1] == 0:
    print("Введен ноль......")
    exit()

def quarter(coordinat):
    if coordinat[0] > 0 and coordinat[1] > 0:
        print("Первая четверть")
    if coordinat[0] < 0 and coordinat[1] > 0:
        print("Вторая четверть")
    if coordinat[0] < 0 and coordinat[1] < 0:
        print("Третья четверть")
    if coordinat[0] > 0 and coordinat[1] < 0:
        print("Четвертая четверть")

quarter(coordinates)
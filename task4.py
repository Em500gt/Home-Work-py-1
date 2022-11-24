# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input("Введите четверть: "))
if quarter > 4 or quarter < 1: 
    print("Ввели неверное число...")
    exit()

def coordinates(quarter):
    if quarter == 1:
        print("X > 0\nY > 0")
    
    if quarter == 2:
        print("X < 0\nY > 0")
    
    if quarter == 3:
        print("X < 0\nY < 0")
    
    if quarter == 4:
        print("X > 0\nY < 0")

coordinates(quarter)
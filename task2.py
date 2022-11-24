# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


s = ([0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1])

for i in s:

    def inputNum(x):    
        xyz = ["X", "Y", "Z"]
        a = []
        count = 0
        for i in x:
            print(f"Введите значение {xyz[count]} : {i}")
            a.append(i)
            count += 1
        return a

    def Predicate(x):
        left = not (x[0] or x[1] or x[2])
        right = not x[0] and not x[1] and not x[2]
        result = left == right
        return result

    statement = inputNum(i)

    if Predicate(statement) == True:
        print(f"Утверждение истинно \n")
    else:
        print(f"Утверждение ложно \n")

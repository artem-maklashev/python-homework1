# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def GetCoordinate(message):
    print(message)
    data = {"X": 0, "Y": 0}
    for item in data:
        isCorrect = False
        while isCorrect == False:
            try:
                data[item] = int(input(f'Введите {item} '))
                isCorrect = True
            except ValueError:
                print("Введено не целое число. Повторите ввод ")
    return data


def GetLength(a, b):
    length = ((a['X']-b['X'])**2+(a['Y']-b['Y'])**2)**0.5
    return round(length, 2) 


a = GetCoordinate("Введите координаты точки А ")
b = GetCoordinate("Введите координаты точки B ")
print(f'Расстояние между точками А({a["X"]}, {a["Y"]}) и B({b["X"]}, {b["Y"]}) равно {GetLength(a,b)}')
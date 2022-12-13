# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def GetData(message):
    print(message)
    data = {"X":0, "Y":0,"Z":0}
    for item in data:
        data[item] = input(f'Введите {item} ')
    return data

def PredicatCheck(data):
    left = not (data['X'] or data['Y'] or data['Z']) 
    right = not data['X'] and not data['Y'] and not data['Z']
    result = left == right
    return result

data = GetData("Введите данные")
print(f'\n¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z -> {PredicatCheck(data)}')
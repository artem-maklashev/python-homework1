# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def GetData():
    print('(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
    data = {}
    for x in [True, False]:
        for y in [True, False]:
            for z in [True, False]:
                result =PredicatCheck(x, y,z)
                print(f'NOT ({x} OR {y} OR {z}) = NOT {x} AND NOT {y} AND NOT {z}  -> {result}')
 

def PredicatCheck(x, y, z):
    left = not (x or y or z) 
    right = not x and not y and not z
    result = left == right
    return result

GetData()

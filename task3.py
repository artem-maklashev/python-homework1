# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def GetNumber(message):
    isCorrect = False
    while isCorrect == False:
        try:
            number = int(input(message))
            if number != 0:
                isCorrect = True
            else:
                print('Число не должно равняться 0')
        except ValueError:
            print("Введено не число. Повторите ввод ")            
    return number

def GetQuoter(x,y):
    return {
        x>0 and y>0 : '1 четверти',
        x<0 and y>0: '2 четверти',
        x<0 and y<0: '3 четверти',
        x>0 and y<0: '4 четверти'
    }[True]

x = GetNumber("Введите X ")
y = GetNumber("Введите Y ")

print(f'Координаты ({x}, {y}) соответствуют {GetQuoter(x,y)}')
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
def GetNumber(message):
    isCorrect = False
    while isCorrect == False:
        try:
            number = int(input(message))
            if number not in range(1,5):
                print('Номер четверти находится в диапазоне от 1 до 4')
            else:
                isCorrect = True
        except ValueError:
            print("Введено не число. Повторите ввод ")            
    return number

def GetVolues(quoter):
    return {
        quoter == 1 : "X > 0, Y > 0",
        quoter == 2 : "X < 0, Y > 0",
        quoter == 3 : "X < 0, Y < 0",
        quoter == 4 : "X > 0, Y < 0",
    }[True]

quoter = GetNumber('Введите номер четверти ')
print(f'{quoter} четверти соответствует диапазон значений {GetVolues(quoter)}')
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def GetNumber(message):
    isCorrect = False
    while isCorrect == False:
        try:
            number = int(input(message))
            if number not in range(1,8): #< 1 or number > 7:
                print('Введенное число выходит за диапазон. Введите число от 1 до 7')
            else:
                isCorrect = True
        except ValueError:
            print("Введено не число. Повторите ввод ")
    return number


def IsVacation(dayNumber):
    return {
        dayNumber < 6: 'Рабочий день',
        dayNumber > 5: 'Выходной'
    }[True]


dayNumber = GetNumber('Введите номер дня недели. 1..7: ')
print(f'{dayNumber} -> {IsVacation(dayNumber)}')

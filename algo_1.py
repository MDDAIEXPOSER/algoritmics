"""O(N)"""

def StepsWork(number_to_zero): #инициализация функции, аргумент - число, с которым будем работать
    steps = 0 #а-ля счётчик, на самом деле, количество шагов
    while number_to_zero != 0 and number_to_zero > 0: #цикл, контролирующий приводимое число
         if number_to_zero % 2 == 0: #если нацело делится, то выполняем блок кода
            steps += 1
            number_to_zero //= 2
            print('Step:',steps,';', number_to_zero,'- works')
         else: #иначе 
            steps += 1
            number_to_zero -= 1
            print('Step', steps,';', number_to_zero, '- works')
    

def main():
    StepsWork(int(input()))

if __name__ == "__main__":
    main()

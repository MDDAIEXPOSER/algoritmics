"""O(N)"""

def base_k(n,k):
    new_num = ''#готовим строку
    while n > 0: #цикл который проверяет переводимое число 
        new_num = str(n % k) + new_num #математические операции перевода в произвольную систему счисления 
        n //= k 
    result = sum(map(int,str(new_num))) #складываем все цифры в числе
    if int(n) == int(k): #блок проверки
        print('n is already in base 10', result )
        print('Sum digit:', result)
    else:
        print(new_num)
        print('Sum digit:', result)
    

def main():
    base_k(int(input()),int(input())) #вызов функции и передача аргументов

if __name__ == "__main__":
    main()




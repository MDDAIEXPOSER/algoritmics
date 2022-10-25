"""Difficulty - O(n)"""



def control_block_part(target): #инициализируем функцию с аргументом - строкой из скобочек
    clear_result = [] #готовим пустой список 
    stack_counter = 0 #счётчик 
    for j in target: #запускаем цикл в строке 
        if j == ')': #проверка существования первой скобы в строки (открытой)
            stack_counter -= 1 #двигаем виртуальную каретку далее, чтобы проверить другие символы в строке
        if stack_counter > 0: #проверка счётчика, если в листе уже есть скоба - закидываем ещё
            clear_result.append(j) #закидываем
        if j == '(': #проверка скоб в строке 
            stack_counter += 1 #получаем 1
    return "".join(clear_result) #переводим из листа в строку результат 
    """Программа работает до тех пор, пока в полученной строке есть скобы"""

def main():
    print(control_block_part(str(input())))
if __name__ == "__main__":
    main()

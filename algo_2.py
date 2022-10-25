"""O(N)"""

def ComparerDesk(que_teams): #инициализируем функцию, в качестве аргумента направляем количество матчей в турнирной сетке 
    fights = 0 #наш любимый счётчик
    while que_teams != 1: #цикл контролирует ситуацию, когда в турнирной сетке остаётся одна команда - победитель 
        if que_teams % 2 == 0: #классическое распределение команд
            fights += que_teams // 2 
            que_teams //= 2 
        else: #когда количество команд нечётное и попадает под не классическое условие. 
            fights += (que_teams - 1) // 2 
            que_teams = (fights - 1) // 2 
            result_card = que_teams + 1 
    return result_card

def main():
    print(ComparerDesk(14))

if __name__ == "__main__":
    main()
def robo_mech(robo_grid): #на вход мы подаём списки - строки матрицы 
    if (robo_grid[-1][-1] == 1) or (robo_grid[0][0] == 1): #если строки нулевые или 
        return 0 #возвращаем 0 
    else:
        dependings = [[0]*len(robo_grid[0]) for i in range(len(robo_grid))] #генерируем поле
        dependings[0][0] = 1 #задаём значение ячейке
        for i in range(len(robo_grid)): #запускаем цикл по индексам
            for j in range(len(robo_grid[0])): #ещё один, но теперь по диапозону 
                if robo_grid[i][j] == 0: #проверяем следующие ячейки 
                    dependings[i][j] += dependings[i-1][j] if i-1 >= 0 else 0 
                    dependings[i][j] += dependings[i][j-1] if j-1 >= 0 else 0
        return dependings[-1][-1] #возвращаем полученное значение ячейки 


def main():
    print(robo_mech("",[[0,0,0],[0,1,0], [0,0,0]]))


if __name__ == "__main__":
    main()

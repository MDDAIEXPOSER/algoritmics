"""O(N)"""


def find_jewerly(jewerlies, stones): #инициализация функции с аргументами 
    count_jew = 0 #счётчик
    for jewerly in jewerlies: #инициализация перебора подстроки в строке
        count_jew += stones.count(jewerly) #если нашли, обновляем счётчик 
    print(count_jew)



def main():
    jewels = str(input())
    stone = str(input())
    find_jewerly(jewels,stone)

if __name__ == "__main__":
  main()

def count_square_matris(matrix_string): #функция (аргумент - матричные строки)
    if matrix_string == [[1]]:
        return 1
    rowset = len(matrix_string)
    columns = len(matrix_string[0])
    counter = 0
    for r in range(rowset):
        for c in range(columns):
            if (r == 0 or c == 0):
                if matrix_string[r][c] == 1:
                    counter += 1
            elif matrix_string[r][c] == 1:
                sq = min(matrix_string[r-1][c], min(matrix_string[r][c-1], matrix_string[r-1][c-1])) + 1
                matrix_string[r][c] = sq
                counter += sq
    return counter


def main():
    matrix = [[0,1,1,1], [1,1,1,1], [0,1,1,1]]
    print(count_square_matris(matrix))
if __name__ == "__main__":
    main()

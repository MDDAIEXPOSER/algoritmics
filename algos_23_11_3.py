def robo_mech(robo_grid):
    if (robo_grid[-1][-1] == 1) or (robo_grid[0][0] == 1):
        return 0
    else:
        dependings = [[0]*len(robo_grid[0]) for i in range(len(robo_grid))]
        dependings[0][0] = 1
        for i in range(len(robo_grid)):
            for j in range(len(robo_grid[0])):
                if robo_grid[i][j] == 0:
                    dependings[i][j] += dependings[i-1][j] if i-1 >= 0 else 0
                    dependings[i][j] += dependings[i][j-1] if j-1 >= 0 else 0
        return dependings[-1][-1]


def main():
    print(robo_mech("",[[0,0,0],[0,1,0], [0,0,0]]))


if __name__ == "__main__":
    main()

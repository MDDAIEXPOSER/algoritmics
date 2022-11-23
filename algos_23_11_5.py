class Solution:
    def function(self, cost):
        inn = len(cost)
        que = [0]*inn
        counter = 1
        for i in range(inn):
            if i == 0:
                que[0] = 1
                continue
            elif cost[i-1]-cost[i]==1:
                que[i]=que[i-1]+1+counter
                counter = counter + 1
            else:
                que[i] = que[i-1] + 1
                counter = 1
        return que[-1]

if __name__ == "__main__":
    print(Solution.function("",[3,2,1,4]))

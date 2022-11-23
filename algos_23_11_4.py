class Solution():
    def seller(self, costs):
        if not costs:
            return 0
        else:
            que = 0
            for i, volume in enumerate(costs):
                if i == 0:
                    continue
                if costs[i-1] < volume:
                    que += volume - costs[i-1]

        return que

if __name__ == "__main__":
    print(Solution.seller("",[7,1,5,3,6,4]))

#O(n) - difficulty

class Solution():
    def Bandos_Mode(self, targets):
        if len(targets) == 0:
            return 0
        if len(targets) <= 2:
            return max(targets)


        def Power_Fortune(targets):
            if len(targets) <= 2:
                return max(targets)
            que = [0]*len(targets)
            que[0] = targets[0]
            que[1]=max(targets[0],targets[1])
            for i in range(1,len(targets)):
                que[i]=max(targets[i] + que[i-2], que[i-1])
            return max(que)


        return max(Power_Fortune(targets[:-1]),Power_Fortune(targets[1:]))


print(Solution.Bandos_Mode("",[2,3,2]))

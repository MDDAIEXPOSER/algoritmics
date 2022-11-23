def maxi_generate(n):
    if n == 0:
        return 0
    else:
        array = [0] * (n+1)
        array[1] = 1
        for i in range(n+1):
            if i*2 <= n:
                array[i*2] = array[i]
            if i*2 + 1 <= n:
                array[i*2+1] = array[i] + array[i+1]
        return max(array)

def main():
    print(maxi_generate(int(input())))
if __name__ == "__main__":
  main()

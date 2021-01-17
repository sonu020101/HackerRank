def main():
    n=int(input())
    li=[]
    for i in range(n):
        li.append(list(map(int,input().split())))
    sum_o,sum_t=0,0
    for i in range (n):
        sum_o+=(li[i])[i]
        sum_t+=(li[i])[n-i-1]
    print(abs(sum_o-sum_t))    

if __name__ == "__main__":
    main()
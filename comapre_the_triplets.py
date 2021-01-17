def main():
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    alice,bob=0,0
    for i in range(3):
        if a[i]>b[i]:
            alice+=1
        elif a[i]<b[i]:
            bob+=1
        else:
            continue
    print(alice,bob)
if __name__ == "__main__":
    main()
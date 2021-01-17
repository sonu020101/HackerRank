def main():
    n=int(input())
    li=list(map(int,input().split()))
    pos,neg,zero=0,0,0
    for num in li:
        if num<0:
            neg+=1
        elif num>0:
            pos+=1
        else:
            zero+=1
    print("%f"%round((pos/n),6))
    print("%f"%round((neg/n),6))
    print("%f"%round((zero/n),6))


if __name__ == "__main__":
    main()
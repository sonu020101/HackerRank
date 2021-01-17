def main():
    arr=sorted(list(map(int,input().split())))
    print(sum(arr[:4]),sum(arr[1:]))

if __name__ == "__main__":
    main()
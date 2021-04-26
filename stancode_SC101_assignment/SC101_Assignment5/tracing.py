def main():
    # count = [0]
    # num = b(5, 2, count)
    # print(num)
    # print('base case count = '+str(count[0]))
    # pass'
    print(34//10)


def b(n, k, count):
    if k == 0 or k == n:
        print('base case!')
        count[0] += 1
        return 2
    else:
        return b(n-1, k-1, count)+b(n-1, k, count)


if __name__ == '__main__':
    main()

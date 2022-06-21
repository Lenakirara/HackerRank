if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        i = input().split()
        if i[0] == 'insert':
           lst.insert(int(i[1]), int(i[2]))
        if i[0] == 'print':
            print(lst)
        if i[0] == 'remove':
            lst.remove(int(i[1]))
        if i[0] == 'append':
            lst.append(int(i[1]))
        if i[0] == 'sort':
            lst.sort()
        if i[0] == 'pop':
            lst.pop()
        if i[0] == 'reverse':
            lst.reverse()

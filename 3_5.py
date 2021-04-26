#специальный символ прекращающий работу программы #
s=0
while True:
    a = list(input('Введите числа через пробел: ').split())
    for i in a:
        if i == '#':
            print(s)
            quit()
        else:
            s=s+int(i)
    print(s)






#print((input().split()))


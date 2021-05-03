def fact(n):
    f=1
    for el in range (1, n+1):
        f=f*el
        yield f

for el in fact(int(input('Введите число для получения факториала: '))):
    print(el)



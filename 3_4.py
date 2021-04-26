# решение через **
def my_func(x,y):
    my_func=x**y
    return my_func
print(my_func(float(input('Введите действительное положительное число: ')), int(input('Введите целое отрицательное число: '))))

# решение через цикл
def my_func(x,y):
    my_func = 1
    while y<0:
        my_func=my_func/x
        y+=1
    else:
        return my_func
print(my_func(float(input('Введите действительное положительное число: ')), int(input('Введите целое отрицательное число: '))))

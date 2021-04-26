def my_func(ar1, ar2, ar3):
    my_func=ar1+ar2+ar3-min(ar1, ar2, ar3)
    return my_func
print('Сумма двух наибольших чисел равна: ',my_func(int(input('Введите первое число: ')), int(input('Введите второе число: ')), int(input('Введите третье число: '))))

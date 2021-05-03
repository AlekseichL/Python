from functools import reduce

def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el
my_list=[i for i in range (100, 1001, 2)]
print(my_list)
print(reduce(my_func, range(100, 1001, 2)))

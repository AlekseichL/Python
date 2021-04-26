def dell(ar1, ar2):
    if ar2==0:
        return (print('Выражение не имеет смысла, делитель равен нулю'))
    dell = ar1 / ar2
    return dell
a1=int(input('Введите делимое : '))
a2=int(input('Введите делитель : '))
print(dell(a1, a2))

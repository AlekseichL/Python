b = int(input('Введите число: '));
c = 0;
while b//10>=1:
    if b%10>c:
        c=b%10;
    else:
        c=c;
    b=b//10;
print('Наибольшая цифра в числе:', c);
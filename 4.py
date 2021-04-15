b = int(input('Введите число: '));
c = b%10;
while b//10>=1:
    b = b // 10;
    if b%10>c:
        c=b%10;
    else:
         c=c;
print('Наибольшая цифра в числе:', c);
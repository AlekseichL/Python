a = int(input('Результат спотсмена в первый день составил: '));
b = int(input('Результат должен составить: '));
i=1;
while a<=b:
    i+=1;
    a=a+a/10;
print('на {}-й день спотсмен достигнет результата не менее {} километров'.format(i, b));

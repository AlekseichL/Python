class Cell:
    def __init__(self, nc):
        self.nc=nc

    def __add__(self, other):
        nc_a=self.nc+other.nc
        return f'Количество ячеек после объединения клеток: {nc_a}\n{self.make_order(nc_a)}'

    def __sub__(self, other):
        if self.nc>other.nc:
            nc_s=self.nc-other.nc
            return f'Количество ячеек после вычитания клеток: {nc_s}\n{self.make_order(nc_s)}'

        else:
            return f'Указанное действие невозможно'

    def __mul__(self, other):
        nc_m=self.nc*other.nc
        return f'Количество ячеек после умножения клеток: {nc_m}\n{self.make_order(nc_m)}'

    def __truediv__(self, other):
        nc_t = self.nc // other.nc
        return f'Количество ячеек после деления клеток: {nc_t}\n{self.make_order(nc_t)}'

    def make_order(self, nc=None):
        if nc==None:
            nc=self.nc
        y=0
        nc_q=''
        while y<nc:
            nc_q+='*'
            y+=1
            if y%5==0:
                nc_q+='\n'
        return nc_q

c1=Cell(13)
print(c1.make_order())
print('')
c2=Cell(15)
print(c2.make_order())
print('')
c3=Cell(7)
print(c3.make_order())
print('')
print(c1+c3)
print('')
print(c1-c2)
print('')
print(c1-c3)
print('')
print(c1*c3)
print('')
print(c1/c3)



from sys import argv

script_name, t, B, P = argv

print("Расчет заработной платы сотрудника: ")
print("Выработка в часах: ", t)
print("Ставка в час: ", B)
print("Премия: ", P)
print("Заработная плата сотрудника составит: ", round((float(t)*float(B))+float(P), 2))

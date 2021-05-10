class Road:

    def __init__(self, length, width):
        self._l = length
        self._w = width

    def mroad(self):
        Mk=25 #вес 1 кв. метра дорожного полотна толщиной 1 см
        h=5 #толщина дорожного полотна
        m=self._l*self._w*Mk*h
        print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна составляет: {m} т')

Road=Road(100, 5)
Road.mroad()

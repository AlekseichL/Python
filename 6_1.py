from time import sleep

class TrafficLight:
    # атрибут класса
    __color = ('Красный', 'Желтый', 'Зеленый')

    # метод класса
    def running(self):
        i=0
        while i<3:
            print(f'Переключение сигнала \n {TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(6)
            i += 1

TrL = TrafficLight()
TrL.running()

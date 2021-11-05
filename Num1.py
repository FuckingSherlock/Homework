import time


class TrafficLight:
    def __init__(self, current_color):
        self.__color = current_color
        self.color_list = ['red', 'yellow', 'green']

    def running(self):
        if self.__color in self.color_list:
            num = 0
            i = self.color_list.index(self.__color)
            while num != 3:
                if i == 0:
                    print(self.color_list[i])
                    time.sleep(7)
                    i += 1
                elif i == 1:
                    print(self.color_list[i])
                    time.sleep(2)
                    i += 1
                else:
                    print(self.color_list[i])
                    time.sleep(5)
                    i = 0
                num += 1
        else:
            print('incorrect color')


color1 = TrafficLight('red')

color1.running()

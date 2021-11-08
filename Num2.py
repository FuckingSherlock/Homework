from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, cloth):
        self.cloth = cloth

    @abstractmethod
    def fabric_consumption(self):
        pass


class Suit(Clothes):
    @property
    def fabric_consumption(self):
        return round(2*self.cloth + 0.3)


class Coat(Clothes):
    @property
    def fabric_consumption(self):
        return round(self.cloth/6.5 + 0.5)


coat = Coat(75)
print(coat.fabric_consumption)

suit = Suit(190)
print(suit.fabric_consumption)

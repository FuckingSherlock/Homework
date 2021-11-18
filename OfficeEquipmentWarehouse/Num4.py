class OfficeEquipmentWarehouse:
    # """Класс склада организационной техники"""

    def __init__(self):
        self.equip_types = {}

    def __add__(self, adder):
        name = adder[0].name
        quantity = adder[1]
        class_of_equip = adder[0].__class__.__name__
        temp = {}
        temp.setdefault(name, quantity)
        if not isinstance(quantity, str):
            if class_of_equip not in self.equip_types:
                self.equip_types.setdefault(class_of_equip, temp)
            elif name not in self.equip_types[class_of_equip]:
                self.equip_types[class_of_equip][name] = quantity
            else:
                self.equip_types[class_of_equip][name] += quantity
            print(self.equip_types)
            return self
        else:
            raise TypeError('Не верный тип данных "количество"')


class OfficeEquipment:
    """Базовый класс типов техники"""

    def __init__(self, name):
        self.paper_handling = True
        self.waterproof = False
        self.name = name


class Printer(OfficeEquipment):
    def __init__(self, *args, **qwargs):
        super().__init__(*args, **qwargs)
        self.information_output = True


class Scanner(OfficeEquipment):
    def __init__(self, *args, **qwargs):
        super().__init__(*args, **qwargs)
        self.information_reading = True


class Copier(OfficeEquipment):
    def __init__(self, *args, **qwargs):
        super().__init__(*args, **qwargs)
        self.copying_information = True


warehouse = OfficeEquipmentWarehouse()

eqp1 = Printer('Cannon')
eqp2 = Scanner('Epson')
eqp3 = Copier('Xerox')
eqp4 = Copier('HP')


# print(warehouse.equip_types)

warehouse + (eqp1, 3) + (eqp1, 3)
warehouse + (eqp4, 4)
warehouse + (eqp1, "3")
warehouse + (eqp3, 2)
warehouse + (eqp3, 6)

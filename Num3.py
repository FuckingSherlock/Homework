class Worker:
    def __init__(self, name, surname, position, **income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        if isinstance(self._income, dict):
            w = self._income.get('wage')
            b = self._income.get('bonus')
            if str(w).isdigit() and str(b).isdigit():
                print("The employee's income was", w+b)
            else:
                print("Incorrect 'income' input")


employee = Position('Michael', 'Green', 'engineer', wage=20000, bonus=5500)

employee.get_full_name()

employee.get_total_income()

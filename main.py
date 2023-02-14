

class AbstractRepr:

    def get_properties(self):
        properties = sorted([i for i in self.__dict__ if i[0] != '_'], reverse=True)
        properties_string = ''

        for i in properties:
            properties_string = properties_string + f'{i}: {self.__dict__[i]}, '

        return properties_string[0:-2:1]

    def __repr__(self):
        name = str(self.__class__).split('.')[1][:-2:1]
        properties_string = self.get_properties()
        return f'[{name}] {properties_string}'


class Person(AbstractRepr):
    def __init__(self, name, job, pay):  # init block
        self.name = name
        self.job = job
        self.pay = pay

    def raise_pay(self, percent=0.1):
        self.pay = self.pay * (1 + percent)
        return 'Pay is raised succesfully'

    def __repr__(self):
        return AbstractRepr.__repr__(self)


class Manager(Person):
    def __init__(self, name, pay):
        self.general_manager = False  # there is new general_manager variable
        Person.__init__(self, name=name, pay=pay, job='manager')  # job is always manager

    def raise_pay(self):
        Person.raise_pay(self, percent=0.23)  # start percent is more than person percent

    def is_general_manager(self):
        return self.general_manager

    def set_general(self):
        if self.general_manager is False:
            self.general_manager = True
        elif self.general_manager is True:
            return 'Wrong! {self} is already general manager'

    def undo_general(self):
        if self.general_manager is True:
            self.general_manager = False
        elif self.general_manager is False:
            return 'Wrong! {self} is already not general manager'


#  test block

if __name__ == '__main__':
    oleg = Person('Oleg Molchanov', 'dev', 20000)
    alex = Person('Alex Romanov', 'manager', 15000)
    sue = Person('Sue Jones', 'dev', 70000)
    matvey = Manager('Matvey Siroedov', 50000)

    matvey.set_general()

    print(matvey.undo_general())  # check .undo_general
    print(matvey.undo_general())  # check .undo_general _ Need create exception
    print(matvey.set_general())  # check .set_general
    print(matvey.set_general())  # check .set_general _ Need create exception

    for pers in (oleg, alex, sue, matvey):
        pers.raise_pay()
        print(pers)

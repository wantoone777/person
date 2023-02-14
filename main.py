


class AbstractRepr:
    
    def __repr__(self):
        name = self.__class__
        properties = [i for i in self.__dict__ if i[:2] != "__"]
        properties_string = ""
        for i in properties:
            properties_string = properties_string + f"{i}: {self.__dict__[i]} "
        return f"[{name}] {properties_string}"
        

class Person(AbstractRepr):
    def __init__(self, name, job, pay):
        self.name = name
        self.job = job
        self.pay = pay
    
    def raise_pay(self, percent=0.1):
        self.pay = self.pay * (1 + percent)
        return "Pay is raised succesfully"
    
    def __repr__(self):
        return AbstractRepr.__repr__(self)
    

if __name__ == "__main__":
    oleg = Person("Oleg Molchanov", "dev", 20000)
    alex = Person("Alex Romanov", "manager", 15000)
    
    for pers in (oleg, alex):
        pers.raise_pay()
        print(pers)

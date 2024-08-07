
"""INHERITENCE"""

class Person :

    _name = 'Kunal'
    __surname = 'Kalkotwar'
    yob = 1996

    def _age(self , current_year):
        return current_year - self.yob
    def __age(self,current_year):
        return current_year - self.yob

obj = Person()
class employee(Person) :        # THIS IS CALLED AS INHERITENCE
    pass

print(obj._age(2022))
print(obj._Person__age(2022))
print(employee.yob)
print(employee._name)
print(employee._Person__surname)


# Public            - self.name (It is a public variable which anyone can access)

# Private           - self.__name (It is a Private variable, for which
#                     following systax is used - "print(kunal._person__name)")
#                     Here Person is the class name followed by the variable name

# Protected         - self._name (It is the protected variable which can be accessed by
#                     following syntax - "print(kunal._name)")
#                     Here direct variable name is given.

class person1 :

    def __init__(self,name,surname,yob):
        self._name = name
        self.__surname = surname
        self.yob = yob

kunal = person1("Kunal", "Surname", 1996)

print(kunal._name)
print(kunal._person1__surname)
print(kunal.yob)
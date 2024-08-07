class Person :


    def __init__(self,name, surname, emailid, year_of_birth):
        self.name1 = name
        self.surname1 = surname
        self.emailid1 = emailid
        self.year_of_birth1 = year_of_birth

    def age(self_2,current_year) :
        return (current_year - self_2.year_of_birth1)

kunal_var = Person('Kunal', 'Kalkotwar','Kunalkalkotwar21@gmailcom',1996)
print(kunal_var.age(2022))


#print(kunal_var.name1)
#print(kunal_var.surname1)
#print(kunal_var.emailid1)
#print(kunal_var.year_of_birth1)

"""
Here kunal_var is class variable and is technaically called as "OBJECT"____and
"PERSON is the Class"

Here "SELF" is the pointer which is changeable(According to Developer)

"Here in "self.name1 = name"  name1 and name both are different from each other. here 
self.name1 is the class variable, where as name is the variable where data is assigned."

"""


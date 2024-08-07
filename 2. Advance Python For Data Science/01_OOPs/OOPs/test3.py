
class person :

    def name(self) :
        name = input("Please enter your name : ")
        print("The Name entered is :", name)
        return name

    def EmailID(self) :
        emailid = input('Please enter your EmailID : ')
        print("The EmailID you entered is :", emailid)
        return emailid

    def contact_number(self) :
        contact_number = input('Please enter your contact number : ')
        print("The contact number you entered is :", contact_number)
        return contact_number

    def age(self) :
        current_year = int(input('Enter current year : '))
        year_of_birth = int(input('Enter year of birth : '))
        age = current_year - year_of_birth
        print("Your current age is",age)
        return age


kunal = person().name()

"""kunal.name()
kunal.EmailID()
kunal.contact_number()
kunal.age()"""





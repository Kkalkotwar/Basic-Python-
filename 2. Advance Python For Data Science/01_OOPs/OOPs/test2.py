import logging
logging.basicConfig(filename='test2.log', level=logging.INFO, format= "%(levelname)s,%(message)s")

class person :

    def name(self) :
        name = input("Please enter your name : ")
        logging.info("Name Entered is : %s",name)
        return name

    def EmailID(self) :
        emailid = input('Please enter your EmailID : ')
        logging.info("The EmailID you entered is : %s", emailid)
        return emailid

    def contact_number(self) :
        contact_number = input('Please enter your contact number : ')
        logging.info("The contact number you entered is : %s", contact_number)
        return contact_number

    def age(self) :
        current_year = int(input('Enter current year : '))
        year_of_birth = int(input('Enter year of birth : '))
        age = current_year - year_of_birth
        logging.info("Your current age is : %s",age)
        return age


kunal = person()

kunal.name()
kunal.EmailID()
kunal.contact_number()
kunal.age()





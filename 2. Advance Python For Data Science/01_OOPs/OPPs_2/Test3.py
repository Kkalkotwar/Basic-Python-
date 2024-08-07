# Calling the seprate class in the new desired file:

# So for example I want to call the Test1 class in this file and use its feature.

import Test1    # Just by importing the file we can access all the features of that class
print(Test1)

obj = Test1.person1("Kunal", "Kalkotwar", 1996)
print(obj.yob)
print(obj._name)
print(obj._person1__surname)


# Packages are noting but the directories/folder
# Package >> Folder >> Modules >> files >> classes/entities
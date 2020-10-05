# LAMBDA

#a LIST of DICTs
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"},
]

def f(person): #if we made a whole new function... instead of making it on a new line below
    return person["name"]
    #return person["house"]


    #Sort the people in the list:
#people.sort() #Python3 doesn't know how to sort the DICT... so tell it!
#people.sort(key=f) #sort; the way to sort ('key') is using 'f'
people.sort(key=lambda person: person["name"]) #the inside () is a complete function

print(people)

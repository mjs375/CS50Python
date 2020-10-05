# O B J E C T  -  O R I E N T E D   P Y T H O N PROGRAMMING


# a CLASS is a template for a new type of object


class Point(): #define 'point', then use them!
    # When you create a point, what happens? Magic method...:
    def __init__(self, x, y): #automatically called anytime you create a 'point'
        #variables 'self', 'x', 'y' (variables could be called anything)
        self.x = x #self represents the point itself: to store its own x/y values, store it inside 'self'
        self.y = y #variable stored inside itself (self)

p = Point(2, 8) #provide an x/y value when creating point 'p'

print(p.x) #dot notation means go inside 'p' and access... 'x'
print(p.y) #...or access 'y'


#############


class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = [] #create an empty LIST to store passengers

    def add_passenger(self, name):  #method, or function, that works on an individual object
        if not self.open_seats(): #equivalent to    if self.open_seats() == 0:
            return False #indicate error: capacity is filled!
        self.passengers.append(name) #access the passenger LIST inside the object[self, append a name to the LIST
        return True

    def open_seats(self): #returns number of open seats on Flight (left)
        return self.capacity - len(self.passengers) #how many open seats? capacity - existing passengers

flight = Flight(3) #create object 'flight'
people = ["Harry", "Ron", "Hermione", "Ginny"]

for person in people:
    success = flight.add_passenger(person) #add_passenger() returns True or False
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats left for {person}.")










#

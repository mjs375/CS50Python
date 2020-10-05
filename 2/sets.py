s = set() #Creates an empty SET[collection of unique values]

s.add(1) #Add an element
s.add(2)
s.add(3)
s.add(4)
s.add(3) #This WON'T be added– a set can only have UNIQUE values
s.remove(2) #Removes variable from set

print(s)


print(f"The set has {len(s)} elements.") #Format string lets you include Python syntax inside the print statement

len #len() gives the LENGTH of a thing (list, set, &c.)

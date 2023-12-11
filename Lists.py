friends = ["Praison", "Alan", "Gijo", "Aswathy", "Gijo"]

print(friends)
print(friends[2])
print(friends[-1]) #from reverse
print(friends[1:])
print(friends[1:3])
friends[3]="Aswathy patasseril"
print(friends)

lucky_number = [5, 69, 46, 7]
lucky_number.sort()
lucky_number.reverse()
print(lucky_number)

lucky_number2 = lucky_number.copy()
print(lucky_number2)

#append and extend
friends.extend(lucky_number) #merges in the end like append
friends.append("creed")
friends.insert(1, "Ganesh")
friends.remove("Ganesh")
friends.pop() #Removes the last element
print(friends)

print("Index is " , friends.index("Gijo"))
print(friends.count("Gijo")) #Checks the total count


compositList= ["Ganesh", 25, True]
print(compositList)
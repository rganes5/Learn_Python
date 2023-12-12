#for letter in "Hello world":
#   print(letter)

friends = ["Jim", "Karem", "Levin"]
for names in friends:
    print(names)

for j in range(len(friends)):
    #print(j)
    print(friends[j])

for index in range(10):
    print(index)

print("\n")

for i in range(3, 19):
    print(i)


for k in range(5):
    if k == 0:
        print("first iteration")
    else:
        print("Not the first iteration")
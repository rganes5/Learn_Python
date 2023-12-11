def cube_of(num):
    print("cube of the number ", num, "is")
    return num * num * num


print(cube_of(2))
print(cube_of(3))

result = cube_of(5)
print(result)


def func_list(list):
    list[2] = "is great!"
    return list


simple_list = ["hello", "world", "sucks!"]
result = func_list(simple_list)
print(result)

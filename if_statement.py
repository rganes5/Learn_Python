is_male = False

if is_male:
    print("You are a Male!")
else:
    print("You are not a male! And this example sucks too")

is_tall = True

if is_male and is_tall:
    print("Chad")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but not tall")
else:
    print("what?")
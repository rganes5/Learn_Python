# File: example.py
def some_function():
    print("This function is defined in the module.")

if __name__ == '__main__':
    print("This code is executed only if the script is run as the main program.")
    some_function()



def sample_func(x,y):
    if y==0:
        print("cannnot divide by zero")
    else:
        return x/y

print(sample_func(2,3))
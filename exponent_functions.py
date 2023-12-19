#print(2**3)

def raise_to_power(base_num, pow_num):
    result =1
    for i in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(3 ,4))


def sample_func():
    for val in range(10):
        print(val)

sample_func()

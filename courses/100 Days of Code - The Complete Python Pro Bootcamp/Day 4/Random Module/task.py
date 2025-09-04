import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_0_to_1 = random.random() * 10
# print(random_0_to_1)
#
# random_float = random.uniform(1, 10)
# print(random_float)

coin = random.randint(0 , 1)
if coin == 0:
    print("Heads")
else:
    print("Tails")
i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers:")

for num in numbers:
    print(num)

def while_loop_test(upper_limit):
    numbers = []
    i = 0
    while i < upper_limit:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    
while_loop_test(10)    

def while_loop_test_with_increment(upper_limit, increment):
    numbers = []
    i = 0
    while i < upper_limit:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    
while_loop_test_with_increment(10, 2)    

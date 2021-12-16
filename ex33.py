from sys import argv

def add_i(x):
    i = 0
    numbers = []
    while i < x:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

num = argv[1]

while True:
    try:
        parsed_num = int(num)
        add_i(parsed_num)
        exit()
    except ValueError:
        print("Youi stupid fuck. That's not an integer. Try again.\n")
        num = input("> ")


to_print = ""

for x in range(1, 300):
    if x % 3:
        to_print = (to_print + "fizz ")
        print(to_print)
    if x % 4:
        to_print = (to_print + "buzz ")
        print(to_print)
    to_print = ""

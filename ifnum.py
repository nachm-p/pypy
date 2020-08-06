num1 = input("Wpisz pierwszy numer: ")
num2 = input("Wpisz drugi numer: ")
num3 = input("Wpisz trzeci numer: ")
print("Twoje numery to " + num1 + num2 + num3)


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print("Twoj największy numer to " + max_num(num1, num2, num3))
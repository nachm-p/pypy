szereg_input = input("Wpisz szereg cyfr do uporządkowania: ")
print("Twoje cyfry to " + szereg_input)

elementy = szereg_input.split()
wynik = "Twoja najwieksza liczba to " + max(elementy)
print(wynik)
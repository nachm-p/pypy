friends = ["Ania", "Kasia", "Józia"]
numbers = [1, 2, 3]
print(friends)
print(friends[-1])

friends.extend(numbers)
print(friends)

friends.append("Krzysiu")
print(friends)

friends.insert(1, "Zosia")
print(friends)

friends.pop()
print(friends)

friends.remove("Kasia")
print(friends)

friends.index("Ania")
print(friends)

friends.sort()
print(friends)

friends2 = friends.copy()
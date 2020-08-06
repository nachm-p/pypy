

open_file = open("file.txt", "r")
# r read
# w write - overwriting a file and creating new ones
# r+ read and write
# a append - adding text at the end of the file


print(open_file.readable())
print(open_file.readlines()[1])

for employee in open_file.readlines():
    print(employee)

open_file.close()

open_file = open("file.txt", "a")

open_file.write("\nToby - Human Resources")
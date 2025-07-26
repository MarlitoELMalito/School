str_manip = input("Enter a sentence: ")

print(len(str_manip))

last_char = str_manip[-1]
print(str_manip.replace(last_char, "@"))

print(str_manip[-3:][::-1])

print(str_manip[:3] + str_manip[-2:])

with open('a.txt', 'w') as file:
    file.write("sdf")

with open('a.txt') as file:
    data = file.read()
    print(data)

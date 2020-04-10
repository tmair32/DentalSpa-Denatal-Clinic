f = open("person.txt", "w")

for i in range (1042, 4500):
    if 1325 <= i < 1366:
        continue
    else:
        data = "%d\n" %i
        f.write(data)
f.close()
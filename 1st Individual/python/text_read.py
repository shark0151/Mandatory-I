phone = {}
list = []
with open("./Files/data.txt") as f:
    while True:
        line = f.readline().strip("\n")
        if not line:
            break
        phone["brand"] = line
        line = f.readline().strip("\n")
        phone["model"] = line
        line = f.readline().strip("\n")
        phone["year"] = line
        line = f.readline().strip("\n")
        phone["os"] = line
        list.append(phone.copy())
f.close()

print(list)

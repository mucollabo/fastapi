def doh():
    yield "Homer: D'oh!"
    yield "Lisa: A deer!"
    yield "Marge: A female deer!"

for line in doh():
    print(line)

# print(doh())
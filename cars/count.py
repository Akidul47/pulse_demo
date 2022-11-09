with open('cars/counter.txt', 'r') as c:
    n = c.read()
# print(type(n))
c = int(n)+1
print(c)

filename = "form%s.txt" %c
with open(filename, 'w') as f:
    f.write(str(c))
# n = n+1
# print((n))
with open('cars/counter.txt', 'w') as f:
    f.write(str(c))
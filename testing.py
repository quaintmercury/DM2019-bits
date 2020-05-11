mask = 0
for i in range(6):
    mask = (mask << 1) | 1


print(bin(mask))

def mmc(x, y):
    minimo = x
    while minimo % x != 0 or minimo % y != 0:
        minimo = minimo + 1
    return minimo


a = int(input("A: "))
b = int(input("B: "))
min = mmc(a, b)
print("MMC", min)


# a = int(input("A: "))
# b = int(input("B: "))

# minimo = a

# while minimo % a != 0 or minimo % b != 0:
#     minimo = minimo + 1

# print("MMC", minimo)

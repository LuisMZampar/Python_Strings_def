def decimal_binario(n):
    binario = 0
    pot = 1

    while n != 0:
        resto = n % 2
        binario = binario + resto * pot
        n = n // 2
        pot = pot * 10

    return(binario)


# n = int(input("Informe um numero decimal: "))

# binario = 0
# pot = 1

# while n != 0:
#     resto = n % 2
#     binario = binario + resto * pot
#     n = n // 2
#     pot = pot * 10

# print(binario)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12,13,14]



impares = [n for n in numeros if n%2 != 0 and n > 10]
print(impares)


impares_filter = filter(lambda n: n%2 != 0,numeros)
print(list(impares_filter))
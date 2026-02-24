notas = [85, 100, 92, 100, 78, 100, 95]

max_note = [i for i, nota in list(enumerate(notas,start=1)) if nota == 100]
print(max_note)

for i, nota in enumerate(notas,start=1):
    if nota == 100:
        print(i)


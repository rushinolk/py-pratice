from functools import reduce

animais = ["gato","elefante","cachorro","passarinho","leão"]

max_len_animal = reduce(lambda x,y: x if len(x) > len(y) else y,animais)

print(max_len_animal)
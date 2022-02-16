import itertools

string = input('String a ser permutada:  ')

resultado = itertools.permutations(string, len(string)) #no local do len pode ser alterado para o valor desejado

for i in resultado:
    print(''.join(i))
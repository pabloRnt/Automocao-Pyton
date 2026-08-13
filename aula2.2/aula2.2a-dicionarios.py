end2sp = {}

eng2sp = {
    'one': 'uno',
    'two': 'dos',
    'three': 'tres'
}

print(eng2sp)
print(eng2sp['two'])

print('dos' in eng2sp)

valores = eng2sp.values()
print('uno' in valores)

for chave, valor in eng2sp.items():
    if valor == "uno":
        print(chave)
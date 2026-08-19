import re

padrao = r"([^@, ]+)@([^@, ]+)"

dicicionario_dominimos = {}
lista_usuarios = []

emails = ["ana.silva@gmail.com",
"bruno.santos@outlook.com",
"carlos.mendes@yahoo.com",
"daniela.oliveira@hotmail.com",
"eduardo.costa@gmail.com",
"fernanda.lima@proton.me",
"gabriel.rocha@outlook.com",
"helena.alves@yahoo.com",
"igor.pereira@gmail.com",
"juliana.martins@hotmail.com",
"lucas.barros@proton.me",
"mariana.souza@gmail.com",
"nicolas.ferreira@outlook.com",
"olivia.ribeiro@yahoo.com",
"paulo.carvalho@hotmail.com",
"rafaela.gomes@gmail.com",
"ricardo.teixeira@proton.me",
"sofia.araujo@outlook.com",
"thiago.monteiro@yahoo.com",
"vitoria.nunes@gmail.com"]

for resultado in re.finditer(padrao, ' '.join(emails)):
    
    lista_usuarios.append(resultado.group(1))
    dominio = resultado.group(2)
    
    if dominio not in dicicionario_dominimos:
        dicicionario_dominimos[dominio] = 1
    else: 
        dicicionario_dominimos[dominio] += 1

usuarios = tuple(lista_usuarios)

print("Quantidade de emails por domínio:")
for dominio, contador in dicicionario_dominimos.items():
    print (f"{dominio}: {contador}")
    
print(f"Lista de usuários: {lista_usuarios}")

lista_usuarios[0], lista_usuarios[-1] = lista_usuarios[-1], lista_usuarios[0]

print(f"Após troca de posições: {lista_usuarios}")
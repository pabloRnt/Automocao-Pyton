endpoints = ["/login", "/produtos", "/pedidos"]
status = [
[200, 200, 401, 200, 500, 200, 300],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500] 
]

def erros_seguidos(codigos_http:list)->bool:

    for i in range(len(codigos_http)-1):

        codigo_atual = codigos_http[i]
        prox_codigo = codigos_http[i+1]

        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True
        return False

def eh_sucesso(codigo_http):
    if codigo_http >= 200 and codigo_http <=299:
        return True

def analisar_endpoints(codigos_http):
    qtd_sucessos = 0

    for codigo in codigos_http:

        if eh_sucesso(codigo):
            qtd_sucessos += 1

    qtd_requisicoes = len(codigos_http)
    qtd_erros = qtd_requisicoes - qtd_sucessos

    percentual_sucesso = (qtd_sucessos/qtd_requisicoes) * 100

    tem_erros_seguidos = erros_seguidos(codigos_http)

    if tem_erros_seguidos:
        classificacao = "CRÍTICO"
    elif percentual_sucesso >= 80:
        classificacao = "ESTÁVEL"
    else:
        classificacao = "INSTÁVEL"  

    return(qtd_sucessos, qtd_erros, percentual_sucesso, classificacao)

maior_qtd_erros = -1
endpoints_maior_erro = ""

for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    codigos_endpoint = status[i]

    sucessos, erros, percentual, classificacao = analisar_endpoints(codigos_endpoint)

    print(f"Endpoint: {nome_endpoint}")
    print(f"Códigos HTTP: {codigos_endpoint}")
    print(f"Sucessos: {sucessos}")
    print(f"Erros: {erros}")
    print(f"% sucesso: {percentual}")
    print(f"Classificacao: {classificacao}")
    print("-" * 50)

    if erros > maior_qtd_erros:
        maior_qtd_erros = erros
        endpoints_maior_erro = nome_endpoint
    elif erros == maior_qtd_erros:
        endpoints_maior_erro += " " + nome_endpoint

print(f"Endopoint com erros: {endpoints_maior_erro} ({maior_qtd_erros})")

'''Essa versão é mais modularizada, ou seja, funções que executam tarefas separadamente. Também possui o tratamento de erros caso
pelo menos 2 endpoints possuam a mesma quantidade de erros
'''
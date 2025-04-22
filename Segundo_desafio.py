
def variaveis():
    vitorias = 10
    derrotas = 2
    return vitorias, derrotas

def saldo(vitorias, derrotas):
    return vitorias - derrotas

def calculadora(saldo):
    if 0 <= saldo <= 10:
        return "Ferro"
    elif 11 <= saldo < 20:
        return "Bronze"
    elif 21 <= saldo < 50:
        return "Prata"
    elif 51 <= saldo < 70:
        return "Ouro"
    elif 81 <= saldo < 90:
        return "Diamante"
    elif 91 <= saldo < 100:
        return "Lendário"
    else:
        return "Imortal"

def resultado():
    vitorias, derrotas = variaveis()
    sld = saldo(vitorias, derrotas)
    nivel = calculadora(sld)
    print("O herói tem saldo de", sld,"vitórias e está no nível",nivel,".")

resultado()

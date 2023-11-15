def CriaDistancia():
    distancia_entre_postos = []
    primeiro_elemento = 0

    while True:
        try:
            segundo_elemento = float(input("Digite um número (ou 'stop' para encerrar): "))
            distancia_entre_postos.append([primeiro_elemento, segundo_elemento])
            primeiro_elemento = segundo_elemento
        except ValueError:
            print("Entrada inválida. Encerrando a criação de distâncias.")
            break

    return distancia_entre_postos

def Abastecimento(Percurso, Autonomia, Distancia_entre_Postos):
    soma_kilometros = 0
    i = 0
    PostoEscolhido = []

    while Percurso >= 0 and i < len(Distancia_entre_Postos):
        distancia_trecho = Distancia_entre_Postos[i][1] - Distancia_entre_Postos[i][0]

        if distancia_trecho > Autonomia:
            print("Não é possível fazer a viagem, pois haverá um trecho sem gasolina.")
            break
        else:
            PostoEscolhido.append(Distancia_entre_Postos[i])
            soma_kilometros = PostoEscolhido[-1][1] - PostoEscolhido[-1][0] + soma_kilometros
            i += 1
            print("\nO Posto escolhido é", PostoEscolhido[-1])
            Distancia_entre_Postos = Distancia_entre_Postos[i:]
            Percurso -= distancia_trecho

    if Percurso <= 0:
        print("\nVocê chegou ao seu destino!")
    

def testeAbastecimento():
    distancia_entre_postos_teste = [(0, 40), (40, 70), (70, 100), (100, 130), (130, 160), (160, 200)]

    Percurso_teste = 200
    Autonomia_teste = 50

    print("\nResultados esperados para o teste:")
    print("\nDistância entre postos:", distancia_entre_postos_teste)
    print("\nO Posto escolhido é (0, 40)")
    print("O Posto escolhido é (70, 100)")
    print("O Posto escolhido é (160, 200)")
    print("Você chegou ao seu destino!\n")
    print("#################################")

    Abastecimento(Percurso_teste, Autonomia_teste, distancia_entre_postos_teste)

# Dados de entrada para teste
testeAbastecimento()
# Insere um valor de percurso para iniciar o loop
# Insere um valor de percurso para iniciar o loop
Percurso = 1

while Percurso >= 0:
    # Solicita ao usuário para inserir o Percurso
    try:
        Percurso = float(input("\nDigite o Percurso: "))
        Percurso_float = float(Percurso)
        print("\nVocê inseriu:", Percurso_float)

        # Verifica se Percurso é negativo, se sim, exibe a mensagem e encerra o programa
        if Percurso_float < 0:
            print("Programa fechando.")
            break

        # Solicita ao usuário para inserir a autonomia do veículo
        Autonomia = float(input("\nDigite a Autonomia do seu veículo: "))

        # Tratamento de exceção
        try:
            Autonomia_float = float(Autonomia)
            print("\nVocê inseriu:", Autonomia_float)
        except ValueError:
            print("\nEntrada inválida. Certifique-se de inserir um número.")

        # Chama a função para criar distâncias
        print("\nInsira a distância entre os postos de gasolina:")
        Distancia_entre_Postos = CriaDistancia()

        # Resultado
        print("\n#################################")
        Abastecimento(Percurso_float, Autonomia_float, Distancia_entre_Postos)

    except ValueError:
        print("\nEntrada inválida. Certifique-se de inserir um número.")



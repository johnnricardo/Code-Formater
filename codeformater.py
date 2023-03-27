import os

# Definindo uma variável para controlar se o programa vai executar novamente ou nao, de acordo com a escolha do usuário
continuar = 'S'

os.system("cls")
print("                    *Programa Para Formatar Códigos*\n")

# Criando um comando de condição de acordo com a variável "continuar", para rodar o código novamente se o usuário escolher
while(continuar == 'S' or continuar == 's'):

    # Definindo um vetor para guardar os inputs do usuário e declarando um indice para controlar algumas condições abaixo
    codigos = []
    indice = 0
    print("                  Quantos códigos voce precisa formatar? ")
    print("")

    # Recebendo o numero de códigos que o usuário deseja formatar
    numeroDeCodigos = int(input("                                   "))
    print("")

    # Comando para pegar input de usuário de acordo com o numero de entradas que ele informou que iria ter
    print("                        Cole seus códigos aqui:\n ")

    for i in range(numeroDeCodigos):
        codigos.append(str(input("                                 ")))

    print("")

    # Mostrando o número de códigos recebidos de acordo com o tamanho do vetor, para o usuário saber quantos códigos foram recebidos
    print("                         ",len(codigos), "códigos recebidos")
    print("\n")

    # Condições para printar os códigos na formatação correta
    print(" Códigos formatados: ")
    print('')
    if (numeroDeCodigos == 1):
        print("('", end="")
        print(   codigos[indice], end="")
        print("')")
    else:
        print(r"('", end="")
        while(indice < numeroDeCodigos):
            if (indice == 0):
                print(   codigos[indice], end="")
                print("',")
            elif (indice == numeroDeCodigos-1):    
                print(" '", end="")
                print(   codigos[indice], end="")
                print("')")
            else:
                print(" '", end="")
                print(   codigos[indice], end="")
                print("',")
            indice += 1
     
    print("")
    print("                        Você formatou", len(codigos),"códigos")
    print("                      Copie os codigos formatados")
    print("")

    # Menu para o usuário escolher o que fazer
    print("")
    print("                              !ATENÇÂO! ")
    print("")
    print("                    [S] para formatar mais códigos ")
    print("                    [N] para sair do programa")
    print("                    [C] para créditos")
    print("")
    print("                              Continuar? ", end="")
    continuar = str(input())
    print("")
    
# Condição para mostrar os créditos ou sair do programa
if(continuar == 'C' or continuar == 'c'):
    os.system("cls")
    print(r"                    Thank You for use my program!")
    print(r"                                Coded")
    print(r"                           By João Ricardo")
    print("")
    print(r"                 e-mail: joaoricardomoura99@gmail.com")
    print("\n\n\n\n\n\n\n\n")
    print(r"                        Press [Enter] to EXIT")
    input()
else:
    exit()

# Programa simples escrito por João Ricardo, Estudante de Sistemas da Informação e em busca de me tornar um desenvolvedor
# e-mail: joaoricardomoura99@gmail.com


# Esse código foi criado para agilizar a formatação de grandes volumes de códigos, e esse formato de saída é usado, 
# por exemplo, para selecionar códigos de uma tabela com SQL
 
#MENU - converte massa em volume
import model
opcao = 1
print()

while opcao != '3':
    print()
    print('Escolha uma opção abaixo: ')
    opcao = input('[1] converte massa em volume - [2] ajuda - [3] Encerrar o Programa ')
    if opcao == '1':
        model.combustiveis()

        
    elif opcao == '2':
        model.ajuda()
        
        
    elif opcao == '3':
        print('saindo do programa')


    else:
        print()
        print('Opção Invalida, leia atentamente e coloque a opção correta! ')
        print()




#converte massa em volume
def combustiveis(): 
    print('escolha um combustivel')
    combustivel= input('[1]jet-a1, [2]avgas, [3]biodiesel, [4]qav-1')

    if combustivel=='1':
        massa= float (input('digite o peso (kg): '))
        litro= massa/0.8
        print ('total de litros {:.2f} litros'.format(litro))
        
    elif combustivel=='2':
        massa= float (input('digite o peso (kg): '))
        litro= massa/0.72
        print ('total de litros {:.2f} litros'.format(litro))

    elif combustivel=='3':
        massa= float (input('digite o peso (kg): '))
        litro= massa/0.88
        print ('total de litros {:.2f} litros'.format(litro)) 

    elif combustivel=='4':
        massa= float (input('digite o peso (kg): '))
        litro= massa/0.771
        print ('total de litros {:.2f} litros'.format(litro))
        
    else:
        print(  ' numeração invalida selecione de 1 a 4 ' )

def ajuda():
    print ('precisa de ajuda?')
    print ('você vai escolher um numero de 1 a 4 que é o tipo de combustivel que você vai quere.')
    print ('depois escolha um valor em kg para ele calcular o litro dos combustivel.')



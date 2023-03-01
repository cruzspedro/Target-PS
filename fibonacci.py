# escopo de funções do código

def fibonacci(num):
    aux1 = 0
    aux2 = 1
    flag = 0
    while flag < num:
        flag = aux1 + aux2
        aux1 = aux2
        aux2 = flag
        if flag == num:
            return True
    return False


# Corpo principal do código

var = int(input('Insira o numero a ser testado: '))

if fibonacci(var):
    print('Está na sequência')
else:
    print('Não está na sequência')

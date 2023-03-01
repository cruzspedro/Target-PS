def valor_estado(estado):
    match estado:
        case 'SP':
            return 67_836.43
        case 'RJ':
            return 36_678.66
        case 'MG':
            return 29_229.88
        case 'ES':
            return 19_849.53
        case default:
            print('Estado não mencionado')
            quit()


# valor bruto por estado

SP = 67_836.43
RJ = 36_678.66
MG = 29_229.88
ES = 19_849.53

# Primeiro, calcula-se o valor total

total = SP + RJ + MG + ES

estado = input('Digite o estado que quiser saber a porcentagem de participação: ')
resultado = valor_estado(estado)*100/total
print(f'A participação do estado {estado} é {resultado:.2f}%')

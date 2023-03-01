# Jeito mais simples, usando slicing

palavra = input('Insira a palavra que quer inverter: ')
palavra_aux = palavra[::-1]
print(palavra_aux)

# Sem utilizar slicing

palavra_aux = ""
for i in palavra:
    palavra_aux = i + palavra_aux

print(palavra_aux)
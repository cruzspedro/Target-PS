import json


def highest(info: list):
    high_val = 0.0
    for i in info:
        if i['valor'] > high_val:
            high_val = i['valor']
    return high_val


def how_many_above_mean(info: list):
    mean = 0
    count = 0
    quant = 0
    for i in info:
        if i['valor'] > 0:
            mean = mean + i['valor']
            count = count + 1
    mean = mean/count
    for i in info:
        if i['valor'] > mean:
            quant = quant + 1
    return quant


def lowest(info: list):
    low_val = 99_999.0
    for i in info:
        if i['valor'] < low_val and i['valor'] != 0:
            low_val = i['valor']
    return low_val


try:
    fh = open('dados.json').read()
except:
    print('Erro ao abrir arquivo')

info = json.loads(fh)

print(lowest(info))
print(highest(info))
print(how_many_above_mean(info))
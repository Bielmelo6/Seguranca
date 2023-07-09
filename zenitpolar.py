
zen = ['z','e','n','i','t']

pol  = ['p','o','l','a','r']

text = 'gabriel'

def zenit_polar(text):
    saida = []
    print(text)
    
    for i in text:
        for j in pol: 
            if j == i:
                saida.append(zen[pol.index(j)])
            elif i not in saida and i not in pol and i not in zen:
                saida.append(i)
        for j in zen:
            if j == i:
                saida.append(pol[zen.index(j)])
            elif  i not in saida and i not in zen and i not in pol:
                saida.append(i)
    return saida

print(zenit_polar(text))
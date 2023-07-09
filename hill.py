import numpy as np

def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def inverso_modular(a, m):
    if mdc(a, m) != 1:
        raise ValueError('Inverso modular não existe.')
    t1, t2 = 0, 1
    r1, r2 = m, a
    while r2 != 0:
        q = r1 // r2
        t1, t2 = t2, t1 - q * t2
        r1, r2 = r2, r1 - q * r2
    if t1 < 0:
        t1 += m
    return t1

def decifra_hill(texto_cifrado, chave):
    n = 2
    det = int(np.linalg.det(chave))
    det_inverso = inverso_modular(det % 26, 26)
    chave_inversa = (det_inverso * np.round(det_inverso * np.linalg.inv(chave)) % 26).astype(int)
    tamanho_texto = len(texto_cifrado)
    texto_plano = ''
    for i in range(0, tamanho_texto, n):
        bloco = [ord(ch) - ord('A') for ch in texto_cifrado[i:i+n]]
        bloco = np.array(bloco)
        bloco = np.dot(chave_inversa, bloco) % 26
        texto_plano += ''.join(chr(ch + ord('A')) for ch in bloco)
    return texto_plano

texto_cifrado = 'IOIO'
#texto_cifrado = 'IVAV'
chave = np.array([[4,-1], [1, 2]])
#matriz = chave**-1
#print(matriz)
texto_plano = decifra_hill(texto_cifrado, chave)

print('Texto cifrado:', texto_cifrado)
print('Chave:', chave)
print('Texto plano:', texto_plano)
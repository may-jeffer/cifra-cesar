MODO_CRIPTOGRAFIA = 1
MODO_DECRIPTOGRAFIA = 0

def cesar(data, key, mode):
    alfabeto = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'
    novos_dados = ''
    for c in data:
        indice = alfabeto.find(c)
        if indice == -1:
            novos_dados += c
        else:
            novo_indice = indice + key if mode == MODO_CRIPTOGRAFIA else indice - key
            novo_indice = novo_indice % len(alfabeto)
            novos_dados += alfabeto[novo_indice:novo_indice+1]
    return novos_dados
    
    

key = 3
msg = 'Casa Branca'
print('  Original:', msg)
ciphered = cesar(msg, key, MODO_CRIPTOGRAFIA)
print('Encriptada:', ciphered)
plain = cesar(ciphered, key, MODO_DECRIPTOGRAFIA)
print('Decriptada:', plain)

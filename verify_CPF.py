# Ex2.: CPF
# MAC 0110- Heloisa Tambara


# função que inverte o número para que seja mais fácil acessar os dígitos do CPF: (ex.: 1234 torna-se 4321)
def inverter(A):
    A = str(A)
    B = int(A) 
    novonum = 0
    for j in range(len(A)):
        digito = B // 10 ** (len(A) - 1 - j)    # separa o dígito, da esquerda para a direita
        B -= digito * 10 **(len(A) - 1 - j)
        novonum += digito * 10 ** j    # coloca o dígito da direita para a esquerda
    A = novonum
    return A
    
    
    
# função que confere a validade dos últimos dígitos do CPF:
def verificaCPF(A):
    d11r = A % 10 
    d10r = A % 100 // 10
    A //= 100    # guarda e separa os digitos finais 
    B = str(A)
    soma1 = 0
    soma2 = 0
    A = inverter(A)
    
    for i in range(len(B)):    # para cada dígito (di) no CPF, separá-lo, multiplicá-lo por (11 - i) e juntá-los numa soma
        digito = A % 10
        A //= 10
        soma1 += digito * (11 - i - 1)    # somatoria do d10
        soma2 += digito * (12 - i - 1)    # somatoria do d11
        
    d10 = soma1 % 11    # calcula o d10
    if d10 < 2:
        d10 = 0
    else:
        d10 = 11 - d10

    d11 = (soma2 + d10r * 2) % 11    # calcula o d11
    if d11 < 2:
        d11 = 0
    else:
        d11 = 11 - d11

    return d11r == d11 and d10r == d10    # confere se os d10 e d11 da entrada batem com os calculados
        
        

# inserir o CPF, verificando a validade
while True:
    CPF = input('Entre com o número do CPF:')
    if len(CPF) == 11: 
        try:
            CPF = int(CPF) 
            if CPF >= 0:
                if verificaCPF(CPF):    
                    print('CPF válido')
                    break # para deixar em loop infinito inclusive quando o CPF é valido, basta comentar esse break




# erros de entrada:
                else:    # calculo dos digitos não bateu
                    print('Valor inválido. O CPF foi digitado incorretamente.')
            else:    # valor negativo
                print('Valor inválido. O CPF deve ser um número positivo.')
        except:    # valor string ou float
            print('Valor inválido. Insira somente um número inteiro sem letras ou caracteres especiais.')
    else:    # numero diferente de digitos
        print('Valor inválido. O CPF deve ter 11 dígitos.')

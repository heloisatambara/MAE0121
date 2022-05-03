# EP 2
import math as m
   

def seno(x, n):
    soma = 0
    fator = x
    den = 1
    for i in range(n):
        soma += fator
        fator = fator * x * -x
        fator /= den + 1
        fator /= den + 2
        den += 2
    return soma 

def cosseno(x, n):
    soma = 1
    den = 2
    fator = -x * x / den
    for i in range(n):
        soma += fator
        fator = fator * x * -x
        fator /= den + 1
        fator /= den + 2
        den += 2
    return soma
    

def main():
    var1 = 'valor invalido' # caso seja a primeira vez que roda o programa, não será aceito apenas <ENTER> nos inputs de x e eps.
    var2 = 'valor invalido' # essas variáveis estão sendo usadas a seguir no programa para guardar os valores de x e eps em cada vez que roda.
    
    while True:
# pede os valores para calcular
        while True: 
            x = input('Entre com x: ')
            n = input('Entre com n: ')
            if x == '':
                x = var1
                print(x)
            if n == '':
                n = var2
        
            try:
                x = float(x)
                n = int(n)
            # transforma x para o intervalo 0 a 2pi
                if x > 2 * m.pi:
                    while x > 2 * m.pi:
                        x -= 2 * m.pi
                elif x < 2 * m.pi:
                    while x < 0:
                        x += 2 * m.pi
            # consistência para n
                if n > 100 or n <= 0:
                    print('Valor de n inválido. Insira 0 < n < 100')
                else:
                    print('Valores calculados para:')
                    print(f'x = {x}')
                    print(f'n = {n}')
                    break
            except:
                print('Valor inválido')
                
# o que deseja que seja feito?
        print("Qual cálculo deseja?")
        print("[1] Seno\n[2] Cosseno\n[3] Tangente\n[4] Cossecante\n[5] Secante\n[6] Cotangente")#\n[7] Arcosseno\n[8] Arcocosseno\n[9] Arcotangente")
        while True:
            calc = input('Digite o número correspondente: ')
            try:
                calc = int(calc)
                if calc == 1: 
# faz o print - seno               
                    print('\nSeno:')
                    b = "Usando a soma de termos "
                    c = "- Valor Calculado: "
                    sen = seno(x, n)
                    print(b, c, '%+5f' %sen)
                    break
                elif calc == 2:
# faz o print - cosseno
                    print('\nCosseno:')
                    b = "Usando a soma de termos "
                    c = "- Valor Calculado: "
                    cos = cosseno(x, n)
                    print(b, c, '%+5f' %cos)
                    break
                elif calc == 3:
# faz o print - tangente
                    print('\nTangente:')
                    b = "Usando a soma de termos "
                    c = "- Valor Calculado: "
                    tan = seno(x, n)/cosseno(x, n)
                    print(b, c, '%+5f' %tan)
                    break
                elif calc == 4:
                    print("\nCossecante:")
                    b = "Usando a soma de termos "
                    c = "- Valor Calculado: "
                    cossec = 1/seno(x, n)
                    print(b, c, '%+5f' %cossec)
                    break
                elif calc == 5:
                    print("\nSecante:")
                    b = "Usando a soma de termos "
                    c = "- Valor Calculado: "
                    sec = 1/cosseno(x,n)
                    print(b, c, '%+5f' %sec)
                    break
                elif calc == 6:
                    print("\nCotangente:")
                    b = "Usando a soma de termos "
                    c = "- Valor Calculado: "
                    cotan = cosseno(x,n)/seno(x, n)
                    print(b, c, '%+5f' %cotan)
                    break
                # elif calc == 7:
                #     print("\nArcosseno:")
                #     b = "Usando a soma de termos "
                #     c = "- Valor Calculado: "
                #     arcsen = arcsen(x, n)
                #     print(b, c, '%+5f' %arcsen)
                #     break
                # elif calc == 8:
                #     print("\nArcocosseno:")
                #     b = "Usando a soma de termos "
                #     c = "- Valor Calculado: "
                #     arccos = arccos(x,n)
                #     print(b, c, '%+5f' %arccos)
                #     break
                # elif calc == 9:
                #     print("\nArcotangente:")
                #     b = "Usando a soma de termos "
                #     c = "- Valor Calculado: "
                #     arctan = 
                #     print(b, c, '%+5f' %arctan)
                #     break
                else: print('Digitte um número de 1 a 6')
            except: print('Digite um número de 1 a 6')

        var1 = x # guarda os valores para uma possível próxima rodada
        var2 = n

# novo calculo
        while True:
            ask = input('Novo cálculo (S/N): ')
            if ask == 'N' or ask == 'n':
                break
            elif ask != 'S' and ask != 'N' and ask != 's' and ask != 'n':
                print("Digite S ou N")
            elif ask == 'S' or ask =='s':
                break
        if ask == 'N' or ask == 'n':
            break
    if ask == 'N' or ask == 'n':
        return
main()

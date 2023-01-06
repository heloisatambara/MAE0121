def main():
    r = int(input('Entre com o valor em Reais: '))
    while r % 10 != 0:
        print('O valor deve ser múltiplo de 10')
        r = int(input('Entre com o valor em Reais:'))

    a = r // 100
    b = (r % 100) // 50
    c = ((r % 100) % 50 ) // 20
    d = (((r % 100) % 50) % 20) // 10

    print(a, 'nota(s) de 100')
    print(b, 'nota(s) de 50')
    print(c, 'nota(s) de 20')
    print(d, 'nota(s) de 10')

    ask = input('Deseja sacar dessa forma? Digite s ou n: ')
    if ask == 'n':
        b = r // 50
        c = (r % 50) // 20
        d = ((r % 50) % 20) // 10
        print(b, 'nota(s) de 50')
        print(c, 'nota(s) de 20')
        print(d, 'nota(s) de 10') 
        ask2 = input('Deseja sacar dessa forma? Digite s ou n: ')
        if ask2 == 'n':
            c = r // 20
            d = (r % 20) // 10
            print(c, 'nota(s) de 20')
            print(d, 'nota(s) de 10')
            ask3 = input('Deseja sacar dessa forma? Digite s ou n: ')
            if ask3 == 'n':
                d = r // 10
                print(d, 'nota(s) de 10')
    return

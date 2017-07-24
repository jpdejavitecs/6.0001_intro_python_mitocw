def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    #n é o numero de peças >> a peça de numero maior é a maior, e a menor a menor
    #spare é a torre vazia
    #from é uma torre
    #to é outra torre
    if n == 1:
        '''se houver apenas 1 peça na torre checada, printará a mexida da peça
para a torre possível'''
        printMove(fr, to)

    else:
        Towers(n-1, fr, spare, to)
        '''como n inicia no numero mais alto, esta função irá recursará o numero
    até o n mais baixo (n > 0) para que printe a mexida da peça menor'''
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

print(Towers(4, 'P1', 'P2', 'P3'))


from random import randint
from time import sleep

computador = randint(0, 5)
print('-=-'*20)
print('Vou pensar em um numero entre 0 e 10. Tente Advinhar...')
print('-=-'*20)
jogador = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
sleep (2)
if jogador == computador:
 print('Parabéns, voce acertou!!!')
else:
    print('GANHEI!! eu pensei no numero {} e nao no numero {} '.format(computador, jogador))
sleep (10)


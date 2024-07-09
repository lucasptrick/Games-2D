from random import randint
c=0
py=randint(0,10) #PY PENSANDO
print('\033[35mVou pensar em um número entre 0 a 10.     Tente adivinhar...')
print('\033[1;34m~•°•~\033[m'*8)
while c!=py:
    player=int(input('\033[35mEm qual número eu pensei?')) #PLAY adivinhando
    if player==py:
        print('\033[32mPARABÉNS! Você conseguiu me vencer.      Dúvido acerta novamente!!! ;)')
    else:
        print('\033[31mGanhei!!! Eu pensei em outro número e não no {}. Tente outra vez!!! ;) KKKKK'.format(player))
print('\033[1;30m~•~'*13)
print('\033[1;33mThanks for using our programming of the 1Ptrck')
print('\033[1;33m~•°•~\033[m'*13)
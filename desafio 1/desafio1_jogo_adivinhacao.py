#Desafio: Jogo de Adivinhação Simples
#O programa deve gerar um número aleatório entre 1 e 10.
#O usuário tem três tentativas para adivinhar o número.
#A cada tentativa, o programa deve informar se o palpite está correto, muito alto ou muito baixo.
#Se o usuário acertar, o jogo termina imediatamente.
#Se o usuário não acertar em três tentativas, o programa revela o número correto.

import random

random_num = random.randint(1,10)
attemps = 3
more_or_less = ''

print('------Seja bem vindo(a) ao Jogo de Adivinhação!------\n')

while attemps > 0:
  answer = int(input('Escolha um número inteiro entre 1 e 10: '))

  attemps -= 1
  if random_num > answer:
     more_or_less = 'maior'
  else:
     more_or_less = 'menor'

  if answer != random_num:
    Tip = f'Dica: o número é {more_or_less}!' + '\n'
    if attemps > 1:
      print(f'Você errou, mas ainda pode tentar {attemps} vezes')
      print(Tip)
    elif attemps == 0:
       print(f'Suas tentativas acabaram. O número misterioso é {random_num}!')
       print('Jogue novamente!')
    else:
       print(f'Você errou, mas ainda pode tentar {attemps} vez')
       print(Tip)

  else:
      print(f'Você acertou, parabéns o número misterioso é {random_num}!')
      break
  
  
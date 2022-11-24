# Meu primeiro projeto Python
# Oi professor, eu estava treinando para pygame, fiz um mini jogo para mostrar para ti.
# A implementação de banco de dados me ajudou a entender melhor sobre como podemos acessar e até mesmo estudei um pouco sobre ciência de dados, seguirei pelo caminho de python e análise de dados.
# Adorei as aulas e a sua didática, obrigada por passar todo conhecimento.
# Atenciosamente, Liu, sua aluna da extensão de Python!!!

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem vindo ao mapa do tesouro.")
print("Sua missão é encontrar o baú secreto.")

choice1 = input(
  'Você está em uma encruzilhada, para onde deseja ir? Digite "esquerda" ou "direita" '
).lower()
if choice1 == "direita":
  print("Oh não, você caiu em um buraco. Fim de jogo!")
elif choice1 == "esquerda":
  choice2 = input(
    'Você chegou a um lago. Há uma ilha no meio do lago. Digite "espere" para esperar por um barco. Digite "nade" para atravessar a nado. '
  )

if choice2 == "espere":
  choice3 = input(
    "Você chega na ilha ileso. Há uma casa com 3 portas. Uma vermelha, uma amarela e uma azul. Qual cor você escolhe? "
  )
else:
  print("Você foi atacado por trutas. Fim de jogo!")

if choice3 == "vermelha":
  print("Você foi queimado pelo fogo. Fim de jogo!")
elif choice3 == "azul":
  print("Você foi comido por feras. Fim de jogo!")
elif choice3 == "amarela":
  print("VOCÊ GANHOU!! PARABÉNS!!")
else:
  print("FIM DE JOGO!")

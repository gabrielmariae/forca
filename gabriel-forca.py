''' O 'import' importa uma nova biblioteca.
Nesse caso, está sendo importada a biblioteca 'random'.
O módulo 'random' implementa geradores de números pseudo-aleatórios para várias distribuições.'''
import random

palavras = [''] #Essa variável apresenta uma lista de palavras a serem sorteadas.
letrasErradas = '' #Nessa variável serão armazenadas as letras erradas que o jogador digitar.
letrasCertas = '' #Já nessa, serão armazenadas as letras corretas, ou seja, as que correspondem à palavra sorteada.
escolha = 'sim'

print('Digite as palavras que você deseja. Dentre elas será sorteada a Palavra Secreta.')
while True:
    palavras.append(input('Digite a palavra que você deseja adicionar à lista: ')) #As palavras digitadas aqui serão adicionadas à lista da variável 'palavras'.
    decidir = input ('Deseja escolher mais palavras? ') #Pergunta se o jogador deseja escolher mais palavras.
    if decidir == 'sim': #Se sim, a variável 'palavras.append' repetirá. Se não, o while True para e o jogo começa.
        continue
    else: #Se não, o while True para e o jogo começa.
        break

#A variável 'FORCAIMG' armazena uma lista de caracteres. É a sequência de forcas que serão impressas a cada vez que o jogador erra.
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''] 


def principal(): #O comando 'def' define uma nova função.
    """
    Função Princial do programa
    """
    print('F O R C A') #O print imprime na tela determinado texto. Será impresso na tela o nome do jogo 'FORCA'. 

    palavraSecreta = sortearPalavra()
    palpite = ''
    desenhaJogo(palavraSecreta,palpite)

    while True: #Dá um loop ifinito
        palpite = receberPalpite() 
        desenhaJogo(palavraSecreta,palpite)
        #Se o jogador errar todos os palpites disponíveis, a função perdeuJogo é ativada.
        if perdeuJogo():
            print('Voce Perdeu!!!') #Se essa condição (if) for verdadeira, imprime na tela o texto 'Você perdeu'.
            break #Se essa condição (if) for verdadeira, o break para o While True.
        #Se o jogador descobrir a palavra secreta, a função ganhouJogo é ativada1
        if ganhouJogo(palavraSecreta):
            print('Voce Ganhou!!!') #Se essa condição (if) for verdadeira, imprime na tela o texto 'Você ganhou'.
            break  #Se essa condição (if) for verdadeira, o break para o While True.         
        
#Quando o jogador terminar de colocar seus palpites, a função 'perdeuJogo é chamada.
def perdeuJogo():
    global FORCAIMG #'global' informa que a variável está fora de uma função.
    if len(letrasErradas) == len(FORCAIMG): #O  'len' contará a quantidade de letras erradas pelo jogador.
        return True #Quando a função perdeuJogo for verdadeira, ele retorna.
    else:
        return False #Se a função for falsa, ele retorna falso.
    
#A função 'ganhouJogo contém a palavra que foi sorteada. Ela recorretrá às letras certas dos palpites do jogador.
def ganhouJogo(palavraSecreta):
    global letrasCertas
    ganhou = True #A variável 'ganhou' recebe verdadeira.
    for letra in palavraSecreta: #A instrução 'for' irá percorrer todos os elementos da 'palavraSecreta' verificando se contém a letra palpitada.
        if letra not in letrasCertas: #Se a letra não pertencer à letrasCertas, 'ganhou' recebverá falso.
            ganhou = False 
    return ganhou  #Será retornado a variável 'ganhou' indicando se é verdadeiro ou falso.
        


def receberPalpite():
    
    palpite = input("Adivinhe uma letra: ") #Pede para que o jogador insira uma letra como palpite.
    palpite = palpite.upper()
    if len(palpite) != 1: #Se o jogador inserir mais de uma letra, será avisado para que digite uma única.
        print('Coloque um unica letra.')
    elif palpite in letrasCertas or palpite in letrasErradas: #Se o jogador repetir uma letra, seja ela certa ou errada, será avisado.
        print('Voce ja disse esta letra.')
    elif not "A" <= palpite <= "Z": #Se o jogador digitar qualquer caractere diferente de uma letra, será avisado.
        print('Por favor, escolha apenas letras')
    else:
        return palpite #Se nenhum desses acontecer, retorna à variável 'palpite' e repete a função.
    
    
def desenhaJogo(palavraSecreta,palpite): #A função 'desenhaJogo' contém a palavra secreta e o palpite.
    #ela receberá a global 'letrasCertas' 'letrasErradas' e 'FORCAIMG' para printar na tela o desenho.
    global letrasCertas
    global letrasErradas
    global FORCAIMG

    print(FORCAIMG[len(letrasErradas)]) #Será impresso na tela a letrsa errada e o desenho da forca correspondente ao erro, consecutivamente.
    
     
    vazio = len(palavraSecreta)*'-' #Define 'vazio' como a palavra sorteada.
    
    if palpite in palavraSecreta: #Se o palpite pertencer a palavra sorteada, a variável 'letrasCertas' armazenará o palpite somando-o às letras corretas.
        letrasCertas += palpite
    else: #Se não, a variável 'letrasErradas' armazenará o palpite somando-o às letras erradas.
        letrasErradas += palpite

#'letra' percorrerá 'letrasCertas', 'range' criará uma lista vazia com a quantidade de letras da palavra sorteada, cada espaço vazio será preenchido com a respectiva letra certa.
    for letra in letrasCertas:
        for x in range(len(palavraSecreta)):
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]
                
    print('Acertos: ',letrasCertas ) #Imprime na tela as letras certas.
    print('Erros: ',letrasErradas) #Imprime na tela as letras erradas.
    print(vazio) #Imprime a palavra sorteada.
     

def sortearPalavra():  #sorteará apenas uma e ela retornará
    global palavras #A função 'sortearPalavra', quando chamada, recorrerá a global 'palavras' que contém as palavrasq ue poderão ser sorteadas, sorteará apenas uma e ela retornará.
    return random.choice(palavras).upper() #'Choice' sorteará uma palvra aleatória na lista.

    
principal()

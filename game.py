from random import randint
from os import system,name
from colorama import Fore
from rich.table import Table
from rich.console import Console


hand = ['Pedra','Papel','Tesoura']
winsPc   = winsPlayer   = 0
trophyPc = trophyPlayer = 0


def clear():
    if name == 'nt':
        system('cls')
    else:system('clear')


def display_combination():
    print('-=-'*8)
    print(
    ''' Pedra  Papel  Tesoura
  0       1       2''')
    print('-=-'*8)
    print()
 

def PlayerPlay():
    while True:
        display_combination()
        try:
            indexPlayer = int(input('Indice: '))
        except ValueError: 
            clear()
            continue
        except IndexError:
            clear()
            continue
        if indexPlayer < 0 or indexPlayer > 2:
            print(f'{Fore.LIGHTRED_EX}Digite um valor entre 0 e 2{Fore.RESET} \n')
            continue
        else:
            break
    return indexPlayer


def PcPlay():
    return randint(0,2)


def WinVerify(indexRobot, indexPlayer):
    global winsPc, winsPlayer, trophyPc, trophyPlayer

    #jogadas do computador 
    if  indexRobot == 0 and indexPlayer == 2 or indexRobot == 1 and indexPlayer == 0 or indexRobot == 2 and indexPlayer == 1:
        print(f'{Fore.RED}O computador ganhou! +1pt{Fore.RESET}')
        winsPc += 1

    #jogadas do jogador
    elif indexPlayer == 0 and indexRobot == 2 or indexPlayer == 1 and indexRobot == 0 or indexPlayer == 2 and indexRobot == 1 :
        print(f'{Fore.GREEN}O player ganhou! +1pt{Fore.RESET}')
        winsPlayer += 1
    else:
        print(f'{Fore.YELLOW}Empate{Fore.RESET}')
    
    if winsPc >= 10:
        trophyPc += 1
        winsPc = 0
    elif winsPlayer >= 10:
        trophyPlayer += 1
        winsPlayer = 0
    

def TablePoint():
    console = Console()
    table = Table()
    table.add_column('Pc Wins')
    table.add_column('Player Wins')
    table.add_column('Pc Trophy')
    table.add_column('Player Trophy')
    table.add_row(str(winsPc), str(winsPlayer), str(trophyPc), str(trophyPlayer))
    console.print(table)


def display_screen(indexRobot, indexPlayer):
    print('-'*30)
    print(f'O computador jogou: {Fore.LIGHTMAGENTA_EX}{hand[indexRobot]}{Fore.RESET}')
    print(f'O jogador    jogou: {Fore.LIGHTCYAN_EX}{hand[indexPlayer]}{Fore.RESET}')
    WinVerify(indexRobot, indexPlayer)
    TablePoint()
    print('-'*30)


while True:
    pc     = PcPlay()
    player = PlayerPlay()
    display_screen(pc,player)
    system('pause')
    clear() 
   
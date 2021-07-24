import classes
from time import sleep
import threading 

escolha_champion_banir = input('escolha Ban:   ')
escolha_champion_pickar = input('escolha Pick:   ')

def aceitar_fila():
        fila_search = classes.Recognition('aceitar!.png')

# Função para pickar campeão escolhido
def pickar():
    search = classes.Recognition('buscarlol.png')
    if  search != None:
        write_input = classes.write(escolha_champion_pickar) 
    champion_search = classes.Recognition('ChampionsPick/'+escolha_champion_pickar+'Pick.png')
    if  champion_search != None:
        pickar_search = classes.Recognition('pickar.png')
    if  pickar_search != None:
        print('sucess Pick')  

# Função para banir campeão escolhido
def banir():
    search = classes.Recognition('buscarlolBan.png')
    if  search != None:
        write_input = classes.write(escolha_champion_banir) 
    champion_search = classes.Recognition('ChampionsBan/'+escolha_champion_banir+'Ban.png')
    if  champion_search != None:
        pickar_search = classes.Recognition('banir.png')
    if  pickar_search != None:
        print('sucess Ban')  

def main():
    while True:
        aceitar_fila()
        sleep(1)
        banir()
        sleep(1)
        pickar()        
        if aceitar_fila():
            continue
        break

main()
import classes
import PySimpleGUI as sg
import funcoes
import os
from time import sleep
import threading

# janelas
janela, banimentos, janela_cancel = funcoes.janela_inicial(), funcoes.janela_banimento(), None
banimentos.hide()


#Ler os arquivos
while True:
    window, event, values = sg.read_all_windows()
    #tempo = values.get('<')    
   

    #Função para aceitar fila
    pass
    # Escolhe o campeão que deseja banir
    escolha_champion_banir = values.get('dropban')
    print(escolha_champion_banir)
    # Escolhe o campeão que deseja pickar
    escolha_champion_pickar = values.get('droppick')
    print(escolha_champion_pickar)
    # Função para pickar campeão escolhido
    def pickar():
        search = classes.Recognition('buscarlol.png')
        if  search != None:
            write_input = classes.write(escolha_champion_pickar) 
        champion_search = classes.Recognition('ChampionsPick/'+escolha_champion_pickar+'Pick.png')
        if  champion_search != None:
            pickar_search = classes.Recognition('pickar.png') 
        else:
            return 
                
    # Função para banir campeão escolhido
    def banir():
        search = classes.Recognition('buscarlolBan.png')
        if  search != None:
            write_input = classes.write(escolha_champion_banir) 
        champion_search = classes.Recognition('ChampionsBan/'+escolha_champion_banir+'Ban.png')
        if  champion_search != None:
            banir_search = classes.Recognition('banir.png') 
        else:
            return 

# executar funções pick/ban
    if  window == banimentos and event == '"':           
        if escolha_champion_banir != '' and escolha_champion_pickar != '':
            popup_two = sg.popup('AGUARDE SEU PICK/BAN')
            print(popup_two)
            banir()
            pickar()
        if escolha_champion_pickar != None and escolha_champion_banir == '':
            sg.popup('AGUARDE SEU PICK')
            pickar()
        if escolha_champion_banir != None and escolha_champion_pickar == '':
            sg.popup('AGUARDE SEU BAN')
            banir() 
        

    # Quando a janela for fechada
    if  window == janela and event == sg.WIN_CLOSED:
        break
    if  window == janela_cancel and event == sg.WIN_CLOSED:
        break
    if  window == banimentos and event == sg.WIN_CLOSED:
        banimentos.hide()
    if  window ==  janela_cancel and event == 'Cancelar':
        break
    # Funcoes da janela 'janela'
    funcoes.saved_account_popup(janela, window, event)

    # Funcoes da janela 'banimentos'
    funcoes.events_banimentos(janela, banimentos, window, event, pickar, banir)
    funcoes.disable(janela, banimentos, window, event, values)
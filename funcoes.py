import PySimpleGUI as sg
import classes


# Lista de campeões
champion_list = ('aatrox', 'ahri', 'akali', 'alistar', 'amumu', 'anivia', 'annie', 'ashe', 'aurelion_sol', 'azir',
'bard', 'blitzcrank', 'brand', 'braum', 'caitlyn', 'camille', 'cassiopeia', 'cho_gath', 'corki', 'darius', 'diana',
'dr_mundo', 'draven', 'ekko', 'elise', 'evelynn', 'ezreal', 'fiddlesticks', 'fiora', 'fizz', 'galio', 'gangplank',
'garen', 'gnar', 'gragas', 'graves', 'hecarim', 'heimerdinger', 'illaoi', 'irelia', 'ivern', 'janna', 'jarvaniv', 
'jax', 'jayce', 'jhin', 'jinx', 'kalista', 'karma', 'karthus', 'kassadin', 'katarina', 'kayle', 'kennen', 'kha_zix',
'kindred', 'kled', 'kogmaw', 'leblanc', 'leesin', 'leona', 'lissandra', 'lucian', 'lulu', 'lux', 'malphite', 'malzahar',
'maokai', 'masteryi', 'missfortune', 'mordekaiser', 'morgana', 'nami', 'nasus', 'nautilus', 'nidalee', 'nocturne',
'nunu', 'olaf', 'orianna', 'pantheon', 'poppy', 'quinn', 'rammus', 'reksai', 'renekton', 'rengar', 'riven', 'rumble',
'ryze', 'sejuani', 'shaco', 'shen', 'shyvana', 'singed', 'sion', 'sivir', 'skarner', 'sona', 'soraka', 'swain', 'Syndra',
'tahm_kench', 'taliyah', 'talon', 'taric', 'teemo', 'thresh', 'tristana', 'trundle', 'tryndamere', 'twisted_fate', 'twitch',
'udyr', 'urgot', 'varus', 'vayne', 'veigar', 'vel_koz', 'vi', 'viktor', 'vladimir', 'volibear', 'warwick', 'wukong',
'xerath', 'xinzhao', 'yasuo', 'yorick', 'zac', 'zed', 'ziggs', 'zilean', 'zyra')


# Funções
''' Funcoes referente a criação de Janelas '''

def fila():
    sg.theme('DarkTeal10')
    layout =  [
        [sg.Button('Auto Fila', size=(10, 1),  pad=(110, 10))],
    ]
    return sg.Window('Lol Fodase', layout=layout, size=(350,440), finalize=True)





def janela_inicial():
    sg.theme('DarkTeal10')
    layout =  [
        [sg.Text('Adicione o seu Login:', pad=(85, 0))],
        [sg.Input('', size=(20,20), pad=(80, 0))],
        [sg.Text('Adicione o sua senha:', pad=(85, 0))],
        [sg.Input('', password_char = "*" ,size=(20,20), pad=(80, 5))],
        [sg.Button('Adicionar Conta',  pad=(103, 10))],
        [sg.Text('', pad=(85, 40))],
        [sg.Text('Selecione a conta:', pad=(95, 0))], 
        [sg.DropDown('Contas', size=(20,20), pad=(80, 0))],
        [sg.Button('Logar', size=(10, 1),  pad=(110, 10))],
        [sg.Checkbox('Auto Ban', pad=(40, 0), key='checkban'), sg.Checkbox('Auto Pick',  pad=(15, 0), key='checkpick')],
        [sg.Checkbox('Aceitar Partida Automaticamente', pad=(40, 0), key='checkpartida')],
        [sg.Button('.', image_filename='Icons/engrenagem.png', pad=(140, 10))],
    ]
    return sg.Window('Lol Fodase', layout=layout, size=(350,440), finalize=True)

def janela_banimento():
    sg.theme('DarkGrey3')
    layout = [
      [sg.Text('Escolha um campeão para banir:', pad=(65, 0))],
        [sg.Combo(champion_list, size=(20,20), pad=(90, 10), key='dropban')],
        [sg.Button('Confirmar', size=(10, 1),  pad=(120, 10), key='confirmaban')],
        [sg.Text('', pad=(85, 50))],
        [sg.Text('Escolha um campeão para pickar:', pad=(65, 0))],
        [sg.Combo(champion_list, size=(20,20), pad=(90, 10), key='droppick')],
        [sg.Button('Confirmar', size=(10, 1),  pad=(120, 10), key='confirmapick')],
        [sg.Text('', pad=(85, 60))],
        [sg.Button('.', enable_events=True, image_filename='Icons/voltar.png', pad=(10, 0), key='.')],
        [sg.Button('"', enable_events=True, image_filename='', pad=(120, 0), size=(10, 1), key='"')],
    ]
    return sg.Window('Janela de Banimentos', layout=layout, finalize=True)

# def janela_popup():
#     sg.theme('GreenMono')
#     layout = [
#     [sg.Input('Tempo', size=(10, 1), pad=(10, 0), key='<')],
#     ]
#     return sg.Window('Janela de Banimentos', layout=layout, finalize=True)


''' Funcoes referentes a eventos dentro das janelas '''



# Eventos dentro da janela banimentos
def events_banimentos(janela, banimentos, window, event, pickar, banir):
    if  window == janela and event == '.':
        banimentos.un_hide()
    if  window == banimentos and event == '.':
        banimentos.hide()
        # Botao que vai rodar as funcoes e chamar o popup
        # Executa a função pickar()
    """if  window == banimentos and event == 'confirmapick':
        pickar()
        # Executa a função banir()
    if  window == banimentos and event == 'confirmaban':        
        banir()"""

def saved_account_popup(janela, window, event):
    if  window == janela and event == 'Adicionar Conta':
        sg.popup('Sua conta foi salva!')

# desabilitar e habilitar eventos da janela banimentos
def disable(janela, banimentos, window, event, values):   
    if  window == janela and event == '.':
        if values ['checkban'] == False and values ['checkpick'] == False:
            banimentos.hide() 
            sg.popup('Marque uma das opções "Auto Ban" ou "Auto Pick" para continuar')
            # Sobre ban
        if values ['checkban'] == False:
            banimentos['dropban'].update(disabled=True)
        if values ['checkban'] == False:
            banimentos['confirmaban'].update(disabled=True)
        if values ['checkban'] == True:
            banimentos['dropban'].update(disabled=False)
        if values ['checkban'] == True:
            banimentos['confirmaban'].update(disabled=False)
            #Sobre pick
        if values ['checkpick'] == True:
            banimentos['droppick'].update(disabled=False)
        if values ['checkpick'] == True:
            banimentos['confirmapick'].update(disabled=False)
        if values ['checkpick'] == False:
            banimentos['droppick'].update(disabled=True)
        if values ['checkpick'] == False:
            banimentos['confirmapick'].update(disabled=True)

       
        
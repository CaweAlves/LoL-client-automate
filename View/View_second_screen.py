import PySimpleGUI as sg

class View_second_screen:
    def __init__(self):
        sg.theme('DarkGrey3')
        layout = [
        [sg.Text('Escolha um campeão para banir:', pad=(65, 0))],
            [sg.Combo('''champion_list''', size=(20,20), pad=(80, 10), key='dropban')],
            [sg.Button('Confirmar', size=(10, 1),  pad=(110, 10), key='confirmaban')],
            [sg.Text('', pad=(85, 50))],
            [sg.Text('Escolha um campeão para pickar:', pad=(65, 0))],
            [sg.Combo('''champion_list''', size=(20,20), pad=(80, 10), key='droppick')],
            [sg.Button('Confirmar', size=(10, 1),  pad=(110, 10), key='confirmapick')],
            [sg.Text('', pad=(85, 60))],
            [sg.Button('.', enable_events=True, image_filename='', pad=(10, 0), key='.')],
        ]
        self.janela_2 = sg.Window('Janela de Banimentos', layout=layout, finalize=True)
        while True:
            self.window, self.event, self.values = self.janela.Read()

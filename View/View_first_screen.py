import PySimpleGUI as sg

class View_first_screen:
    def __init__(self):
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
            [sg.Button('.', image_filename='', pad=(140, 10))],
        ]
        self.janela = sg.Window('Lol Fodase', layout=layout, size=(350,440), finalize=True)
        while True:
            self.window, self.event, self.values = self.janela.Read()


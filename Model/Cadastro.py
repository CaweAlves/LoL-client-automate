import csv

login_conta = input('Insira o Login da conta: ')
senha_conta = input('Insira a Senha da conta: ')

class Cadastro:
    def __init__(self, arquivo) -> None:
        arquivo = 'ContasCSV.csv'
        #grava os dados
        with open(arquivo, 'a', newline='') as csvfile:
            fieldnames = ['Login', 'Senha']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'Login': login_conta, 'Senha': senha_conta})
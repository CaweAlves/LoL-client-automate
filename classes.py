import time, subprocess, sys, csv
import pandas as pd
#from openpyxl import Workbook
import csv
from pynput.keyboard import Key, Controller
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import DropDown, popup
from numpy import source
from pyautogui import *
import pyautogui
from time import sleep
import time
pyautogui.PAUSE = 0.5

keyboard = Controller()


class Recognition:
    def __new__(self, directory) -> None:
        #contador = 0
        #tempo = int(input('Quanto tempo deseja que o programa rode?(segundos)'))
        while True: #contador < tempo True:
            #print(contador)
            #contador = contador + 1     
            self.position = pyautogui.locateCenterOnScreen(directory)
            print(pyautogui.locateCenterOnScreen(directory, confidence=0.7))          
            if self.position != None:
            #    pyautogui.moveRel(423, 161)
                pyautogui.moveTo(self.position)
            #   pyautogui.click(None,None,1)
            #   pyautogui.moveRel(423, 161)
            #   pyautogui.click(None,None,1)
                pyautogui.click(moveTo(self.position))
                return False 
            #   pyautogui.moveRel()
            #   pyautogui.click()
   
"""
class Click(Recognition):
    # Função para mouse clickar
    def clickar(x, y):
        while True:



             if self.position != None:
            click_champion(position.x,  position.y)
            return True
        return False

            """

class Write:
    def __init__(self, choice) -> None:
        self.pyautogui.write(choice)

class Acesso:

    def __init__(self, email, senha) -> None:
        self.email = email
        self.__senha = senha



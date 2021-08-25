import pyautogui as pg
pg.PAUSE = 0.5

class Click:
    def __new__(self, position_click):
        pg.moveTo(position_click)
        pg.click(position_click)
        return True
        
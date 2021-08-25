import pyautogui as pg

class Write:
    def __init__(self, choice) -> None:
        self.writer = pg.write(choice)
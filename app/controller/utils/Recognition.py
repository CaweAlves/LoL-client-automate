import pyautogui as pg
import asyncio


class Recognition:

    def __init__(self):
        pass

    def find_image(image):
        location = pg.locateOnScreen(image, confidence=0.9, grayscale=True)
        if location:
            return location
        else:
            return False
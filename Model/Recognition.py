from Model.Click import Click
import pyautogui as pg
import gc

class Recognition:
    def __new__(self, directory):  
        self.position = pg.locateCenterOnScreen(directory, confidence=0.5)
        print(pg.locateCenterOnScreen(directory))          
        if self.position != None:
            a = print("first condition")
            resolution = pg.size() 
            print(resolution)
            return Click(self.position)
        else:
            b = print("second condition")
            del self.position
            del b
            gc.collect()
            return Recognition(directory)
        

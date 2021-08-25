from Model.Click import Click
import pyautogui as pg
import gc

class Recognition:
    def __new__(self, directory):  
        self.position = pg.locateCenterOnScreen(directory)
        print(pg.locateCenterOnScreen(directory))          
        if self.position != None:
            return Click(self.position)
        else:   
            del self.position
            gc.collect()
            return Recognition(directory)
        

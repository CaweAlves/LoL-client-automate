from Model.Click import Click
import pyautogui as pg
import gc

class Recognition:
    def __new__(self, directory):  
        self.position = pg.locateCenterOnScreen(directory)
        print(pg.locateCenterOnScreen(directory))          
        if self.position != None:
            print("first condition")
            return Click(self.position)
        else:
            print("second condition")
            del self.position
            gc.collect()
            return Recognition(directory)
        

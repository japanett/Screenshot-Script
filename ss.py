import pyautogui

class ss:
    def __init__(self, number, path):
        self.name = "ScreenShot_%d.jpg" %(number)
        self.number = number
        self.path = path

    def takeSS(self):
        ss = pyautogui.screenshot()
        ss.save(self.path + self.name)

    def showPath(self):
        return self.path + self.name

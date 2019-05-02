import os


class settingsFile:

    def __init__(self):
        if os.path.exists("settings.txt") == False:
            settings = open("settings.txt","w+")
            currentLoc = os.path.dirname(os.path.abspath(__file__))
            lines = []
            lines.append(currentLoc)
            lines.append(currentLoc)
            with open('settings.txt', 'w') as f:
                f.writelines("%s\n" % l for l in lines)

        self.settings = open("settings.txt","r")
        self.settingsArray = []
        for line in self.settings:
            self.settingsArray.append(line.replace("\n",""))

        for i in range(0,len(self.settingsArray)):                                          #protects settings file opened on different machines
            if os.path.exists(self.settingsArray[i]) == False:
                self.settingsArray[i] = 'C:/'
                self.updateSettingsFile()

    def getCurrentOpenLoc(self):
        return self.settingsArray[0]

    def setCurrentOpenLoc(self, currentFileLoc):
        self.settingsArray[0] = currentFileLoc
        self.updateSettingsFile()

    def getAnsysLoc(self):
        return self.settingsArray[1]

    def setAnsysLoc(self, currentFileLoc):
        self.settingsArray[1] = currentFileLoc
        self.updateSettingsFile()

    def updateSettingsFile(self):
        settings = open("settings.txt", "w")
        lines = []
        for i in range(0, len(self.settingsArray)):
            lines.append(self.settingsArray[i])
        with open('settings.txt', 'w') as f:
            f.writelines("%s\n" % l for l in lines)
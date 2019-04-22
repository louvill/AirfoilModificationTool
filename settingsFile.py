import os

class settingsFile:

    def __init__(self):
        if os.path.exists("settings.txt") == False:
            settings = open("settings.txt","w+")
            currentLoc = os.path.dirname(os.path.abspath(__file__))
            lines = "defaultOpenLoc " + currentLoc + "\n"
            lines += "AnsysLoc " + currentLoc + "\n"
            settings.writelines(lines)
            settings.close()

        with open("settings.txt") as self.settings:
            self.settingsArray = [line.split() for line in self.settings]

    def getCurrentOpenLoc(self):
        return self.settingsArray[0][1]

    def setCurrentOpenLoc(self, currentFileLoc):
        self.settingsArray[0][1] = currentFileLoc
        self.updateSettingsFile()

    def getAnsysLoc(self):
        return self.settingsArray[1][1]

    def setAnsysLoc(self, currentFileLoc):
        self.settingsArray[1][1] = currentFileLoc
        self.updateSettingsFile()

    def updateSettingsFile(self):
        settings = open("settings.txt", "w")
        lines = ""
        for i in range(0, len(self.settingsArray)):
            for j in range(0, len(self.settingsArray[i])):
                if j == len(self.settingsArray):
                    lines += self.settingsArray[i][j]
                else:
                    lines += self.settingsArray[i][j] + " "
                #lines += self.settingsArray[i][j] + " "
            lines += "\n"
        #print("Settings file was updated to " + lines)
        settings.writelines(lines)
        settings.close()
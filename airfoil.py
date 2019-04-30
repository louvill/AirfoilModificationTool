import csv


class airfoil:

    def __init__(self):
        self.genNum = 1

    def loadFile(self, fileLocation):
        self.fileLocation = fileLocation
        #print(self.fileLocation)
        self.points = list(csv.reader(open(self.fileLocation)))
        #print(self.points)
        for i in range(0,len(self.points)):
            for j in range(0,len(self.points[0])):
                self.points[i][j] = float(self.points[i][j])
        #print(self.points)
    
    def getPlottingPoints(self, canvasWidth, canvasHeight):
        xmin = self.points[0][0]
        xmax = self.points[0][0]
        for i in range(1,len(self.points)):
            if self.points[i][0] < xmin:
                xmin = self.points[i][0]
            if self.points[i][0] > xmax:
                xmax = self.points[i][0]
        xcenter = .5*(xmin+xmax)

        ymin = self.points[0][1]
        ymax = self.points[0][1]
        for i in range(1,len(self.points)):
            if self.points[i][1] < ymin:
                ymin = self.points[i][1]
            if self.points[i][1] > ymax:
                ymax = self.points[i][1]
        ycenter = .5*(ymin+ymax)

        plottingPoints = []
        scaleFactor = canvasWidth*.8
        for i in range(0,len(self.points)):                                                     #ycoords must be inverted since down is +y
                plottingPoints.append([(self.points[i][0] - xcenter)*scaleFactor+canvasWidth/2, (-1*self.points[i][1] - ycenter)*scaleFactor+canvasHeight/2])

        return plottingPoints
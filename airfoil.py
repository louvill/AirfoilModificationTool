import csv
import random
import numpy

class airfoil:

    def __init__(self):
        self.points = []

    def loadFile(self, fileLocation):
        self.fileLocation = fileLocation
        self.points = list(csv.reader(open(self.fileLocation)))
        for i in range(0,len(self.points)):
            for j in range(0,len(self.points[0])):
                self.points[i][j] = float(self.points[i][j])
    
    def getPlottingPoints(self, canvasWidth, canvasHeight):                                     #converts normalized points to plottable points
        xmin = self.points[0][0]
        xmax = self.points[0][0]
        for i in range(1,len(self.points)):
            if self.points[i][0] < xmin:
                xmin = self.points[i][0]
            if self.points[i][0] > xmax:
                xmax = self.points[i][0]
        xcenter = .5*(xmin+xmax)                                                                #find central x value so that the airfoil can be centered

        ymin = self.points[0][1]
        ymax = self.points[0][1]
        for i in range(1,len(self.points)):
            if self.points[i][1] < ymin:
                ymin = self.points[i][1]
            if self.points[i][1] > ymax:
                ymax = self.points[i][1]
        ycenter = .5*(ymin+ymax)

        plottingPoints = []
        scaleFactor = canvasWidth*.9                                                            #what percent of the screen the airfoil should fill
        for i in range(0,len(self.points)):                                                     #ycoords must be inverted since down is +y
                plottingPoints.append([(self.points[i][0] - xcenter)*scaleFactor+canvasWidth/2, (-1*self.points[i][1] - ycenter)*scaleFactor+canvasHeight/2])

        return plottingPoints
    
    def randomizeGeometry(self):
        numMods = random.randint(1,int(len(self.points)/2))
        #print(numMods)
        for i in range(0, numMods):
            pointNum = random.randint(0,len(self.points)-1)
            #print(pointNum)
            self.points[pointNum][0] = self.points[pointNum][0] + random.randint(-2,2)/1000
            self.points[pointNum][1] = self.points[pointNum][1] + random.randint(-2,2)/1000
        self.normalizeAirfoil()

    def getNumberOfPoints(self):
        return len(self.points)

    def normalizeAirfoil(self):
        ymax = self.points[0][1]
        ymin = self.points[0][1]
        xmax = self.points[0][0]
        xmin = self.points[0][0]
        xMaxLoc = 0
        xMinLoc = 0
        for i in range(0, len(self.points)):
            if self.points[i][0] > xmax:
                xmax = self.points[i][0]
                ymax = self.points[i][0]
                xMaxLoc = i
            if self.points[i][0] < xmin:
                xmin = self.points[i][0]
                ymin = self.points[i][0]
                xMinLoc = i
        rotationAngle = -1*numpy.arctan((ymax-ymin)/(xmax-xmin))
        print(rotationAngle)
        for i in range(0, len(self.points)):
            self.points[i][0] = self.points[i][0]*numpy.cos(rotationAngle)-self.points[i][1]*numpy.sin(rotationAngle)
            self.points[i][1] = self.points[i][0]*numpy.sin(rotationAngle)+self.points[i][1]*numpy.cos(rotationAngle)
        
        chordScale = 1/(self.points[xMaxLoc][0]-self.points[xMinLoc][0])
        #print(chordScale)
        for i in range(0, len(self.points)):
            self.points[i][0] = self.points[i][0]*chordScale
            self.points[i][1] = self.points[i][1]*chordScale

        #deltax = -1*self.points[xMaxLoc][0]
        #deltay = -1*self.points[xMaxLoc][1]

        #for i in range(0, len(self.points)):
        #    self.points[i][0] = self.points[i][0]+deltax
        #    self.points[i][1] = self.points[i][1]+deltay
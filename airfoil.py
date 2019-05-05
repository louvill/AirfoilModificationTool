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
        #ycenter = .5*(ymin+ymax)
        ycenter = 0

        plottingPoints = []
        scaleFactor = canvasWidth*.9                                                            #what percent of the screen the airfoil should fill
        for i in range(0,len(self.points)):                                                     #ycoords must be inverted since down is +y
                plottingPoints.append([(self.points[i][0] - xcenter)*scaleFactor+canvasWidth/2, (-1*self.points[i][1] - ycenter)*scaleFactor+canvasHeight/2])

        return plottingPoints
    
    def randomizeGeometry(self):
        ranOnce = False
        modPoints = []
        while ranOnce == False or self.selfIntersection(modPoints) == True:
            modPoints = []
            for i in range(0, len(self.points)):
                array = []
                for j in range(0, len(self.points[0])):
                    array.append(self.points[i][j])
                modPoints.append(array)
            numMods = random.randint(1,int(len(self.points)/2))
            for i in range(0, numMods):
                pointNum = random.randint(0,len(modPoints)-1)
                modPoints[pointNum][0] = modPoints[pointNum][0] + random.randint(-2,2)/1000
                modPoints[pointNum][1] = modPoints[pointNum][1] + random.randint(-2,2)/1000
            self.normalizeAirfoil(modPoints)
            ranOnce = True
        self.points = modPoints

    def getNumberOfPoints(self):
        return len(self.points)

    def normalizeAirfoil(self, points):
        xmax = points[0][0]
        xmin = points[0][0]
        xMaxLoc = 0
        xMinLoc = 0
        for i in range(0, len(points)):
            if points[i][0] > xmax:
                xmax = points[i][0]
                xMaxLoc = i
            if points[i][0] < xmin:
                xmin = points[i][0]
                xMinLoc = i

        deltax = -1*points[xMinLoc][0]                                                     #shift left most point to origin
        deltay = -1*points[xMinLoc][1]

        for i in range(0, len(points)):
            points[i][0] = points[i][0]+deltax
            points[i][1] = points[i][1]+deltay
        
        #rotate so AoA is zero
        rotationAngle = -1*numpy.arctan((points[xMaxLoc][1]-points[xMinLoc][1])/(points[xMaxLoc][0]-points[xMinLoc][0]))
        for i in range(0, len(points)):
            points[i][0] = points[i][0]*numpy.cos(rotationAngle)-points[i][1]*numpy.sin(rotationAngle)
            points[i][1] = points[i][0]*numpy.sin(rotationAngle)+points[i][1]*numpy.cos(rotationAngle)
        
        chordScale = 1/(points[xMaxLoc][0]-points[xMinLoc][0])
        for i in range(0, len(points)):
            points[i][0] = points[i][0]*chordScale
            points[i][1] = points[i][1]*chordScale
    
    def selfIntersection(self, points):
        intersection = False

        def ccw(A,B,C):
            return (C[1]-A[1])*(B[0]-A[0]) > (B[1]-A[1])*(C[0]-A[0])

        def intersect(A,B,C,D):
            return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

        for i in range(0,len(points)):
            Ax = points[i][0]
            Ay = points[i][1]
            if i == len(points)-1:
                Bx = points[0][0]
                By = points[0][1]
            else:
                Bx = points[i+1][0]
                By = points[i+1][1]
            for j in range(i+2,len(points)-1):
                Cx = points[j][0]
                Cy = points[j][1]
                if j == len(points):
                    Dx = points[0][0]
                    Dy = points[0][1]
                else:
                    Dx = points[j+1][0]
                    Dy = points[j+1][1]
                A = [Ax, Ay]
                B = [Bx, By]
                C = [Cx, Cy]
                D = [Dx, Dy]
                if intersect(A,B,C,D) == True:
                    intersection = True
                    #print("Intersection Detected")
        return intersection
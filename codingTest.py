#!/usr/bin/python

import numpy as np #arrays and their routines
import sys #to read sys.argv
import bokeh.plotting as plot #for graphing
import webbrowser as web #to open graph in a new tab

def lineOfBestFit(X, Y):
    bestFit = np.polyfit(X, Y, 1, full = True)
    
    slope = bestFit[0][0]
    intercept = bestFit[0][1]

    x1 = [min(X), max(X)]
    y1 = [slope*i + intercept for i in x1]

    return (x1, y1, slope, intercept)

def genGraph(X, Y, bestFit):
    boundsY = np.sort(Y) #Note X is already sorted

    TOOLS = 'resize, crosshair, pan, wheel_zoom, box_zoom, reset, box_select, lasso_select'

    graph = plot.figure(tools=TOOLS, x_range=(X[0],X[-1]), y_range=(boundsY[0], boundsY[-1]))
    graph.scatter(X, Y, fill_color='blue') #plot data
    graph.line(bestFit[0], bestFit[1], size=5, color='red', line_width=2) #plot line of best fit

    return graph

if __name__ == '__main__':

#Load data files and separate into X and Y
    dataFile = open(sys.argv[1])
    rawData = np.loadtxt(dataFile, skiprows = 1, usecols = (1,2), delimiter = ',')

    X = rawData[:,0] #Independent variable
    Y = rawData[:,1] #Dependent variable

    bestFit = lineOfBestFit(X,Y)

    plot.output_file('AirPassengersGraph.html', title='Air Passengers Graph') #file saved here

    graph = genGraph(X, Y, bestFit)

    plot.save(graph)

    web.open_new_tab('AirPassengersGraph.html') #opens graph in default browser window

    if bestFit[3] >= 0:
        print 'Line of Best Fit is of the form Y = ' + str(bestFit[2]) + ' * X + ' + str(bestFit[3])
    else:
        print 'Line of Best Fit is of the form Y = ' + str(bestFit[2]) + ' * X - ' + str(abs(bestFit[3]))

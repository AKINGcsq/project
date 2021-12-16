from galogic import *
import matplotlib.pyplot as plt
import progressbar
pbar = progressbar.ProgressBar()

import os

path = os.getcwd()

fileList = os.listdir(path+'/dataset')
for i in range(len(fileList)):
    fileList[i] = path + '/dataset/' + fileList[i]

filename = fileList[3]
c = 0
city_list = []
with open(filename) as f:
    while True:
        line = f.readline()
        if not line:
            break
            pass
        if len(line) > 4:
            x = line.split(' ')[1]
            y = line.split(' ')[2].replace('\n','')
            city_list.append([x,y])
numNodes = len(city_list)
# Add Dustbins
for i in range(numNodes):
    RouteManager.addDustbin(Dustbin(int(city_list[i][0]), int(city_list[i][1])))

random.seed(seedValue)
yaxis = [] # Fittest value (distance)
xaxis = [] # Generation count

pop = Population(populationSize, True)
globalRoute = pop.getFittest()
print ('Initial minimum distance: ' + str(globalRoute.getDistance()))

# Start evolving
for i in pbar(range(numGenerations)):
    pop = GA.evolvePopulation(pop)
    localRoute = pop.getFittest()
    if globalRoute.getDistance() > localRoute.getDistance():
        globalRoute = localRoute
    yaxis.append(localRoute.getDistance())
    xaxis.append(i)

print ('Global minimum distance: ' + str(globalRoute.getDistance()))
print ('Final Route: ' + globalRoute.toString())

fig = plt.figure()

plt.plot(xaxis, yaxis, 'r-')
plt.show()

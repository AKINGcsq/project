from dustbin import *
import os

path = os.getcwd()

fileList = os.listdir(path+'/dataset')
for i in range(len(fileList)):
    fileList[i] = path + '/dataset/' + fileList[i]

filename = fileList[5]
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

print(len(city_list))
print(city_list[1][1])



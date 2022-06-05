file = 'D:\Code\gnssbox\gnssbox\lib\IGSNetwork.csv'
fileData = open(file, 'r+').readlines()
for line in fileData:
    print(line.split(','))
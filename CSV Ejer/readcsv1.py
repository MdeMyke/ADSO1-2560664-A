import csv
with open('C:\\rutas\\Csvruta\\malee.csv') as csvDataFile:
#with open('files/people.csv') as csvDataFile:
    csvReader=csv.reader(csvDataFile)
    #print(csvReader)
    for row in csvReader:
        #print(row)
        print('mindex:',row[0])
        print('myear:',row[1])
        print('mage:',row[2])
        print('mname:',row[3])
        print('mmovie:',row[4])



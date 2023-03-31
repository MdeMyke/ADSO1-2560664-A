from Male import *
import csv
listamalefemale=[]
with open('C:\\rutas\\Csvruta\\malee.csv') as csvDataFile:


    csvReader=csv.reader(csvDataFile)    
    for row in csvReader:
        obm=Male(row[0],row[1],row[2],row[3],row[4])
        listamalefemale.append(obm)
        #print(row)
        # print('first name:',row[0])
        # print('last name:',row[1])
        # print('email:',row[2])
        # print('id:',row[3])
print(listamalefemale)
for aprendiz in listamalefemale:
    print(listamalefemale[10])





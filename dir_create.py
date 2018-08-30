import csv
import os


directory = ''

with open('2010-2013VehDB_YMML_AUG18.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile, delimiter=',')
    for row in csvReader:
        if any(row):
            directory = 'D:/otherwebsites/carspot/Vehicles/' + row[0] + '/' + row[1] + '/' + row[2]
            if not os.path.exists(directory):
                try:
                    os.makedirs(directory)
                except:
                    pass
                    
with open('2014-2019VehDB_YMML_AUG18.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile, delimiter=',')
    for row in csvReader:
        if any(row):
            directory = 'D:/otherwebsites/carspot/Vehicles/' + row[0] + '/' + row[1] + '/' + row[2]
            if not os.path.exists(directory):
                try:
                    os.makedirs(directory)
                except:
                    pass                    
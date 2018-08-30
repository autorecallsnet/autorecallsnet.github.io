import csv

prevRow = ['','']
prevMake = ''
prevModel = ''
pmakes = []
makes = []
pmodels = []
models = []
num = 0


#col = 1 for make and col = 2 for model, etc.
with open('2014-2019VehDB_YMML_AUG18.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile, delimiter=',')
    for row in csvReader:
        if any(row):
            if (row[1] != prevRow[1]):
                prevRow = row
                pmakes.append(row[1])

with open('2010-2013VehDB_YMML_AUG18.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile, delimiter=',')
    for row in csvReader:
        if any(row):
            if (row[1] != prevRow[1]):
                prevRow = row
                pmakes.append(row[1])
                
pmakes.sort()                
for make in pmakes:
    if (make != prevMake):
        prevMake = make
        makes.append(make)

prevRow = ['','','']        
        
with open('2014-2019VehDB_YMML_AUG18.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile, delimiter=',')
    for row in csvReader:
        if any(row):
            if (row[2] != prevRow[2]):
                prevRow = row
                pmodels.append(row[2])

with open('2010-2013VehDB_YMML_AUG18.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile, delimiter=',')
    for row in csvReader:
        if any(row):
            if (row[2] != prevRow[2]):
                prevRow = row
                pmodels.append(row[2])
                
pmodels.sort()                
for model in pmodels:
    if (model != prevModel):
        prevModel = model
        models.append(model)
        
with open('index.html', 'r') as ind:
    with open('newindex.html', 'a+') as newInd: 
        for line in ind.readlines():
            if (line.find('<!--<<BEGIN MAKES>>-->') != -1):
                newInd.write(line)
                for make in makes:                    
                    newInd.write("\n                                             <option>" + make + "</option>")
            elif (line.find('<!--<<BEGIN MODELS>>-->') != -1):
                newInd.write(line)
                for model in models:
                    newInd.write("\n                                             <option>" + model + "</option>")
            else:
                newInd.write(line)
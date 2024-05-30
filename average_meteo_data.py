#averaging meteo data
path = "/Users/amelonelie/Documents/Master EMMA/semester 2/advanced geomatics+EIA/advanced geomatics/02/data/rain_data_1year.txt"

with open(path, 'r') as file:
    lines =file.readlines()
    
monthlyDataDict = {}
for line in lines[1:]: # to not take the header
    line = line.strip()
    lineSplit = line.split(",")
    date = lineSplit[0]
    value = float(lineSplit[1])
    yearMonth = date[:-2] # to miss the last two characters (days)
    dataPerMonth = monthlyDataDict.get(yearMonth, []) # to get the existing list or creating a new one by []
    dataPerMonth.append(value) # appending to the list
    #data per month: only used temporary
    monthlyDataDict[yearMonth] = dataPerMonth  # putting it info the dictionary
for yearMonth, valuesList in monthlyDataDict.items():
    cumulated = 0
    count = 0
    for value in valuesList:
        if value != -9999.0: #error in the dataset
            cumulated += value
            count += 1
            
    avg = cumulated/count
    
    month = yearMonth[4:] # to leave out the year
    print("month", month, "cumulated: ", cumulated, "/ average:", avg)
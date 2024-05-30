def fileSummary(path, idFieldName, avgFieldName):
    with open(path, 'r') as file:
        lines = file.readlines()
    idIndex = None
    analyzeIndex = None
    for line in lines[:10]:
        line = line.strip()
        if line.startswith("#"):
            #we have the header
            fields = line[1:].split(",")
            for index, field in enumerate(fields):
                field = field.strip()
                if field == idFieldName:
                    idIndex = index
                elif field == avgFieldName:
                    analyzeIndex = index
        else:
            pass
                    
                    
                    
    print(f"Fileinfo: {path}")
    print("================")
    print("Fields:")
    for field in fields:
        print(f"->{field.strip()}")
fileSummary("/Users/amelonelie/Documents/Master EMMA/semester 2/advanced geomatics+EIA/advanced geomatics/01/stations.txt", "STATID", "RR")
print("********************")
fileSummary("/Users/amelonelie/Documents/Master EMMA/semester 2/advanced geomatics+EIA/advanced geomatics/01/station_data.txt", "CN", "HEIGHT")
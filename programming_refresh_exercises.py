folder = "/Users/amelonelie/Documents/Master EMMA/semester 2/advanced geomatics+EIA/advanced geomatics/01/"


# exercise 1

age = 25
name = "Mario Rossi"
activity = "skating"
job = "engineer"

print(f"Hei, I am {name}\nI am {age} and I love to go {activity}\nI work as an {job}")


# exercise 2
import pandas as pd
csv_path = f"{folder}01_exe2_data.csv"

with open(csv_path, 'r') as file:
    lines =file.readlines()
    
    
for line in lines:
    line = line.strip()             # strip removes whitespaces
    lineSplit = line.split(";")
    analogString = lineSplit[0]
    analogSplit = analogString.split(":")
    x1 = float(analogSplit[1])
                                    #other variant with slicing
    maxvoltageString = lineSplit[1]
    y2 = float(maxvoltageString[11:])

    maxanalogString = lineSplit[2]
    x2 = float(maxanalogString[10:])
    y1 = (x1/x2)*y2
    print(y1)
    
#exercise 3
string= "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s"
new_string = string.replace(",",";")
print(new_string)

# exercise 4
list = [1,2,3,4,5]
for i in list:
    print(i)
    
# exercise 5
for i in list:
    print(f"Number {i}")

# exercise 6
list_a = [10,20,30,40,50,60,70,80,90,100]
list_b = list_a[:5]
    
for i in list_b:
    print(f"Number {i}")
    
#exercise 7
list1 = list
list2 = ["first", "second", "third", "fourth", "fifth"]
for item1, item2 in zip(list,list2):
    print(f"{item2} is {item1}")

#exercise 8
string = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum."""

characters = len(string)
new_string = string.replace(" ", "")
no_space_characters = len(new_string)
words = string.split(" ")
count_words =len(words)
print(f"Characters count: {characters}\nCharacters count without spaces: {no_space_characters}\nWord count: {count_words}")

#exercise 9
csv_path2 = f"{folder}01_exe9_data.csv"
with open(csv_path2, 'r') as file:
    lines =file.readlines()

for line in lines:
    line = line.strip()
    if "#" not in line and line: # first checks if there is a hashtag inside, second checks if its am empty string
        print(line)

# exercise 10
for line in lines:
    line = line.strip()
    if "#" not in line and line and float(line[3:]) < 1000: 
        print(line)

#exercise 11
csv_path3 = f"{folder}01_exe11_data.csv"
with open(csv_path3, 'r') as file:
    lines =file.readlines()

for line in lines:
    line = line.strip()    
    lineSplit = line.split(";")
    baseString = lineSplit[0]
    base = float(baseString[5:-2])
    heightString = lineSplit[1]
    height = float(heightString[7:])
    height = height * 100
    result = base * height / 2
    print(f"base * height / 2 = {base} * {height} = {result}cm2")

# exercise 12
who = {
"Daisy": 11,
"Joe": 201,
"Will": 23,
"Hanna": 44} 

what = {
44: "runs",
11: "dreams",
201: "plays",
23: "walks"} 

where = {
44: "to town.",
11: "in her bed.",
201: "in the livingroom.",
23: "up the mountain."}

for key, value in who.items(): #does not work if you write only who
    activity = what.get(value, "unknown activity")
    location = where.get(value, "unknown location")
    print(f"{key} {activity} {location}")


#variation
who = {
"Daisy": 11,
"Joe": 201,
"Will": 23,
"Hanna": 44} 
what = {
44: "runs",
11: "dreams",
201: "plays",
23: "walks"} 

where = {
"runs": "to town.",
"dreams": "in her bed.",
"plays": "in the livingroom.",
"walks" : "up the mountain."}

for key, value in who.items():
    activity = what.get(value, "unknown activity")
    location = where.get(activity, "unknown activity")
    print(f"{key} {activity} {location}")
    
    
# exercise 13
list1 = ["a", "b", "c", "d", "e", "f"]
list2 = ["c", "d", "e", "f", "g", "h", "a"]
list3 = ["c", "d", "e", "f", "g"]
list4 = ["c", "d", "e", "h", "a"]
whole_list = list1+list2+list3+list4
print(whole_list)

char_dict = {}
for char in whole_list:
    count = char_dict.get(char, 0) # check if this char is already in the dict, take its value or take 0
    count += 1 # increase the value of appearance of the char
    char_dict[char] = count # put it back into the dict

for key, value in char_dict.items():
    print("count of", key, "=", value)

# exercise 14
path = f"{folder}stations.txt"

with open(path, 'r') as file:
     station_lines =file.readlines()
linenumber = 20
counter = 0 
for line in station_lines:
    counter +=1
    if counter < linenumber:
        print(line)

# exercise 15
count = 0
for line in station_lines:
    if line.startswith("#") or len(line) == 0:
        continue
    count += 1

print(count)

# exercise 16
linenumber = 5
counter = 0 
for line in station_lines:
    line = line.strip()  
    stationSplit = line.split(",")
    counter +=1
    if counter < linenumber:
        print(stationSplit)
print(len(stationSplit))

# exercise 17
for line in station_lines[:20]:
    line = line.strip()  
    stationSplit = line.split(",")
    stationid = stationSplit[0]
    station_name = stationSplit[1]
    if line.startswith("#") or len(line) == 0:
        continue
    print(stationid, station_name)
# exercise 18
heights = []
for line in station_lines:
    line = line.strip()  
    stationSplit = line.split(",")
    if line.startswith("#") or len(line) == 0:
        continue
    station_height = float(stationSplit[5])
    heights.append(station_height)    
    average_height = (sum(heights)/len(heights))    
print(average_height)

# exercise 19
def fileinfo(path):

    station_count = 0
    heights = []
    available_fields = []
    first_data_lines = []

    with open(path, 'r') as file:
        header_line = file.readline()
        header_line_stripped = header_line.strip()
        column_names_split = header_line_stripped.split(',')
        cleaned_column_names = []
        for column_name in column_names_split:
            cleaned_column_name = column_name.strip()
            cleaned_column_name = cleaned_column_name.replace("#", "")
            cleaned_column_names.append(cleaned_column_name)
        column_names = cleaned_column_names
        
        station_lines =file.readlines()
        for line in station_lines:
            line = line.strip() 
            stationSplit = line.split(",")
            if line.startswith("#") or len(line) == 0:
                continue
            station_count += 1
            station_height = float(stationSplit[5])
            heights.append(station_height)    
            average_height = (sum(heights)/len(heights))
            if len(first_data_lines) < 2:
                first_data_lines.append(line)
    print("File info: {}".format(path))
    print("-----------------------")
    print("Stations count:", station_count)
    print("Average value:", average_height)
    print("Available fields:")
    print(column_names)
    print("First data lines:")
    for data_line in first_data_lines:
        print(data_line)

fileinfo(path)

# exercise 20
path2 = f"{folder}station_data.txt"
def fileinfo2(path2):

    station_count = 0
    RR = []
    available_fields = []
    first_data_lines = []

    with open(path2, 'r') as file:
        header_line = file.readline()
        header_line_stripped = header_line.strip()
        column_names_split = header_line_stripped.split(',')
        cleaned_column_names = []
        for column_name in column_names_split:
            cleaned_column_name = column_name.strip()
            cleaned_column_name = cleaned_column_name.replace("#", "")
            cleaned_column_names.append(cleaned_column_name)
        column_names = cleaned_column_names
        
        station_lines =file.readlines()
        for line in station_lines:
            line = line.strip() 
            stationSplit = line.split(",")
            if line.startswith("#") or len(line) == 0:
                continue
            station_count += 1
            station_RR = float(stationSplit[4])
            RR.append(station_RR)    
            average_RR = (sum(RR)/len(RR))
            if len(first_data_lines) < 2:
                first_data_lines.append(line)
    print("File info: {}".format(path2))
    print("-----------------------")
    print("Stations count:", station_count)
    print("Average value:", average_RR)
    print("Available fields:")
    print(column_names)
    print("First data lines:")
    for data_line in first_data_lines:
        print(data_line)
fileinfo2(path2)     
#exercise 21
n = 10
m = 5
for asteriscs in range(n):
    print(m*"* ")
# exercise 22
counter = 1
for asteriscs in range(n):
    print(counter*"*")
    counter += 1   
    
# exercise 23
counter = 10
for asteriscs in range(n):
    print(counter*"*")
    counter -= 1   
    
# exercise 24
a = 10
list = []
for i in range(0,a+1): # because range does not take the last number
    if i%2 == 0:
        list.append(i)
print(sum(list))

# exercise 25
numbers = [123, 345, 5, 3, 8, 87, 64, 95, 9, 10, 24, 54, 66]
even_numbers = []
for i in numbers:
    if i%2 == 0:
        even_numbers.append(i)
print(sum(even_numbers))


#exercise 26
csv_path4 = f"{folder}01_exe26_dataset1.csv"
csv_path5 = f"{folder}01_exe26_dataset2.csv"

with open(csv_path4, 'r') as file:
    dataset1 =file.readlines()
with open(csv_path5, 'r') as file:
    dataset2 =file.readlines()
    
data_dict = {}
ids = []

for line in dataset1:
    line = line.strip()    
    if line.startswith("#") or len(line) == 0:
        continue
    lineSplit = line.split(",")
    id = lineSplit[0]
    data_dict[id] = (float(lineSplit[1]), float(lineSplit[2]))

for line in dataset2:
    line = line.strip()
    if line.startswith("#") or len(line) == 0:
        continue
    lineSplit = line.split(",")
    id = lineSplit[0]
    if id in data_dict:
        existing_tuple = data_dict[id]
        data_dict[id] = (existing_tuple[0], existing_tuple[1], float(lineSplit[1]))
print(data_dict)

    
    
    
    
    
    
    
#using quote parameter to read the number in as floats

import csv

FILENAME = "week1lab.csv"
DATADIR = "C:/Users/angel/OneDrive/College/pfda/PFDA-mywork/Week.01.lab/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    count = 0 
    total = 0
    for line in reader:
        total += line['age']
        print (line)
        count += 1
    print (f"average is {total/(count)}") #why no -1 this time? because reading as a dictionary we are automatically only counting the values for the age column and not the lines. Therefore we do not have the additional +1 as we did when using the lines as a counter
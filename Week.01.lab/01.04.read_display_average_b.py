#using quote parameter to read the number in as floats

import csv

FILENAME = "week1lab.csv"
DATADIR = "C:/Users/angel/OneDrive/College/pfda/PFDA-mywork/Week.01.lab/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    linecount = 0 
    total = 0
    for line in reader:
        if not linecount: # first row is header row
            pass
        else: #all subsequent rows
            total += line[1] 

        linecount += 1
    print (f"average is {total/(linecount-1)}") #why -1?
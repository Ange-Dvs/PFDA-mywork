import csv

FILENAME = "week1lab.csv"
DATADIR = "C:/Users/angel/OneDrive/College/pfda/PFDA-mywork/Week.01.lab/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0 
    total = 0
    for line in reader:
        if not linecount: # first row is header row
            pass
        else: #all subsequent rows
            total += int(line[1]) #why 1? 1 is the index for the age column
        linecount += 1
    print (f"average is {total/(linecount-1)}") # why -1? because we are adding 1 on at the end of each itteration of the loop and is counting the header aswell 4 lines total but we only have 3 ages
        
import csv

FILENAME = "week1lab.csv"
DATADIR = "C:/Users/angel/OneDrive/College/pfda/PFDA-mywork/Week.01.lab/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0 
    for line in reader:
        if not linecount: # first row is header row
            print (f"{line}\n--------------------------")
        else: #all subsequent rows
            print (line)
        linecount += 1
        
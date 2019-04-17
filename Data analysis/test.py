import csv

file= open("data.csv","r")
reader= csv.reader(file)

for line in reader:
    t= line[0],line[1]
    print(t)


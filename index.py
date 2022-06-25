import csv

# 1: get compound names
with open('file.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
# some stuff that is supposed to be in line 1 is in line 2, we can easily identify it because
# it has an empty space " ", so we loop through line 1 and if there is a space we get the same index
# in line two 
compound_name = data[0]
line2 = data[1]
for idx, x in enumerate(compound_name):
    # print(idx, x)
    if x == '':
        compound_name[idx] = line2[idx]

# print(compound_name)


# 2: create dynamic variable names and assign empty lists why: https://www.geeksforgeeks.org/python-read-csv-columns-into-list/
number_of_compounds = len(compound_name)+1
for x in range(0, number_of_compounds):
    globals()['compound%s' % x] = []
# print(compound61)


# 3: iterating over each row and append values to empty list created in (#2)
# go row for row and assign compound name to its element
# open the file in read mode
filename = open('file.csv', 'r')
 
# creating dictreader object
file = csv.DictReader(filename)
# iterating over each row and append
# values to empty list
# for col in file:
    # print(col[compound_name[0]])


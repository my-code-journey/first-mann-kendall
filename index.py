import csv

# 1: get compound names
with open('file.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
# some stuff that is supposed to be in line 1 is in line 2, we can easily identify it because
# it has an empty space " ", so we loop through line 1 and if there is a space we get the same index
# but in line two 
compound_name = data[0]
line2 = data[1]
for idx, x in enumerate(compound_name):
    # print(idx, x)
    if x == '':
        compound_name[idx] = line2[idx]

print(compound_name)

# 2: go row for row and assign compound name to its element
# # open the file in read mode
# filename = open('file.csv', 'r')
 
# # creating dictreader object
# file = csv.DictReader(filename)
# # iterating over each row and append
# # values to empty list
# for col in file:
#     # print(col["Phenol     (ug/L)"])
#     print(col[0])


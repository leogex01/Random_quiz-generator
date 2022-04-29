import csv

dict_from_csv = ()

with open('Periodic Table of Elements.csv', mode='r') as inp:
    reader = csv.reader(inp)
    dict_from_csv = {rows[1]: rows[0] for rows in reader}

print(dict_from_csv)
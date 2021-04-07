__author__ = 'Alvaro Munoz'

import csv
import re


in_file = open("*/customers.csv", "r")
reader = csv.reader(in_file)
out_file = open("*/masked_clients.csv", "w")
writer = csv.writer(out_file)

for row in reader:
    newrow = [re.sub('[a-zA-Z]', 'X', item) for item in row]
    writer.writerow(newrow)

in_file.close()
out_file.close()


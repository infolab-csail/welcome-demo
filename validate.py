import sys
import csv

with open('numbers.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        # check that names are capitalized
        name = row['name']
        if not name[0].isupper():
            sys.exit("'%s' needs to be a capitalized name" % name)

        # check that favorite numbers are valid ints
        int(row['number'])

#!/usr/bin/env python

import csv


def dataset(path):
    with open(path, 'rU') as data:
        reader = csv.reader(data)
        for row in reader:
            row[2] = int(row[2])
            yield row

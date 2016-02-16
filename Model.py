import csv
import os


class Model(object):
    def readcsv(self, filename):
        returnstring = ""

        if os.path.isfile(filename) and filename.endswith(".csv"):
            with open(filename) as csvfile:
                reader = csv.reader(csvfile, delimiter=";")
                for row in reader:
                    for i in row:
                        returnstring += str(i) + "\t"
                    returnstring += "\n"
        else:
            returnstring = "The given Name is no valid csv file"
        return returnstring

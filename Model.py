import csv

class Model(object):
    def readcsv(self,filename):
        returnstring = ""
        with open(filename) as csvfile:
            reader = csv.reader(csvfile, delimiter=";")
            for row in reader:
                for i in row:
                    returnstring += str(i)+"\t"
                returnstring += "\n"
            print(returnstring)
            return returnstring
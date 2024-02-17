import csv

target_file = 'food_data/datafile.csv'

def get_info():
    with open(target_file, "r") as csvfile:
        reader = csv.DictReader(csvfile)

        datalist = {}
        for row in reader:
            #print(row)
            for element in row:
                if element in datalist:
                    datalist[element] += [row.get(element).split(":")]
                else:
                    datalist[element] = [row.get(element).split(":")]
            #print(" ")
        #print("FINAL RESULT:")
        #present_data = str(datalist).replace("],","],\n")
        #print(present_data)

        return datalist

if __name__ == "__main__":
    get_info()
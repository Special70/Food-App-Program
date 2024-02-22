import csv

target_file = 'food_data/datafile.csv'

def get_info(getinfo="keys"):
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
        if getinfo == "keys":
            keys = []
            for i in datalist.keys():
                keys.append(i)
            return keys
        elif getinfo == "products":
            present_data = datalist
            new_data = []
    
            for iteration in present_data:
                for item in present_data[iteration]:
                    if str(item) == "['']":
                        continue
                    new_data.append(item[0])
                    #print(item)
            return new_data
        elif getinfo == "products and shop info":
            present_data = datalist
            new_data = []
            
            for iteration in present_data:
                
                for item in present_data[iteration]:
                    if str(item) == "['']":
                        continue
                    new_data.append([str(item[0]+" : $"+item[1]), iteration])
                    # Product Name, Shop Name, Price
            return new_data

if __name__ == "__main__":
    print(get_info("products and shop info"))
import csv

target_file = 'records/food_datafile.csv'
getinfo_keys = []
getinfo_products = []
getinfo_products_and_shop_info = []

with open(target_file, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    datalist = {}
    for row in reader: # row == csv file row (contains values in that row including blanks)
        for element in row: # element == target column when reading each column in a row which is the shop name
            if row.get(element) == "": # Ignores empty fields
                continue
            if element in datalist: # If shop is recorded at least once
                datalist[element] += [row.get(element).split(":")]
            else: # If shop has yet to be recorded in the dictionary
                datalist[element] = [row.get(element).split(":")]
                
# Key Getters:
for iteration in datalist.keys():
    getinfo_keys.append(iteration)
    
# All Product Value Getters:
for iteration in datalist:
    for item in datalist[iteration]:
        if str(item) == "['']":
            continue
        getinfo_products.append(item[0])
        
# Product and Shop Getters:
for iteration in datalist:
    for item in datalist[iteration]:
        if str(item) == "['']":
            continue
        getinfo_products_and_shop_info.append([str(item[0]+" : $"+item[1]), iteration])
        # Product Name, Shop Name, Price
    

def get_info(getinfo="keys", targetkey="") :
    if getinfo == "keys":
        return getinfo_keys
    elif getinfo == "products":
        return getinfo_products
    elif getinfo == "products and shop info":
        return getinfo_products_and_shop_info
    elif getinfo == "shop products":
        return datalist[targetkey]
    
# Testing area
if __name__ == "__main__":
    #print(datalist["Savory Bites Bistro"])
    pass
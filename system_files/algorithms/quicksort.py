from random import randrange

# Quicksort Algorithm deals with modifying the object
# Modified a bit so it checks for the index 1 (price value) of the list

def algorithm(given_list, start, end):
    if start > end:
        return
    pivot_idx = randrange(start, end+1)
    pivot_element = float(given_list[pivot_idx][1])

    given_list[end], given_list[pivot_idx] = given_list[pivot_idx], given_list[end]
    
    less_than_pointer = start

    for i in range(start, end):
        if float(given_list[i][1]) < pivot_element:
            given_list[i], given_list[less_than_pointer] = given_list[less_than_pointer], given_list[i]
            less_than_pointer += 1
    given_list[end], given_list[less_than_pointer] = given_list[less_than_pointer], given_list[end]

    algorithm(given_list, start, less_than_pointer-1)
    algorithm(given_list, less_than_pointer+1, end)


def _self(givenList):
    algorithm(givenList, 0, len(givenList)-1)

if __name__ == "__main__":
    # Testing Area
    testlist = [['Teriyaki Chicken Bowl', '9.50'], ['Hawaiian Pizza', '12.99'], ['Chicken Quesadilla', '8.75'], ['Mango Tango Smoothie', '6.99'], ['Beef Stir Fry', '11.25'], ['Veggie Wrap', '7.50'], ['Coconut Shrimp', '10.99'], ['Greek Salad', '9.75'], ['Tofu Pad Thai', '10.50'], ['BBQ Pork Sandwich', '8.99']]
    _self(testlist)
    print(testlist)
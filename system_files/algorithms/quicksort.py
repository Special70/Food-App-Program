from random import randrange

def algorithm(given_list, start, end):
    if start > end:
        return
    pivot_idx = randrange(start, end+1)
    pivot_element = given_list[pivot_idx]

    given_list[end], given_list[pivot_idx] = given_list[pivot_idx], given_list[end]
    
    less_than_pointer = start

    for i in range(start, end):
        if given_list[i] < pivot_element:
            given_list[i], given_list[less_than_pointer] = given_list[less_than_pointer], given_list[i]
            less_than_pointer += 1
    given_list[end], given_list[less_than_pointer] = given_list[less_than_pointer], given_list[end]

    algorithm(given_list, start, less_than_pointer-1)
    algorithm(given_list, less_than_pointer+1, end)


def _self(givenList):
    return algorithm(givenList, 0, len(givenList)-1)

if __name__ == "__main__":
    testlist = [3, 6, 2, 5, 1]
    print(_self(testlist))
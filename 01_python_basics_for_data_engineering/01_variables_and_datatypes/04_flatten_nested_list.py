def flatten(nested_list):
    return [item for sublist in nested_list for item in sublist]
    # This line flattens the nested list by iterating through each sublist in the nested list,
    # and then iterating through each item in those sublists to create a single flat list.


if __name__ == "__main__":
    nestedList = [[1, 2], [3, 4], [5]]
    output = flatten(nestedList)  
    print(output)

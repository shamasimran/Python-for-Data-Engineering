def flatten(nested_list):
    return [item for sublist in nested_list for item in sublist]

if __name__ == "__main__":
    print(flatten([[1, 2], [3, 4], [5]]))

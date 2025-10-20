import csv
import os

def write_csv(data, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def read_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return list(reader)

if __name__ == "__main__":
    data = [["name", "age"], ["John", 28], ["Jane", 22]]
    write_csv(data, "example.csv")
    print(read_csv("example.csv"))
    # Delete a File    
    os.remove("demofile.txt")

    if os.path.exists("demofile.txt"):
        os.remove("demofile.txt")
    else:
        print("The file does not exist")

    os.rmdir("myfolder")

import csv
import os
from pathlib import Path
import sys

def write_csv(data, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def read_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return list(reader)


def create_folder_in_exe_directory(folder_name):
    # Get the path of the executable or the Python script
    if getattr(sys, 'frozen', False):
        # Running as a compiled .exe
        base_path = Path(sys.executable).parent
    else:
        # Running as a .py script
        base_path = Path(__file__).parent
    # Define the folder to create (e.g., "logs" inside the exe directory)
    folder_path = base_path / folder_name
    # Create the folder if it doesn't exist
    folder_path.mkdir(parents=True, exist_ok=True)
    print(f"Folder created (if not exists): {folder_path}")
    return str(folder_path)

if __name__ == "__main__":
    data = [["name", "age"], ["John", 28], ["Jane", 22]]

    path = create_folder_in_exe_directory("logs")
    file_path = os.path.join(path, "example.csv")
    write_csv(data, file_path)
    print(read_csv(file_path))
    
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print(f"The file does not exist: {file_path}")

    os.rmdir(path)

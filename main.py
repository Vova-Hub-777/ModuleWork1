def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"File {file_name} was not found.")
        return []
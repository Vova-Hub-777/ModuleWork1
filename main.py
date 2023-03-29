def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"File {file_name} was not found.")
        return []

def write_file(file_name, content):
    with open(file_name, 'w') as file:
        file.writelines(content)

def main():
    file1_name = input("Enter the name of the first file (with .txt extension): ")
    file2_name = input("Enter the name of the second file (with .txt extension): ")

    file1_content = read_file(file1_name)
    file2_content = read_file(file2_name)

    same_content = []
    diff_content = []

    for line in file1_content:
        if line in file2_content:
            same_content.append(line)
        else:
            diff_content.append(line)

    for line in file2_content:
        if line not in file1_content:
            diff_content.append(line)

    write_file("same.txt", same_content)
    write_file("diff.txt", diff_content)

    print("Comparison completed. Results saved in 'same.txt' and 'diff.txt'.")


if __name__ == "__main__":
    main()
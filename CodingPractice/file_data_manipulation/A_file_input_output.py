
FILE = "/Learning/file_add_line.txt"
FILE_PI = "/Learning/file.txt"
FILE_LOGS = "../logs/logs.txt"

def insert_line_into_text(file_location:str, previous_line, new_line):
    with open(file_location, "r") as in_file:
        buffer = in_file.readlines()
        for line in buffer:
            if new_line in line:
                print(f"'{new_line}' already exists in file")
                return 0
    with open(file_location, 'w') as out_file:
        for line in buffer:
            if line == previous_line:
                line = line + new_line
            out_file.write(line)

if __name__ == "__main__":
    # printout file content into a one string
    with open(FILE) as file_obj:
        data = file_obj.read()
    print(f"File_obj.read() which reads file in its entirety as string = \n{data}")

    # printout file contents into lists
    with open(FILE_PI) as fobj:
        for line in fobj:
            print(line, end="")

    with open(FILE) as fobject:
        data_list = fobject.readlines()
    print(data_list)

    # Printing large files into chunks
    with open(FILE_LOGS) as fobject:
        while True:
            chunk = fobject.read(100)
            if not chunk:
                break
            print(chunk, end="")
    print()

    # write to file
    with open(FILE, 'a') as file_obj:
        file_obj.write("\nyuya")

    # add new line into file
    previous_line = "testarrosa\n"
    new_line = "abc\n"
    insert_line_into_text(FILE, previous_line, new_line)
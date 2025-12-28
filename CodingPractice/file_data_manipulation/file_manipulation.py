def fm_read(path):
    with open(path, 'r') as obj:
        lines = obj.readlines()
        for line in lines:
            print(line)

def fm_append(path, appended):
    with open(path, 'a') as obj:
        # lines = obj.readlines()
        obj.write(appended)
        # for line in lines:
        #     if line == "Hola!":


path = "/Users/carlosquiroz/dev/python/CodingPractice/file_data_manipulation/table.txt"
fm_read(path)
appended = "\ntest"
fm_append(path, appended)

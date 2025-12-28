'''
@author: Solrac
'''
def filter_onemin_duration(file_location):
    lines = open(file_location)
    listLines = lines.readlines();
    
    for line in listLines:
        list_ = line.split("    ")
        if len(list_) == 15:
            day_list1 = list_[11].split('/')
            day_list2 = list_[13].split('/')
            if day_list1[0] == day_list2[0]:
                hour_list1 = list_[12].split(':')
                hour_list2 = list_[14].split(':')
                if (hour_list1[0] == hour_list2[0]) or (hour_list1 == 11 and hour_list2 == 12):
                    min1 = hour_list1[1].strip('am')
                    min2 = hour_list2[1].strip('am\n')
                    if int(min2) - int(min1) == 1:
                        print(list_)

def findscore(xml_file_location):
    lines = open(xml_file_location)
    lista = lines.readlines()
    counter = 0
    for line in lista:
        counter += line.count("=")
    print(counter)
    
file_location = "C:/Users/Solrac/workspace/Python.Development/InterviewPractice/table.txt"
filter_onemin_duration(file_location)

xml_file_location = "C:/Users/Solrac/workspace/Python.Development/InterviewPractice/file.xml"
findscore(xml_file_location)
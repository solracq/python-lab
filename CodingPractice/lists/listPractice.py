'''
@author: Solrac
'''
from CodingPractice.lists.finding_duplicates_List import *
from CodingPractice.find_sums.findmax import findmax
import time

start_time = time.time()

def lists():
    numbers = [1,2,3,4,5]
    mythical = ["Unicorn", "Balrog", "Vampire", "Dragon", "Minotaur"]
    everything_ = numbers+mythical
    print(str(numbers[1:3])+" "+mythical[4])
    print(numbers[:-2])
    print(everything_)
    
    # adding elements
    everything_ = everything_+[89]
    everything_ = everything_+["Apple"]
    print(everything_)
    numbers.append(333)
    mythical.append("Nessie")
    print(numbers)
    print(mythical)
    numbers.insert(3, 45)
    mythical.insert(3, "Siren")
    print(numbers + mythical)
    print("Printing content with index")
    for i in mythical:
        print(str(mythical.index(i))+" "+i)
    
    # deleting elements
    print(numbers)
    del numbers[3]
    print("after delete",numbers)
    print(mythical)
    del mythical[-6:-5]
    print("after delete",mythical)
    mythical.remove("Nessie")
    print("after removing 'Nessie'",mythical)
    mythical.pop(2) # removing index
    print("after removing obj in index 2",mythical)
    
    # Other
    mythical.sort()
    print(mythical)
    mythical.reverse()
    print(mythical)
    
    # Equivalent of toCharArray
    name = "Carmelita Quiroz Perez"
    name_list = list(name)
    print(name_list)
    
    # finding element in string
    for element in name_list:
        if element == 'Q':
            print("found "+str(element)+" in position "+str(name_list.index(element)))
    
    # finding duplicates    
    print()
    list_s=["a", "b", "c", "d", "d"]
    print("finding duplicates in list: ", list_s)
    for k in range(len(list_s)-1):
        if list_s[k]==list_s[k+1]:
            print("Duplicates of " +list_s[k] +" at "+ str(list_s.index(list_s[k]))+" and "+str(list_s.index(list_s[k+1])))        
    print()
    string_ky= "saeya"
    string_list = list(string_ky)
    print(string_list)
    print("does the above list contain duplicates? "+str(is_duplicate(string_list)))
    find_duplicate(string_list)
    print("Does the above list contain duplicates using set? "+str(find_duplicates_set(string_list)))
    print("Frequency of 'a' in list: "+str(string_list.count('a')))
    print("does the above list contain duplicates? "+str(find_duplicate_count(string_list)))
    
    # finding max
    list_=[3, 5, 7, 1, 9, 6, 89, 2]
    print(list_)
    print("Maximum value: ", findmax(list_))
    print("max: ", max(list_))
    print("max: ", min(list_))
    
    # combining different types in a list
    listT=["Voldo", 5, "Valeria", 9, "Connan", 3, "Voldo", 7]
    print(listT, len(listT), listT.count("Voldo"), listT.extend("Aquilonia"))
    print(listT)
    listT.remove('a')
    print(listT)

lists()
print("Runing time: ", time.time()-start_time)
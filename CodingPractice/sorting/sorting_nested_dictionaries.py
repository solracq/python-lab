'''
@author: Solrac
'''


def sort_dict_by_name():
    for key, value in sorted(dictionary.items(), key=lambda x: x[1]["name"]):
        print("{} : {}".format(key, value))

def sort_dict_by_date():
    for key, value in sorted(dictionary.items(), key=lambda x: x[1]["date"]):
        print("{} : {}".format(key, value))
        
def sort_dict_by_downloads():
    for key, value in sorted(dictionary.items(), key=lambda x: x[1]['downloads']):
        print("{} : {}".format(key, value))
        
def sort_dict_by_downloads_otherformat():
    for key, value in sorted(dictionary.items(), key=lambda x: x[1]['downloads']):
        print("{}:".format(key))
        for v in value.values():
            print("{}".format(v), end=',')
        print()

dictionary = {
              'KEY1':{'name':'google','date':20101211,'downloads':0},
              'KEY2':{'name':'chrome','date':20200306,'downloads':100},
              'KEY3':{'name':'python','date':20091120,'downloads':50}
              }
print(f"Dictionary : {dictionary}")
print()
sort_dict_by_name()
print()
sort_dict_by_date()
print()
sort_dict_by_downloads()
print()
sort_dict_by_downloads_otherformat()
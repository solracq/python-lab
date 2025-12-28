'''
@author: Solrac
'''
def word_order(list_):
    duplicate = []
    occur = []
    diff_count = 0
    
    for i in range(len(list_)):
        ocurrences = 1
        if list_[i] in duplicate:
            continue
        for j in range(i+1, len(list_)):
            if list_[j] in duplicate:
                continue
            if list_[i] == list_[j]:
                duplicate.append(list_[i])
                ocurrences += 1
            else:
                diff_count += 1
        occur.append(ocurrences)
            
    print(f"diff count = {diff_count}")
    for i in occur:
        print(i," ", end="")
    
list_ = ['bcdef', 'abcdefg', 'bcde', 'bcdef']
print(list)
word_order(list_)

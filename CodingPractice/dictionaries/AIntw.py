'''
@author: Solrac
'''
# test_ids = ['cat', 'dog', 'log']
# generated_tests = [{'test_id': 'dogz', 'number': 12}, {'test_id': 'log', 'number':15}]
# output = [{'test_id' : 'log', 'number' : 15}]

def test_validation(test_ids, generated_tests):
    for dict_ in generated_tests:
        for i in range(len(dict_)):
            if dict_['test_id'] not in test_ids:
                print("wrong test name : {}".format(dict_['test_id']))
                break
            else:
                #print("test_id : {}".format(dict_['test_id']))
                #print("number : {}".format(dict_['number']))
                print(dict_)
                break

def answer(generated_tests, test_ids):
    for dict_ in generated_tests:
        if dict_['test_id'] not in test_ids:
            print(dict_['test_id'],"not found!")
        else:
            print(dict_)


def short_answer(generated_tests, test_ids):
    print([dict_ for dict_ in generated_tests if dict_['test_id'] in test_ids])
          

def printdict(generated_tests):
    for dict_items in generated_tests:
        for key, value in dict_items.items():
            print("{} : {}".format(getKey(dict_items, value),getValue(dict_items, key)))
            

def getKey(dict_, value):
    for key_, value_ in dict_.items():
        if value == value_:
            return key_
    return "key doesn't exist"

def getValue(dict_, key):
    for key_, value_ in dict_.items():
        if key == key_:
            return value_
    return "value doesn't exist"
    
test_ids = ['cat', 'dog', 'log']
generated_tests = [{'test_id': 'dogz', 'number': 12}, {'test_id': 'log', 'number':15}]

test_validation(test_ids, generated_tests)
print()
#printdict(generated_tests)
#answer(generated_tests, test_ids)
short_answer(generated_tests, test_ids)
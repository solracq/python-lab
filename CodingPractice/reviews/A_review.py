'''
@author: Solrac
'''
import random
import itertools
import sys
import json
import math
import requests


def find_goodtest(gen_tests: list, test_ids: list) -> dict:
    if test_ids != [] and gen_tests != []:
        for gen_test in gen_tests:
            if gen_test['test_id'] in test_ids:
                return gen_test
        return "Test id not present"
    else:
        return f"{gen_tests} or {test_ids} lists are empty"


test_ids = ['cat', 'dog', 'log']
generated_tests = [{'test_id': 'dogz', 'number': 12}, {'test_id': 'log', 'number': 15}]
print(find_goodtest(generated_tests, test_ids))


def rotate_string(string: str, direction: list, n: int) -> str:
    if direction == 'l' or direction == "L" or direction == "left":
        return string[n:] + string[:n]
    elif direction == 'r' or direction == "R" or direction == "right":
        return string[-n:] + string[:-n]
    else:
        return "Not accepted input"


string = "chonchita"
print(f"Rotating '{string}' to the left: {rotate_string(string, 'l', 3)}")
print(f"Rotating '{string}' to the right: {rotate_string(string, 'r', 3)}")


def gen_random_matrix(n: int) -> list:
    return [[random.randint(1, 99) for i in range(n)] for j in range(n)]


print(gen_random_matrix(3))


def print_matrix(matrix: list):
    for i in range(len(matrix)):
        print()
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
    print()


matrix = gen_random_matrix(5)
print_matrix(matrix)


def spiral_matrix(matrix: list) -> list:
    sphiral = []
    for i in range(len(matrix)):
        if i % 2 != 0:
            for j in range(len(matrix[i]) - 1, -1, -1):
                sphiral.append(matrix[i][j])
        else:
            for j in range(len(matrix[i])):
                sphiral.append(matrix[i][j])
    return sphiral


def spiral_matrix_simp(matris: list) -> list:
    sphiral = []
    for i in range(len(matrix)):
        if i % 2 == 0:
            sphiral.append(matrix[i])
        else:
            sphiral.append(matrix[i][::-1])
    return sphiral


print(f"sphiral_matrix = {spiral_matrix(matrix)}")
print(f"sphiral_matrix_simp = {spiral_matrix_simp(matrix)}")


def permutate(array: list) -> list:
    permutation = []
    for i in range(1, len(array) + 1):
        permutation += list(itertools.permutations(array, i))
    return permutation

def permutation2(array: list):
    res = []
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] == array[j]:
                res.append(array[i])
                continue
            res.append(array[i]+array[j])
    return res

array = ['a', 'b', 'c', 'd', 'e']
print(f"permutate '{array}': \n{permutate(array)}")


def subsets(string: list):
    letters = []
    groups = []
    for key, group in itertools.groupby(string):
        letters += key
        groups += list(group)
    return letters, groups

def compress_improved(s: str):
    prev = s[0]
    res = ""
    count = 0
    for i in range(len(s)):
        if s[i] == prev:
            count += 1
            prev = s[i]
        else:
            res += str(count) + prev
            count = 1
            prev = s[i]
    res += str(count) + prev

    return res


string = "aabbbccccc"
print(string)
key, group = subsets(string)
print(f"Repetitive keys in '{string}'are \n{key} and {group}")


def look_for_sbstr(string: str, sbstr: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == sub_string[0]:
            if string[i:i + len(sbstr)] == sbstr:  # string[4,9]
                count += 1
    return count


string = "TestCaseTestCase"
sub_string = "CaseT"
print(f"The number of times '{sub_string}' is contained in '{string}' is: {look_for_sbstr(string, sub_string)}")


def parenthesis_validation(s: str) -> str:
    p = list(s)
    op = ['{', '[', '(']
    cp = ['}', ']', ')']
    stack = []
    for i in range(len(p)):
        if p[i] in op:
            stack.append(p[i])
        elif p[i] in cp:
            location = cp.index(p[i])
            if len(stack) != 0 and op[location] == stack[len(stack) - 1]:
                stack.pop()
            else:
                return "UNBALANCED"
    if len(stack) == 0:
        return "BALANCED"


s = "{[()[]{}]}"
print(f"Is '{s}' balanced? {parenthesis_validation(s)}\n")


def reverse_string_chunk(s: str, chunk: int) -> str:
    array = []
    for i in range(0, len(s), chunk):
        array.append(s[i:i + chunk][::-1])
    return "".join(array)


s = "abcdefghijkl"
chunk = 3
print(f"Reversing '{s}' in chunks of {chunk} is: {reverse_string_chunk(s, chunk)}\n")


def linear_search(array: list, k: int) -> int:
    for item in array:
        if item == k:
            return array.index(item)
    return -1


arr = [34, 56, 2, 10, 77, 51, 93, 30, 5, 52]
k = 77
print(f"Find {k} in {arr} = {linear_search(arr, k)}\n")


def binary_search(array: list, k: int) -> int:
    s_array = sorted(array)
    s = 0
    e = len(array) - 1
    m = (s + e) // 2
    found = -1
    while s < e or found == -1:
        if k == s_array[m]:
            found = m
        elif k < s_array[m]:
            e = m - 1
        elif k > s_array[m]:
            s = m + 1
        m = (s + e) // 2
    return found


k = 34
arr = [34, 67, 89, 12, 21, 45, 88, 56, 73, 11, 48, 67, 5, 30, 32]
print(arr)
print(sorted(arr))
print(f"Binary Search: {k} is located in {binary_search(arr, k)}\n")


def find_min(array: list) -> int:
    min = 0
    for i in range(len(array) - 1):
        if array[min] > array[i + 1]:
            min = i + 1
    return array[min]


arr = [34, 67, 89, 12, 21, 45, 88, 56, 73, 11, 48, 67, 5, 30, 32]
print(f"The minimum number in {arr} is {find_min(arr)}\n")


def find_max(array: list) -> int:
    max = 0
    for i in range(len(array) - 1):
        if array[max] < array[i + 1]:
            max = i + 1
    return array[max]


arr = [34, 67, 89, 12, 21, 45, 88, 56, 73, 11, 48, 67, 5, 30, 32]
print(f"The maximum number in {arr} is {find_max(arr)}\n")


def sorting_asc(array: list):
    for i in range(len(array)):
        min = i
        for j in range(i + 1, len(array)):
            if array[min] > array[j]:
                tmp = array[j]
                array[j] = array[min]
                array[min] = tmp


arr = [34, 67, 89, 12, 21, 45, 88, 56, 73, 11, 48, 67, 5, 30, 32]
print(f"Original array: {arr}")
sorting_asc(arr)
print(f"Sorted array asc: {arr}\n")


def sorting_desc(array: list):
    for i in range(len(array)):
        max = i
        for j in range(i + 1, len(array)):
            if array[max] < array[j]:
                tmp = array[j]
                array[j] = array[max]
                array[max] = tmp


arr = [34, 67, 89, 12, 21, 45, 88, 56, 73, 11, 48, 67, 5, 30, 32]
print(f"Original array: {arr}")
sorting_desc(arr)
print(f"Sorted array desc: {arr}\n")


def find_sum_two_num(array: list, x: int):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == x:
                return (i, j)


arr = [50, 20, 10, 80, 75, 35]
x = 70
print(arr)
print(sorted(arr))
print(find_sum_two_num(arr, x))


def two_point_approach(array: list, k: int):
    array = sorted(array)
    s = 0
    e = len(array) - 1
    while s <= e:
        if array[s] + array[e] == k:
            return (array[s], array[e])
        elif array[s] + array[e] < k:
            s += 1
        elif array[s] + array[e] > k:
            e -= 1
    return -1


x = 70
arr = [50, 20, 10, 80, 75, 35]
arr.sort()
print(arr)
print(f"The sum {x} of two nums using Two Point Approach: {two_point_approach(arr, x)}\n")


def closest_sum_zero_bf(array: list, x: int):
    diff = sys.maxsize
    dictionary = {}
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            dictionary[(i, j)] = abs((array[i] + array[j]) - x)
    for key, value in sorted(dictionary.items(), key=lambda x: x[1]):
        return (key)

def closest_sum_zero_bf_2(array: list, x: int):
    dictionary = {}
    for i in range(len(array)):
        for j in range(len(array)):
            if i == j:
                continue
            result = array[i] + array[j] - x
            dictionary[abs(result)] = (array[i], array[j], x)
    for key, value in sorted(dictionary.items()):
        return(value)

nums = [1, 3, 4, 7, 10]
x = 15
print(f"The closest sum zero BF in {nums} and {x} is: {closest_sum_zero_bf(nums, x)}\n")
arr = [-1, 3, 2, -5, 4]
x = 0
print(f"The closest sum zero BF in {arr} and {x} is: {closest_sum_zero_bf(arr, x)}\n")


def closest_sum_zero(array: list, x: int):
    diff = sys.maxsize
    s = 0
    e = len(array) - 1
    res_s = 0
    res_e = 0
    while s < e:
        if abs(arr[s] + arr[e] - x) < diff:
            res_s = s
            res_e = e
            diff = abs(arr[s] + arr[e] - x)
        elif arr[s] + arr[e] < x:
            s += 1
        elif arr[s] + arr[e] > x:
            e += 1
    return (res_s, res_e)


nums = [1, 3, 4, 7, 10]
x = 15
print(f"The closest sum zero in {nums} and {x} is: {closest_sum_zero_bf(nums, x)}\n")
arr = [-1, 3, 2, -5, 4]
x = 0
print(f"The closest sum zero in {arr} and {x} is: {closest_sum_zero_bf(arr, x)}\n")


def three_sum_zero(array: list) -> tuple:
    array = sorted(array)
    for i in range(0, len(array) - 1):
        s = i + 1
        e = len(array) - 1
        while s < e:
            if array[s] + array[e] + array[i] == 0:
                return (i, s, e)
            elif array[s] + array[e] + array[i] < 0:
                s += 1
            else:
                e -= 1
    return -1


def three_sum_zero_bf(array: list) -> tuple:
    for i in range(0, len(array) - 2):
        for j in range(i + 1, len(array) - 1):
            for k in range(j + 1, len(array)):
                if array[i] + array[j] + array[k] == 0:
                    return (i, j, k)


arr = [-1, 0, 1, 2, -1, -4]
print(arr)
print(sorted(arr))
print(f"3sumzero bf found : {three_sum_zero_bf(arr)}")
print(f"3sumzero found : {three_sum_zero(arr)}")


def four_sum_zero(array: list) -> tuple:
    array = sorted(array)
    for i in range(0, len(array) - 2):
        for j in range(i + 1, len(array) - 1):
            s = j + 1
            e = len(array) - 1
            while s < e:
                if array[s] + array[e] + array[i] + array[j] == 0:
                    return (i, j, s, e)
                elif array[s] + array[e] + array[i] + array[j] < 0:
                    s += 1
                else:
                    e -= 1
    return -1


arr = [-1, 0, 1, 2, -1, -4, 1]
print(arr)
print(sorted(arr))
print(f"4sumzero found : {four_sum_zero(arr)}")


def compression(s):
    res = ""
    for key, group in itertools.groupby(s):
        g = len(list(group))
        res += str(g)
        res += key
    return res


# Execution
s = "AAAABBBCCCCCC"
print(f"Compressing {s} = {compression(s)}\n")


def compression_altr(s):
    keys = sorted(set(s))
    sorted_s = sorted(s)
    res = ""
    for key in keys:
        i = 0
        while key in sorted_s:
            if sorted_s[0] == key:
                i += 1
                sorted_s.remove(key)
        res += str(i)
        res += key
    return res


s = "AAAABBBCCCCCC"
print(f"Compressing alternative {s} = {compression_altr(s)}\n")


def get_file_content(file_path: str):
    with open(file_path, 'r') as file_in:
        buffer = file_in.readlines()
        for line in buffer:
            if "Hola!" in line:
                print("String already exists in file")
                return 0
    with open(file_path, 'w') as file_out:
        for line in buffer:
            if "TESTARROSA" in line:
                line = line + "Hola!\n"
            file_out.write(line)


file_path = "../file_data_manipulation/table.txt"
get_file_content(file_path)


def store_list_file_json(jsonfile: str, array: list):
    with open(jsonfile, 'r') as file_in:
        buffer = file_in.readlines()
        for line in buffer:
            if '["a", "b", "c", "d"]' in line:
                print(f"{array} already exists in json file")
                return 0
    with open(jsonfile, 'a') as file_obj:
        json.dump(array, file_obj)


def get_contents_from_json(jsonfile: str):
    with open(jsonfile, 'r') as file_obj:
        content = json.load(file_obj)
    return content


json_path = "/Learning/json_management/numbers.json"
array = ["a", "b", "c", "d"]
store_list_file_json(json_path, array)
print(get_file_content(json_path))


def convert_from_json_to_string(json_string):
    data = json.loads(json_string)
    return data


json_string = '{"name": "John", "age": 30, "city": "New York"}'
print(convert_from_json_to_string(json_string))


def manipulate_json(s):
    dictionary = {s[i]: s.count(s[i]) for i in range(len(s))}
    json_data = json.dumps(dictionary, indent=4, sort_keys=True)
    print(f"json data = {json_data}")
    str_data = json.loads(json_data)
    print(f"str data = {str_data}")


s = "Testing is very dupper fun"
manipulate_json(s)


def find_duplicates(array: list) -> list:
    duplicates = []
    for item in array:
        if item in duplicates:
            continue
        if array.count(item) >= 2:
            duplicates.append(item)
    return duplicates


arrs = [1, 3, 2, 6, 7, 8, 8, 5, 4, 2, 1, 5, 4, 6, 9]
print(f"List with duplicates: {arrs}")
print(f"Found duplicates: {find_duplicates(arrs)}\n")


def find_uniques(array: list) -> list:
    unique = []
    for item in array:
        if item in unique:
            continue
        if array.count(item) == 1:
            unique.append(item)
    return unique


arrs = [1, 3, 2, 6, 7, 8, 8, 5, 4, 2, 1, 5, 4, 6, 9]
print(f"List with uniques: {arrs}")
print(f"Found unique items: {find_uniques(arrs)}\n")


def find_first_nonduplicate(s) -> str:
    for character in s:
        if s.count(character) == 1:
            return character


s = "google"
print(f"first non-duplicate in '{s}' is: {find_first_nonduplicate(s)}")


def compression_it(s: str) -> str:
    resp = ""
    for key, group in itertools.groupby(s):
        g = str(len(list(group)))
        resp += g
        resp += key
    return resp


s = "AAAABBBCCCCCCDEEFFFFFGAA"
print(f"Compressing {s} = {compression_it(s)}\n")


def compression_ml(s: str) -> str:
    resp = ""
    dup = []
    slist = list(s)
    for i in range(len(s)):
        ch = slist.pop()
        if slist == [] and dup != []:
            dup.append(ch)
            resp += ch
            resp += str(len(dup))
        elif ch != slist[len(slist) - 1] and dup == []:
            resp += ch
            resp += str(1)
        elif ch != slist[len(slist) - 1] and dup != []:
            dup.append(ch)
            resp += ch
            resp += str(len(dup))
            dup = []
        elif ch == slist[len(slist) - 1]:
            dup.append(ch)
    return resp[::-1]


s = "AAAABBBCCCCCCDEEFFFFFGAA"
print(f"Compressing My logic {s} = {compression_ml(s)}\n")


def multiply_except_itself(arr: list) -> list:
    res = []
    for i in range(len(arr)):
        mult = 1
        for j in range(0, len(arr)):
            if arr[j] == arr[i]:
                continue
            else:
                mult *= arr[j]
        res.append(mult)
    return res


arr = [-10, 5, 2, 8]
# output = [5*2*8, -10*2*8, -10*5*8, -10*5*2] -> [80, -160, -400, -100]
print(arr)
print(f"Multiply all items in '{arr}' except itself: {multiply_except_itself(arr)}")


def find_first_second_maxs(array: list) -> tuple:
    for i in range(len(array)):
        max = i
        for j in range(len(array)):
            if array[max] < array[j]:
                temp = array[j]
                array[j] = array[max]
                array[max] = temp
    res = (array[0], array[1])
    print(res)


arr = [5, 17, 19, 23, 34, 45, 52, 53, 58, 62, 65, 77, 88, 90, 65, 5]
print(arr)
find_first_second_maxs(arr)


def find_max_sum(arr: list) -> int:
    res = []
    sum = 0
    for i in range(2, len(array) + 1):
        permutations = list(itertools.permutations(arr, i))
        for items in permutations:
            for num in items:
                sum += num
            res.append(sum)
            sum = 0
    return max(res)

def find_max_sum_improved(arr):
    permutation = []
    res = []
    for i in range(1, len(arr) + 1):
        permutation += itertools.permutations(arr, i)
        for item in permutation:
            if len(item) >= 2:
                res.append(sum(item))
    return max(res)


arr = [-1, -2, -3, -4]
print(arr)
print("Maximum sum (between two and more numbers in the list) from list above: ", find_max_sum(arr))  # -3


def remove_vowels(s: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']
    s_list = list(s)
    for vowel in vowels:
        if vowel in s_list:
            s_list.remove(vowel)
    return "".join(s_list)


s = "abc"
print(s)
print(remove_vowels(s))


def urlify(s: str) -> s:
    return s.strip().replace(" ", "%")


s = "  Mr. John Smith "
print(s)
print(urlify(s))


def sort_min(array: list):
    for i in range(len(array)):
        min = i
        for j in range(i + 1, len(array)):
            if array[min] > array[j]:
                array[min], array[j] = array[j], array[min]


array = [5, 17, 19, 23, 34, 45, 52, 53, 58, 62, 65, 77, 88, 90, 65, 5]
print(array)
sort_min(array)
print(array)


def sort_occurrences(array: list):
    dictionary = {}
    array_keys = sorted(set(array))
    ocurrences = []
    for key in array_keys:
        dictionary[key] = array.count(key)
    for k, v in sorted(dictionary.items(), key=lambda x: x[1]):
        if v > 1:
            for i in range(v):
                ocurrences.append(k)
        else:
            ocurrences.append(k)
    return ocurrences


def sort_ocurrences_alt(array: list):
    for i in range(len(array)):
        min = i
        for j in range(i + 1, len(array)):
            if array.count(array[min]) > array.count(array[j]):
                array[min], array[j] = array[j], array[min]

def sort_occurrences_alternative(arr: list):
    arr.sort()
    one_freq = []
    res = []
    for i in range(len(arr)):
        min_fq = arr.count(arr[i])
        for j in range(i+1, len(arr)):
            if arr.count(arr[j]) < min_fq:
                arr[i], arr[j] = arr[j], arr[i]
    for item in arr:
        if arr.count(item) == 1:
            one_freq.append(item)
        else:
            res.append(item)
    one_freq.sort()
    arr.clear()
    arr += one_freq
    arr += res

arr = [3, 1, 2, 2, 4, 5, 1, 1]
print(f"Not sorted arr = {arr}")
sort_min(arr)
print(f"Sorted by value= {arr}")
arr = [3, 1, 2, 2, 4, 5, 1, 1]
print(f"SORT OCCURRENCES: {sort_occurrences(arr)}")
sort_ocurrences_alt(arr)
print(f"SORT OCURRENCES ALTERNATIVE: {arr}")


def sum_matrix(matrix: list) -> int:
    sum = 0
    for i in range(len(matrix)):
        for item in matrix[i]:
            sum += item
    return sum


matrix = [[3, 2, 5], [8, 7, 1], [9, 3, 4]]
total = sum_matrix(matrix)
print(total)
matrix = [[random.randint(1, 99) for i in range(5)] for j in range(5)]
print(matrix)
print(f"Total sum = {sum_matrix(matrix)}")


def find_diff_btw_nums(arr):
    res = []
    for i in range(len(arr) - 1):
        res.append(abs(arr[i] - arr[i + 1]))
    return res


arr = [3, 4, 5, 2, 1]  # -> [1, 1, 3, 1]
print("FIND DIFFERENCE BTW NUMBERS")
print(arr)
print(find_diff_btw_nums(arr))


def find_min_btw_num(arr: list) -> list:
    min = []
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            min.append(arr[i])
        else:
            min.append(arr[i + 1])
    return min


arr = [3, 4, 5, 2, 1]
print("FIND MINIMUM BTW NUMBERS")
print(arr)
print(find_min_btw_num(arr))


def is_palindrome(x: int) -> bool:
    if str(x) == str(x)[::-1]:
        return True


x = 12521
# Lenght of an integer
print(round(math.log10(x) + 1))
print(x)
print(is_palindrome(x))


def making_anagrams(a, b):
    common_a = ""
    common_b = ""
    for i in range(len(a)):
        if a[i] in common_a:
            continue
        if a[i] in b:
            common_a += a[i]
    for j in range(len(b)):
        if b[j] in common_b:
            continue
        if b[j] in common_a:
            common_b += b[j]
    return (common_a, common_b)


a = "fcrxzwscanmligyxyvym"
b = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"
print("MAKING ANAGRAM")
print(making_anagrams(a, b))


def wrap(string: str, max_width: int):
    chopped = []
    for i in range(0, len(string), max_width):
        chopped.append(string[i:i + max_width])
    resp = "\n".join(chopped)
    return resp


string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
max_width = 4
print(string)
print(wrap(string, max_width))


def lengthOfLongestSubstring(s):
    sub_strings = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
    print(sub_strings)
    res = []
    dup = []
    for sub_string in sub_strings:
        if sub_string in dup:
            continue
        if sub_strings.count(sub_string) >= 2:
            dup.append(sub_string)
        res.append(sub_string)
    return len(res)


s = "poder total"
print(s)
print('longest substring:', lengthOfLongestSubstring(s))


def find_phone_address(s: str, dictionary: dict):
    return dictionary[s]


print("find phone address")
dict_ = {'sam': '99912222', 'tom': '11122222', 'harry': '12299933'}
s = "harry"
print(find_phone_address(s, dict_))


def separate_nums(num: int):
    s_num = str(num)
    resp = []
    for item in s_num:
        resp.append(int(item))
    return resp


def separate_nums_mth(num: int):
    res = []
    for i in range(round(math.log10(num) + 1)):
        if i == 0:
            div = num // 10
            mod = num % 10
        else:
            mod = div % 10
            div = div // 10
        res.append(mod)
    return res[::-1]

def separate_nums_improved(num):
    num_lenght = math.trunc(math.log10(num) + 1)
    res = []
    for i in range(num_lenght):
        if math.trunc(math.log10(num) + 1) == 1:
            res.append(num)

        residual = num % 10
        res.append(residual)
        num = math.trunc(num / 10)
    res_ordered = []
    for i in range(num_lenght-1, -1, -1):
        res_ordered.append(res[i])
    return res_ordered


num = 12345
print("Numbers", num)
print("Separate numbers", separate_nums(num))
print("Separate numbers by math", separate_nums_mth(num))


def minwindowsubs(string: str, sub_string: str) -> str:
    list_substr = list(sub_string)
    res = []
    indexes = []
    sbs_res = []
    # Obtain list of indexes that enclose the found sub-strings range in strings
    for i in range(len(string)):
        if string[i] in list_substr and list_substr != []:
            indexes.append(i)
            list_substr.remove(string[i])
            if list_substr == []:
                list_substr = list(sub_string)
                res.append(indexes)
                indexes = []
    # Obtain the actual strings corresponding to the indexes
    for item in res:
        s = item[0]
        e = item[len(item) - 1] + 1
        sbs_res.append(string[s:e])
    # Order elements based on their length
    for i in range(len(sbs_res) - 1):
        min = i
        for j in range(i + 1, len(sbs_res)):
            if len(sbs_res[min]) > len(sbs_res[j]):
                sbs_res[min], sbs_res[j] = sbs_res[j], sbs_res[min]
    return sbs_res[0]

def minwindowsubs_improved(string: str, sub_string: str) -> str:
    sub_string_list = list(sub_string)
    res = []
    for i in range(len(string)-1):
        if string[i] in sub_string_list:
            sub_string_list.remove(string[i])
            for j in range(i+1, len(string)):
                if string[j] in sub_string_list:
                    sub_string_list.remove(string[j])
                if sub_string_list == []:
                    res.append(string[i:j+1])
                    sub_string_list = list(sub_string)
                    break
    for i in range(len(res)):
        min = i
        for j in range(i+1, len(res)):
            if len(res[j]) < len(res[min]):
                res[min], res[j] = res[j], res[min]
    return res[0]


string = "ADOBECODEBANC"
#         -  - -   -- -
sub_string = "ABC"
print("MINIMUM WINDOW")
print(f"String: {string}")
print(f"Sub-string: {sub_string}")
print(minwindowsubs(string, sub_string))  # -> BANC


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = 30
print(f"Fibonacci for {n} = {fibonacci(n)}")


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


n = 5
print(f"Factorial for {n} = {factorial(n)}")


def prime(n):
    for i in range(2, n + 2):
        if i == 2:
            print(i, end=" ")
        for j in range(2, i):
            if i % j == 0:
                break
            else:
                print(i, end=" ")
                break


n = 30
print(f"\nPrime until {n} = {prime(n)}\n")


def approximate_sum_two_lists(arr1, arr2, x):
    diff = sys.maxsize
    s = 0
    e = len(arr2) - 1
    res_s = 0
    res_e = 0
    while s < len(arr1) and e >= 0:
        if abs(arr1[s] + arr2[e] - x) < diff:
            res_s = s
            res_e = e
            diff = abs(arr1[s] + arr2[e] - x)
        elif arr1[s] + arr2[e] < x:
            s += 1
        else:
            e -= 1
    return (res_s, res_e)


print("APPROXIMATE SUM TWO LISTS")
arr1 = [1, 4, 5, 7]
arr2 = [10, 20, 30, 40]
x = 38
print(approximate_sum_two_lists(arr1, arr2, x))


def closest_num(arr, k):
    dictionary = {}
    for num in arr:
        dictionary[abs(num - k)] = num
    #     dictionary[num] = abs(num-k)
    # for k, v in sorted(dictionary.items(), key=lambda x: x[1]):
    #     return k
    return dictionary[min(dictionary.keys())]


arr = [9, 11, 5, 3, 25, 18]
k = 6
# output : 5
print(f"The closest element in the list {arr} for {k} is: {closest_num(arr, k)}")


def longest_prefix1(lista):
    sc = list(min(lista))
    res = []
    count = len(lista)
    for i in range(len(sc)):
        for item in lista:
            if item == sc:
                continue
            if item.startswith(sc[i], i) and count > 0:
                count -= 1
                if count == 0:
                    res.append(sc[i])
                    count = len(lista)
            else:
                return "".join(res)

def longest_prefix2(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if len(arr[j]) < len(arr[min]):
                arr[j], arr[min] = arr[min], arr[j]
    base = arr[0]
    res = []
    for i in range(len(arr)):
        if base == arr[i]:
            continue
        for j in range(len(base)):
            if arr[i][j] == base[j]:
                if base[j] not in res:
                    res.append(base[j])
            else:
                break
    return "".join(res)

lista = ['flower', 'flowless', 'flat']
print(lista)
print(longest_prefix1(lista))


def find_majority_num(nums):
    keys = list(set(nums))
    dictionary = {}
    for key in keys:
        dictionary[nums.count(key)] = key
    return dictionary[max(dictionary.keys())]


nums = [2, 2, 1, 1, 1, 2, 2]
print(nums)
print(find_majority_num(nums))


def largest_consecutive_sum(arr):
    sums = []
    permutations = [arr[i:j] for i in range(len(arr)) for j in range(i + 1, len(arr) + 1)]
    for item in permutations:
        sums.append(sum(item))
    return max(sums)


print("LARGEST CONSECUTIVE SUM")
arr = [1]
print(largest_consecutive_sum(arr))
arr = [-2, 1]
print(largest_consecutive_sum(arr))
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(largest_consecutive_sum(arr))


def merger(arr1: list, len_arr1: int, arr2: list, len_arr2: int):
    count = 0
    for i in range(len(arr1)):
        if arr1[i] == 0 and count < len_arr2:
            arr1[i] = arr2[count]
            count += 1
    return arr1


print("MERGER")
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [4, 5, 6]
print(merger(nums1, len(nums1), nums2, len(nums2)))


def is_anagram_list(arr):
    count = 0
    for i in range(1, len(arr)):
        if sorted(arr[0]) == sorted(arr[i]):
            count += 1
    if count == len(arr) - 1:
        return True
    return False


arr = ['ice', 'eci', 'cei']
print(f"Are the elements in {arr} anagrams? {is_anagram_list(arr)}")


def pascals_triangle_failed_attempt(n):
    res = []
    for i in range(n):
        if i == 0:
            res.append([1])
        elif i == 1:
            res.append([1, 1])
        elif i > 1:
            array = res[len(res) - 1]
            print(f"\nI = {i}")
            print(f"current array = {array}")
            for j in range(0, len(array), 2):
                # result = sum(array[j:j+2])
                # print(f"result = {result}")
                # array.insert(i-1, result)
                array.append(sum(res[i - 1][j:j + 2]))
                print(f"new array = {array}")
                res.append(array)

    return res


def pascals_triangle(n):
    res = []
    for i in range(n):
        arr = []
        for j in range(0, i + 1):
            if j == 0:
                arr.append(1)
            elif j == i:
                arr.append(1)
            else:
                for k in range(0, 1):
                    arr.append(sum(res[i - 1][k:k + 2]))
        res.append(arr)
    return res


# output: [[1],[1,1],[1,2,1], [1,3,3,1], [1,4,6,4,1]]
n = 5
print(pascals_triangle(n))


#######################################################

def access_jsonFile(jsonFile):
    with open(jsonFile, 'r') as json_obj:
        json_dict = json.load(json_obj)
    for key, value in json_dict.items():
        if type(value) == list:
            print(f"{key}: ")
            for item in value:
                print(f"\t{item}")
        else:
            print(f"{key}: {value}")


jsonFile = 'config.json'
access_jsonFile(jsonFile)

try:
    5 / 0
except ZeroDivisionError:
    print("nono!")

try:
    3 / 0
except:
    with open("../error_handling/error_file.txt", "w") as err_obj:
        err_obj.write("Zero Dvision Issue!")
    print("Errorlogs can be found at error_file.txt")


def dec_bin(num):
    if num == 0:
        return ""
    else:
        return dec_bin(num // 2) + str(num % 2)


num = 5
print(dec_bin(num))


def bin_dec(bnum):
    bnum = list(bnum)
    bnum.reverse()
    result = 0
    for i in range(len(bnum)):
        result += int(bnum[i]) * 2 ** i
    return result


bnum = "101"
print(bin_dec(bnum))


def combinations(s, n):
    return list(itertools.combinations(s, n))


s = "baca"
print(combinations(s, 2))


# **********************************************************************
def rotate_list(nums: list, k: int, direction: str):
    if direction == 'r':
        return nums[-k:] + nums[:-k]
    else:
        return nums[k:] + nums[:k]


k = 3
nums = [1, 2, 3, 4, 5, 6, 7]
print(nums)
print(rotate_list(nums, k, "r"))
print(rotate_list(nums, k, "l"))


def adding_plusone_to_listToDigit(nums):
    for i in range(len(nums)):
        if nums[i] == nums[len(nums) - 1]:
            nums[i] += 1
    return nums


nums = [1, 2, 3]
print(nums)
print(adding_plusone_to_listToDigit(nums))


def parenthesis_validation(s):
    p = list(s)
    op = ["[", "{", "("]
    cp = ["]", "}", ")"]
    stack = []
    for i in range(len(s)):
        if p[i] in op:
            stack.append(p[i])
        elif p[i] in cp:
            location = cp.index(p[i])
            if len(stack) > 0 and op[location] == stack[len(stack) - 1]:
                stack.pop()
            else:
                return "UNBALANCED"
    if len(stack) == 0:
        return "BALANCED"


s = '[({})[()]{[()]}]'
print(s)
print(parenthesis_validation(s))


def spiral_matrix(matrix: list):
    res = []
    for i in range(len(matrix)):
        if i % 2 == 0:
            res += matrix[i]
        else:
            res += matrix[i][::-1]
    return res


n = 5
matrix = [[random.randint(1, 99) for i in range(n)] for j in range(n)]
print(matrix)
print(spiral_matrix(matrix))


def find4sum(nums, x):
    nums = sorted(nums)
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            s = j + 1
            e = len(nums) - 1
            while s < e:
                if nums[s] + nums[e] + nums[i] + nums[j] == x:
                    return (i, j, s, e)
                elif nums[s] + nums[e] + nums[i] + nums[j] < x:
                    s += 1
                else:
                    e -= 1
    return -1


nums = [1, 4, 45, 6, 10, 12]
x = 21
print(nums)
nums.sort()
print(nums)
print(find4sum(nums, x))
print()


# Check Distances btw same letters

def first_letter_twice(s):
    repeated = []
    dictionary = {}
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j] and s[j] not in repeated:
                repeated.append(s[i])
                dictionary[abs(i - j)] = s[j]

    return dictionary[min(dictionary.keys())]

def first_letter_twice_alternative(s):
    arr=s
    dictionary = {}
    dict1 = {}
    for i in range(len(arr) - 1):
        first_dup = arr[i]
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                dictionary[abs(j-i)] = arr[j]
                dict1[j] = arr[j]
    keys = sorted(list(dictionary.keys()))
    keys_dup_loc = sorted(list(dict1.keys()))
    # return dictionary[keys[0]]
    return dict1[keys_dup_loc[0]]

s = "abccbaacz"
s2 = "nwcn"
s4 = "qwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnm"
s5 = "regzueqr"
print(f"First repeated letter in {s} : {first_letter_twice(s)}")
print(f"First repeated letter in {s2} : {first_letter_twice(s2)}")
print(f"First repeated letter in {s4} : {first_letter_twice(s4)}")
print(f"First repeated letter in {s5} : {first_letter_twice(s5)}\n")


def decode_message(key: str, message: str) -> str:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    prc_keys = []
    dictionary = {}
    decoded = ""
    for i in range(len(key)):
        if key[i] not in prc_keys and key[i] != " ":
            prc_keys.append(key[i])
    for i in range(len(prc_keys)):
        dictionary[prc_keys[i]] = alphabet[i]
    for i in range(len(message)):
        if " " in message[i]:
            decoded += " "
        else:
            decoded += dictionary[message[i]]
    return decoded

def decode_message_alternative(key: str, message: str) -> str:
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    dictionary = {}
    deciphered = []
    # Remove ducplicates in key
    unique_key = []
    for item in key:
        if item == " ":
            continue
        if item not in unique_key:
            unique_key.append(item)

    # Create table
    for i in range(len(unique_key)):
        dictionary[unique_key[i]] = alph[i]

    # Decipher
    for i in range(len(message)):
        if message[i] == " ":
            deciphered.append(" ")
            continue
        deciphered.append(dictionary[message[i]])

    return "".join(deciphered)

key = "happy boy"
message = "phob"
print(f"Encoded message: {message} \nDecoded message: {decode_message(key, message)}")
key1 = "the quick brown fox jumps over the lazy dog"
message1 = "vkbs bs t suepuv"
print(f"Encoded message: {message1} \nDecoded message: {decode_message(key1, message1)}")
key2 = "eljuxhpwnyrdgtqkviszcfmabo"
message2 = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
print(f"Encoded message: {message2} \nDecoded message: {decode_message(key2, message2)}")


################################################################
def match_sum(arr1, result):
    for i in range(len(arr1) - 1):
        s = i + 1
        e = len(arr1) - 1
        while s < e:
            if arr1[s] + arr1[e] + arr[i] == result:
                return (i, s, e)
            elif array[s] + array[s] + arr[i] < result:
                s += 1
            else:
                e -= 1


array = [50, 10, 80, 20, 75, 35]
k = 75
print(sorted(array))

def enumerate_test(array):
    for e in enumerate(array, 10):
        print(*e)

colors = "red blue green yellow brown black".split()
print(colors)
enumerate_test(colors)

def enumerate_months(array):
    for num, month in enumerate(array, 1):
        print(f"{num} - {month}")

months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
print(months)
print(enumerate_months(months))

def list_fruits(array):
    return [fruit for fruit in array if fruit.startswith('a')]

fruits = ['watermelon', 'apple', 'mango', 'kiwi', 'apricot', 'lemon', 'guava']
print(list_fruits(fruits))

mygenerator = (2**i for i in range(0, 32))
print(list(mygenerator))

file = "/Learning/file_add_line.txt"
with open(file, 'r') as file_obj:
    for line in file_obj:
        print(line[:-1]) # to remove the extra blank line

frozen_set = frozenset({1, 2, 3, 4, 5})
print(frozen_set) # user cannot add or delete elements from the set

def fun(*kwargs):
    return kwargs

a = "blueberry"
b = "peach"
c ="cherry"
num = 7
print(fun(a, b, c, num, 10))

def fun2(a: str, b: int, *args: list):
    print(a)
    print(b)
    print(args)

a = "testarrosa"
b = "8"
c = [1, 2, 3, 4, 5]
d = {"a": 5, "b": 4, "c": 3}
fun2(a, b ,c, d)

def fun3(*kwargs: dict):
    """ Printing several arguments using *kwargs """
    print(kwargs)

e = {"d": 7, "e": 8, "f": 9}
fun3(d, e)
print(fun3.__doc__) # To print the content of the function description header.x
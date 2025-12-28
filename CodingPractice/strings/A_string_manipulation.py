'''
@author: Solrac
'''

#Splitting
def splitting_strings(text:str):
    if "January" in text:
        split_text = text.split(",")
    else:
        split_text = text.split()
    return split_text

#Joining
def joining_strings(text:str):
    if "January" in text:
        join_text = "/".join(text)
    else:
        join_text = " ".join(text)
    return join_text

#Capitalize
def capitalize_strings(text:str):
    return text.capitalize()

#Title
def title_strings(text:str):
    return text.title()

#Lower
def lower_string(text:str):
    return text.lower()

#Upper
def upper_string(text:str):
    return text.upper()

#Stripe
def striping_string(text:str):
    return text.strip()

#Find
def finding_string(text:str, to_find:str):
    if text.find(to_find):
        return True
    else:
        return False

#Strings Iteration
def find_letter_in_text(text:str, to_find:chr):
    found = []
    for i in range(len(text)):
        if text.startswith(to_find, i):
            found.append(i)
    return found

#Replace chars in strings
def replace_chars(text:str, original:chr, new:chr):
    if original not in text:
        print(f"The '{original}' char doesn't exist in '{text}'")
        exit
    array = list(text)
    for i in range(len(text)):
        if text.startswith(original, i):
            array[i] = new
    return "".join(array)

#Count chars in text
def count_chars(text:str, to_find:chr):
    count = 0
    for i in range(len(text)):
        if text.startswith(to_find, i):
            count += 1
    return count

def count_chars2(text:str, to_find:chr):
    count = 0
    for character in text:
        if character == to_find:
            count += 1
    if count != 0:
        return count
    else:
        return f"{to_find} couldn't be found in {text}"

#Reverse text
def reverse_text(text:str):
    array = list(text)
    reversed_array = []
    for i in range(len(array)-1, -1, -1):
        reversed_array.append(array[i])
    return "".join(reversed_array)

def reverse_text_simple(text:str):
    return text[::-1]

def reverse_array(array:list):
    string = "".join(array)
    new_string = string[::-1]
    return list(new_string)

#Finding palindrome e.g) "ana"
def is_palindrome(text:str):
    array = list(text)
    array_r = []
    for i in range(len(array) - 1, -1, -1):
        array_r.append(array[i])
    if array == array_r:
        return True
    else:
        return False

#finding anagram e.g) soil -> oils
def is_anagram(text1, text2):
    array1 = list(text1)
    array2 = list(text2)
    if sorted(array1) == sorted(array2):
        return True
    else:
        return False

#Remove vowels
def remove_vowels(text):
    array_vowels = ['a', 'e', 'i', 'o', 'u']
    array = list(text)
    new_array = []
    for character in text:
        if character not in array_vowels:
            # array.remove(character)
            new_array.append(character)
    return "".join(new_array)

#Reverse strings based on provided bulk
def reverse_bulk(text:str, bulk:int):
    r_text = ""
    for i in range(0, len(text), bulk):
        r_text += text[i:i+bulk][::-1]
    return r_text

#Rotate strings
def rotate_stringr(text, digits):
    return text[digits:] + text[:digits]

def rotate_stringl(text, digits):
    return text[-digits:] + text[:-digits]

#Substrings
def get_substrings(text:str):
    output = []
    for i in range(len(text)):
        for j in range(i+1, len(text)+1):
            output.append(text[i:j])
    return output

def get_substrings_splified(text:str):
    return [text[i:j] for i in range(len(text)) for j in range(i+1, len(text)+1)]

def find_subtext(text, subtext):
    count = 0
    for i in range(len(text)):
        if text.startswith(subtext[0], i):
            if text[i:i+len(subtext)] == subtext:
                count += 1
    return count

#Parenthesis balncing
def parenthesis_balancing(text):
    p = list(text)
    op = ["{", "[", "("]
    cp = ["}", "]", ")"]
    stack = []
    stackc = []
    for i in range(len(text)):
        if p[i] in op:
            stack.append(p[i])
        elif p[i] in cp:
            location = cp.index(p[i])
            stackc.append(p[i])
            if len(stack) > 0 and op[location] == stack[len(stack)-1]:
                stack.pop()
                stackc.pop()
            else:
                return 'UNBALANCED'
    if len(stack) == 0 and len(stackc) == 0:
        return 'BALANCED'

#FizzBuzz
def fizzbuz(num):
    for i in range(num):
        if i % 3 == 0 and i % 5 == 0 and i != 0:
            print("FizzBuzz")
        elif i % 3 == 0 and i != 0:
            print("Fizz")
        elif i % 5 == 0 and i != 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    text = "abc es muy bonita"
    # Split and Join
    split_text = splitting_strings(text)
    print(split_text)
    join_text = joining_strings(split_text)
    print(join_text)
    text_months = "January,February,March,April,May,June,July,August,September,October,November,December"
    split_text = splitting_strings(text_months)
    print(split_text)
    join_text = joining_strings(split_text)
    print(join_text)
    # Capitalize and Title strings
    text = "sdaf el guapo"
    print(capitalize_strings(text))
    print(title_strings(text))
    # Upper and lower strings
    print(lower_string(text))
    print(upper_string(text))
    # 'in' and 'not in' to find words in strings
    text = "conan the king warrior from aquilonia"
    print("Is 'conan' in message?", str("conan" in text))
    print("Is 'aquilonia' in message", str("aquilonia" in text))
    print("Is 'valerian' in message", "valerian" in text)
    # Strip string
    text = "     testarrosa    "
    print(text)
    print(striping_string(text))
    print(text.rstrip())
    print(text.lstrip())
    text = "-testarrosa-"
    print(text)
    print(text.strip("-"))
    print(text.rstrip("-"))
    print(text.lstrip("-"))
    # Find strings
    text = "abc es mia y solo mia"
    print("Is 'abc' in", text, "=", finding_string(text, "abc"))
    print(f"The first 'mia' in '{text}' is at {text.find('mia')}")
    print(f"The second 'mia' in '{text}' is at {text.rfind('mia')}")
    # Index
    text = "Ojos pispiretos del koko"
    print(text)
    print("first 'p' in text is located w/ index at ", text.index('p'))
    print("second/last 'p' in text is located w/ index at", text.rindex('p'))
    print("first 'p' in text is located w/ find at", text.find('p'))
    print("second/last 'p' in text is located w/ find at", text.rfind('p'))
    array = text.split()
    print(array)
    print("'pispiretos' is found in the array w/index at", array.index('pispiretos'))
    try:
        print("'pispiretos' is found in the array w/found at", array.found('pispiretos'))
    except AttributeError:
        print("The 'found()' method cannot be used w/ lists")
    # checks
    text = "test"
    print(text)
    print("is text alpha", text.isalpha())
    print("is text alnum", text.isalnum())
    print("is text numeric", text.isnumeric())
    print("is text starts with 'y'", text.startswith("y"))
    print("is text starts with 'a'", text.startswith("a"))
    print("is text ends with 'a'", text.endswith('a'))
    print("is text ends with 'y'", text.endswith('y'))
    print(text.endswith('u', 1, 2))
    # counts
    print("The number of 'y's in text", text.count('y'))
    print("The number of 'a's in text", text.count('a'))
    # String iterations and formating
    text = "Conan the barbarian"
    to_find = 'n'
    found = find_letter_in_text(text, to_find)
    print(text)
    print("The letter '{letter_to_find}' was found in '{text_to_search_from}' in the "
          "following locations: '{found_list}'".format(letter_to_find=to_find,
                                                       text_to_search_from=text,
                                                       found_list=found))
    # vars types
    print(f"'{text}' is of type = {type(text)} \n'{to_find}' is of type = {type(to_find)} "
          f"\n'{found}' is of type = {type(found)}")
    # Manually order lists w/ *list
    array = [1, 2, 3, 4, 5, 6]
    print(array)
    print("{5}, {4}, {3}, {2}, {1}, {0}".format(*array))
    print(*array)
    # Find and replace chars in text
    text = "Cad the barbarian "
    print(replace_chars(text, "n", "%"))
    print(replace_chars(text, "z", "%"))
    print(text.replace(" ", "%"))
    print("%".join(text))
    print(f"Counting the 'b' in {text}: {count_chars(text, 'b')}")
    print(f"Counting the 'b' in {text}: {count_chars2(text, 'b')}")
    print(f"Counting the 'x' in {text}: {count_chars2(text, 'x')}")
    # Other string manipulations
    print(text.swapcase())
    text = "My name is Ståle"
    print(text)
    print(f"'{text}' encoded is {text.encode(encoding='ascii', errors='ignore')}")
    # Reverse text
    text = "Moonlight Sonata"
    print(text)
    print("Reverse text:", reverse_text(text))
    print("Reverse text simple:", reverse_text_simple(text))
    # Finding anagram
    text = "ana"
    print(f"Is '{text}' a palindrome? = {is_palindrome(text)}")
    text = "madam"
    print(f"Is '{text}' a palindrome? = {is_palindrome(text)}")
    text1 = "soil"
    text2 = "oils"
    print(f"Is '{text1}' an anagram of {text2}? = {is_anagram(text1, text2)}")
    text1= "cinema"
    text2= "iceman"
    print(f"Is '{text1}' an anagram of {text2}? = {is_anagram(text1, text2)}")
    # Remove vowels
    text = "Moonlight Sonata"
    print(text)
    print(remove_vowels(text))
    array = ["1", "2", "3", "4", "5", "6"]
    print(array)
    print("reversed:", reverse_array(array))
    array = ["saint", "seyia"]
    print("reversed:", reverse_array(array))
    # Reverse string by bulks
    text = "abcdefghi"
    bulk = 3
    print(text)
    print(f"Reversed by bulk of {bulk}: {reverse_bulk(text, bulk)}")
    # Rotate strings
    digits = 2
    print(text)
    print("Rotate to the right: ", rotate_stringr(text, digits))
    print("Rotate to the left: ", rotate_stringl(text, digits))
    print([array[i] for i in range(len(array))])
    array = ["1", "2", "3", "4", "5", "6"]
    print([array[i+1] for i in range(len(array)-1)], end="")
    print()
    # Substrings
    text = "BANANA"
    print(text)
    print(get_substrings(text))
    print(get_substrings_splified(text))
    text = "TestCaseTestCase"
    subtext = "CaseT"
    print(f"Find '{subtext}' in '{text}': {find_subtext(text, subtext)} instances")
    # more on the replace
    text = "ababa"
    print(text.replace('a', 'A', 2))
    # Parenthesis balancing
    s = "{[()[]{}]}"
    print(s)
    print(parenthesis_balancing(s))
    s = "]{[()[]{}]}"
    print(s)
    print(parenthesis_balancing(s))
    # fizzbuzz
    fizzbuz(15)
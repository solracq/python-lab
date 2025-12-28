import re

r = re.compile(r"\d{2,}")  # match 2 or more digits
#     | |----> {m, } : at least m occurrences
#     |------> \d : any digit
file = "/CodingPractice/spam.txt"
with open(file, 'r') as SPAM:
    for line in SPAM:
        if r.search(line):
            print(line, end="")
print()

#########################################################################################
match = re.findall(r'[Gg]eeks', 'GeeksforGeeks: A computer science portal for geeks')
print(match)

#########################################################################################
r = re.compile(r"[Yy]ears")
with open(file, 'r') as file_obj:
    for line in file_obj:
        if r.search(line):
            print(line, end=" ")
print()

#########################################################################################
match = re.search(r'[\d]{2}-[\d]{2}-[\d]{4}', '24-12-2024')
print(match)


#########################################################################################
def search_string(string, k):
    fruits = string.split()

    r = re.compile(k)
    for fruit in fruits:
        if r.search(fruit):
            print(fruit, end=' ')
            print(r.search(fruit).group(), end=' ')
            print(r.search(fruit).start(), end=' ')
            print(r.search(fruit).end())
    print()


string = "apple banana artichoke cherry date enchilada appetizer"
k = r"c."
search_string(string, k)


#########################################################################################
def findall_string(string):
    r = re.compile(
        r'a([a-z]{3})(.)')  # find and print the next 3 characters after 'a' and also print the next character after the 3 chars
    print(r.findall(string))

    print("find object", "\t\t\t\tfind group", "\tfind start", "\tfind end", "\tfind group1")
    for m in r.finditer(string):
        print(m, m.group(), m.start(), m.end(), m.group(1))

findall_string(string)

#########################################################################################
string = "apple banana Artichoke cherry date enchilada APPETIZER"
match = re.findall(r'\ba.{3}', string,
                   re.IGNORECASE)  # find 'a' at  beginning or end of word and print 'a' plus the next three chars
print(match)
#########################################################################################

r = re.compile(r'([a-z])[,;:/](\d+)')
               #   |      |      |---> look for any digit and more
               #   |      |----------> sparated groups by , ; : /
               #   |-----------------> look for any letters
string = "a,123 b;456 c:989 f/134"
matches = r.findall(string)
print(matches)

for m in r.finditer(string):
    for gr_num in range(r.groups+1):
        print(f"{gr_num} {m.group(gr_num)}", end=" ")
    print()

#########################################################################################
# Replacing Text with sub() and subn()
string = "apple banana artichoke cherry date enchilada appetizer"
r = re.compile(r'\b(a[a-z]+)(\s*)') # match words that start with 'a' with any space(\s)
print(r.sub("", string)) # delete matched text (strings that start with 'a')
print(r.subn("XXX", string)) # replace matched text with 'XXX'

# Replace with a callback, replace found string/char with the output of a funciton
def replace_it(m):
    # group 1 is the 'a' word, group 2 is space after it
    return "'" + m.group(1) + "'" + m.group(2)

print(r.sub(replace_it, string)) # replace it with callback

#########################################################################################
# Splitting a string
# match anything BUT a letter, digit, underscore, or apostrophe
rx_wordsep = re.compile(r'[^\w]+') # NOT(^) find any word(\w) - for splitting lines into words
string = 'There are 10 kinds of people ina Binary world -- "Geek talk"'
words = rx_wordsep.split(string)
print(words)

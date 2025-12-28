'''
@author: Solrac
'''
# def

if __name__ == "__main__":
    months = (
        'January', 'February', "March", "April", "May", "June",
        "July", 'August', 'September', 'October', 'November', 'December'
    )
    print(months[8])
    print(list(months))
    print(months.count("August"))
    print(months.index("August"))
    baroque = ("Vivaldi",)
    new_tuple = months + baroque
    print(new_tuple)
    new_tuple = baroque + months
    print(new_tuple)
    print(f"{isinstance(months, type(months))}")
    list_tuple = [
        ('January', 30), ('February', 28), ('March', 31), ('April', 30),
        ('May', 31), ('June', 30), ('July', 31), ('August', 30),
    ]
    print("Print list with tuples".format(*list_tuple))
    print("Print a tuple from the list", list_tuple[7])
    print("Print a month", list_tuple[7][0])
    print("Print a number of a specific month", list_tuple[7][1])
    print([list_tuple[i][0] for i in range(len(list_tuple))])
    print([list_tuple[i][1] for i in range(len(list_tuple))])
    dictionary = dict(list_tuple)
    print(dictionary)
    print(sorted(list(months)))
    num_tuple = (0, 1, 2, 3, 4, 5)
    print(num_tuple[::-1])
    print(max(num_tuple))
    print(min(num_tuple))
    tuple_packed = ("final fantasy", "Ronin", "333")
    a, b, c = tuple_packed
    print(a, b, c)
    num_list = list(num_tuple)
    print(num_list)
    num_tuple2 = tuple(num_list)
    print(num_tuple2)
    num_tuple3 = tuple(num_list[1:4])
    print(num_tuple3)
    print((1, 2, 3,) + (9,))

"""
Review of Python
"""
import math
import random


class Guests:
    def __init__(self, array):
        self.array = array

    def inviting_guests(self):
        self.array.append("Peter")
        self.array.append("Jonathan")
        self.array.append("Hampton")
        self.array.append("Henderson")

    def print_list_confirmed_guests(self):
        print()
        if self.array:
            for guest in self.array:
                print(f"{guest.capitalize()} has confirmed!")
        else:
            print("The list is empty!")

    def unconfirmed_guests(self, guest: str):
        if self.array:
            if guest in self.array:
                location = self.array.index(guest)
                self.array.remove(guest)
                print(f"\n{guest} has been removed from the list")
                return location
            else:
                print("No unconfirmed guest found")
        else:
            print("The list is empty!")

    def new_guest(self, new_guest: str, location: int):
        if self.array:
            self.array.insert(location, new_guest)

    def more_guests(self, head_guest, middle_guest, tail_guest):
        if self.array:
            self.array.insert(0, head_guest)
            self.array.insert((len(self.array) + 1) // 2, middle_guest)
            self.array.append(tail_guest)

    def shirinking_table(self, number_to_reduced):
        size = len(self.array)
        if size < number_to_reduced:
            return
        new_number = size - number_to_reduced
        while len(self.array) > new_number:
            self.array.pop()

    def removing_the_last_two(self):
        if self.array:
            for i in range(2):
                del self.array[len(self.array)-1]



if __name__ == "__main__":
    array = []
    guests = Guests(array)
    guests.inviting_guests()
    guests.print_list_confirmed_guests()
    location = guests.unconfirmed_guests("Hampton")
    guests.print_list_confirmed_guests()
    guests.new_guest("PointDexter", location)
    guests.print_list_confirmed_guests()
    guests.more_guests("awkwafina", "Michael Corleone", "Cartman")
    guests.print_list_confirmed_guests()
    guests.shirinking_table(2)
    guests.print_list_confirmed_guests()
    guests.removing_the_last_two()
    guests.print_list_confirmed_guests()
    # Comparison Nums
    string = "Cinema Paradiso"
    print(string)
    dictionary = dict()
    for i in range(len(string)):
        dictionary[string[i]] = string.count(string[i])
    print(dictionary)


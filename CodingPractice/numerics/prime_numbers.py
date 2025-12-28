'''
@author: Solrac
'''

def get_prime(n):
    for i in range(1, n + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
                else:
                    print(i, end = ", ")
                    break


def print_prime():
    for i in range(1, 101):
        count = 0
        for j in range(2, (i // 2 + 1)):
            if i % j == 0:
                count += 1
                break
            if count == 0 and i != 1:
                print(i, end=' ')


def print_prime2():
    starts = 1
    ends = 100

    for val in range(starts, ends + 1):
        # if num is divisible by any number between 2 and val, it is not prime
        if val > 1:
            for n in range(2, val):
                if (val % n) == 0:
                    break
                else:
                    print(val, end=' ')
                    break


def prime():
    for i in range(1, 101):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
                else:
                    print(i, end=", ")
                    break

if __name__ == '__main__':
    get_prime(100)
#############################################
    # Prime number: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, etc.
    print_prime()
    print()
    print_prime2()
    print()
    prime()
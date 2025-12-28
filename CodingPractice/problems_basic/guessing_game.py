'''
@author: Solrac
'''
def game():
    low = 0
    high = 26
    guess = (low + high) / 2
    print("Think of a number between 0 to 26")
    print("is the number",guess," (too low = l or too high = h)?")
    answer = input()
    
    while answer.lower() != 'y':
        if answer == 'l':
            low = guess
        if answer == 'h':
            high = guess
        guess = (low + high) / 2
        print("is the number",guess," (too low = l or too high = h)?")
        answer = input()
    print("I got it!")

game()
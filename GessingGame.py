import random

"""
    Try to gess the number chosen by the system
"""


def play():
    game_init()
    drawn = int(random.randrange(0, 10))
    player = (input("Enter a number: "))
    numbers_used = []
    chance = 0
    while True:
        if player in numbers_used:
            print("\nHave you used it's number!")
            player = input("\nEnter another number: ")
        elif int(player) == int(drawn):
            continue_or_break(drawn, chance)
            break
        elif player not in numbers_used:
            player, chance, numbers_used = less_or_greater(player, drawn, chance, numbers_used)


def less_or_greater(player, drawn, chance, numbers_used):
    numbers_used += player
    chance += 1
    if int(player) < int(drawn):
        print("\n---->Your number is less than the chosen number!")
    else:
        print("\n---->your number is greater than the chosen number!")
    print(f"\nNumbers that you have already chosen: {numbers_used}")
    player = input("\nTry again and, enter another number: ")
    return str(player), chance, numbers_used


def continue_or_break(drawn, chance):
    print(f"\nYou win!!! the number chosen is: {drawn}")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    if chance == 1:
        print("\nYou got it wrong once!!!")
    elif chance == 2:
        print("\nYou missed twice!!!")
    else:
        print(f"\nYou missed {chance} times")
    try_again = input("You want to play again? If yes press (Y) else press (N)")
    if try_again == "y":
        play()
    game_over()
    return drawn, chance


def game_init():
    print("********************************")
    print("**********Gessing-Game**********")
    print("********************************")

def game_over():
    print("********************************")
    print("***********Game-Over************")
    print("********************************")

if __name__ == '__main__':
    play()

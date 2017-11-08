__author__ = 'Celine Yuwono, yuwono@live.unc.edu, Onyen = yuwono'

# import random
import random

# implement get_player_score function

def get_player_score():
    card1 = deal_card()
    card2 = deal_card()
    total_score = card1 + card2
    print('Your hand of two cards has a total value of ', total_score, '.', sep='')
    hit_me = input('Would you like to HIT or STAY? (y/n) ')
    while not (hit_me == 'y' or hit_me == 'n'):
        print('You entered the wrong input!!')
        hit_me = input('Would you like to HIT or STAY? (y/n) ')
    while hit_me == 'y':
        hit_card = deal_card()
        total_score = total_score + hit_card
        if total_score > 21:
            break
        print('Your hand now has a total value of', total_score)
        hit_me = input('Would you like to HIT or STAY? (y/n) ')
        while not (hit_me == 'y' or hit_me == 'n'):
            print('You entered the wrong input!!')
            hit_me = input('Would you like to HIT or STAY? (y/n) ')

    return total_score

# implement deal_card function...used in get_player_score
# updated to increase the chance of getting a 10 by 4
# and accounts for the Ace by including 11
# change of getting 10 four times out of 13 total cards
# represented by 3 times = .23 and 1 more time in randint (1,12)

def deal_card():
    list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    card_dealt = random.choice(list)
    return card_dealt


# implement get_dealer_score
# updated to deal two cards to dealer
# and to KEEP dealing cards while the score is less than 16
# Set up so dealer will bust if score is greater than 21
def get_dealer_score():
    card1 = deal_card()
    card2 = deal_card()
    dealer_score = card1 + card2
    while dealer_score < 16:
        new_card = deal_card()
        dealer_score = dealer_score + new_card
        if dealer_score > 21:
            break
    # dealer_score = random.randint(16,21)
    return dealer_score


# end game
def end_game():
    print("Thanks for playing! Goodbye.")


# define main function which has main loop that repeats for each hand
# updated to include the option for the dealer to bust if he is dealt a
# total score over 21

def main():
    total_score = get_player_score()
    if (total_score > 21):
        print('You BUSTED with a value of ', total_score, '!', sep="")
        print('**You lose!**')
    if total_score <= 21:
        print('You have stopped taking more cards with a hand value of ', total_score, '.', sep='')
        dealer_score = get_dealer_score()
        if dealer_score > 21:
            print('The dealer BUSTED with a value of ', dealer_score, '!', sep='')
            print('**You win!**')
        elif dealer_score < total_score:
            print('The dealer lost with a value of ', dealer_score, '!', sep='')
            print('**You win!**')
        else:
            print('The dealer was dealt a hand with a value of ', dealer_score, '.', sep='')
            print('**You lose!**')
    new_game = input('Would you like to play another round? (y/n)')
    while not (new_game == 'y' or new_game == 'n'):
        print('Wrong input! Try again!')
        new_game = input('Would you like to play again? (y/n)')
    while new_game == 'y':
        total_score = get_player_score()
        if (total_score > 21):
            print('You just BUSTED with a value of ', total_score, '!', sep="")
            print('**You lose!**')
        if total_score <= 21:
            print('You have stopped taking more cards with a hand value of ', total_score, '.', sep='')
            dealer_score = get_dealer_score()
            if dealer_score > 21:
                print('The dealer BUSTED with a value of ', dealer_score, '!', sep='')
                print('**You win!**')
            elif dealer_score < total_score:
                print('The dealer lost with a value of ', dealer_score, '!', sep='')
                print('**You win!**')
            else:
                print('The dealer was dealt a hand with a value of ', dealer_score, '.', sep='')
                print('**You lose!**')
        new_game = input('Would you like to play again? (y/n)')
        while not (new_game == 'y' or new_game == 'n'):
            print('Wrong input! Try again!')
            new_game = input('Would you like to play another round? (y/n)')
    else:
        end_game()


# call main
main()
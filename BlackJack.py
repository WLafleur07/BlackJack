from BlackJackArt import logo
import secrets
from os import system

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game_running = True
counter = 0


def deal_cards(card_holder, range_amount):
    for i in range(range_amount):
        card_holder.append(secrets.choice(cards))
    return card_holder

def calculate_score(cards):
    card_sum = sum(cards)
    if card_sum == 21:
        return 0
    elif card_sum > 21 and cards.count(11) > 0:
        cards.remove(11)
        cards.append(1)
    return card_sum

def compare(player_score, computer_score):
    if calculate_score(player_score) == calculate_score(computer_score):
        print("\t\nDraw\n")
    elif calculate_score(computer_score) == 21 or calculate_score(computer_score) == 0:
        print("\t\nComputer wins. You lose\n")
    elif calculate_score(player_score) == 21 or calculate_score(player_score) == 0:
        print("\t\nYou win. Computer loses\n")
    elif calculate_score(player_score) > 21:
        print("\t\nComputer wins. You lose\n")
    elif calculate_score(computer_score) > 21:
        print("\t\nYou win. Computer loses\n")
    elif calculate_score(player_score) > calculate_score(computer_score):
        print("\t\nYou win. Computer loses\n")
    else:
        print("\t\nComputer wins. You lose\n")


while game_running:
    
    if counter <= 0:
        system('cls')
        player_cards = []
        computer_cards = []
        print(logo)
        deal_cards(player_cards, 2)
        deal_cards(computer_cards, 2)
    
    print(f"Your cards: {player_cards}, current score: {calculate_score(player_cards)}")
    print(f"Computer\'s first card: {computer_cards[0]}")
   
    if calculate_score(player_cards) > 21 or calculate_score(computer_cards) == 0 or calculate_score(player_cards) == 0:
        print(f"\nYour final hand: {player_cards}, final score: {calculate_score(player_cards)}")
        print(f"Computer\'s final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")
        compare(player_cards, computer_cards)
        user_choice = input("\nDo you want to restart the game? 'Yes' or 'No': ")
        if user_choice == 'yes':
            counter = 0
        else:
            game_running = False
    else:
        user_choice = input("Do you want to draw another card? 'Yes' or 'No': ").lower()
        if user_choice == 'yes':
            deal_cards(player_cards, 1)
            counter += 1
        elif user_choice == 'no':
            while calculate_score(computer_cards) <= 17:
                deal_cards(computer_cards, 1)
            print(f"\nYour final hand: {player_cards}, final score: {calculate_score(player_cards)}")
            print(f"Computer\'s final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")
            compare(player_cards, computer_cards)
            user_choice = input("Do you want to restart the game? 'Yes' or 'No': ")
            if user_choice == 'yes':
                counter = 0
            else:
                game_running = False
           




        


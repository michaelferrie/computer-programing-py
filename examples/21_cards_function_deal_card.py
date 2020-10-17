import random
# first create a dictionary of values
card = {"1":1, "2":2, "3":3,"4":4, "5":5, "6":6,"7":7, "8":8, "9":9,"10":10, "Jack":10, "Queen":10, "King":10, "Ace":11}
suit = ["Clubs", "Hearts", "Diamonds", "Spades"]

def deal_card():
    hand = []
    deal = random.choice(list(card.values()))
    card_suit = random.choice(suit)
    hand.append(deal)
    hand.append(card_suit)
    return (hand)

first_card = deal_card()
second_card = deal_card()
third_card = deal_card()
fourth_card = deal_card()

print ("Players Hand ", first_card, second_card)
print ("Dealers Hand ", third_card, fourth_card)

"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    list_special_cards = {'J','K','Q'}
    list_normal_cards = {'2','3','4','5','6','7','8','9','10'}
    if card in list_special_cards:
        return 10
    elif card in list_normal_cards:
        return int(card)
    elif card == "A" :
        return 1 or 11
    else:
        return "There's no such card in Deck"


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
   # dictionary to map face cards
    card_values = {"A": 1, "J": 10, "Q": 10, "K": 10}

    # Handle card_one
    if card_one in card_values:
        value_one = card_values[card_one]
    else:
        value_one = int(card_one)

    # Handle card_two
    if card_two in card_values:
        value_two = card_values[card_two]
    else:
        value_two = int(card_two)
    
    if value_one > value_two:
        return card_one
    elif value_two > value_one:
        return card_two
    elif value_one == value_two:
        return (card_one, card_two)
        
        

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    # dictionary to map face cards
    card_values = {"A": 11, "J": 10, "Q": 10, "K": 10}

    # Handle card_one
    if card_one in card_values:
        value_one = card_values[card_one]
    else:
        value_one = int(card_one)

    # Handle card_two
    if card_two in card_values:
        value_two = card_values[card_two]
    else:
        value_two = int(card_two)

    if value_one + value_two > 10 :
        return 1
    else:
        return 11


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    # dictionary to map face cards
    card_values = {"A": 11, "J": 10, "Q": 10, "K": 10}

    # Handle card_one
    if card_one in card_values:
        value_one = card_values[card_one]
    else:
        value_one = int(card_one)

    # Handle card_two
    if card_two in card_values:
        value_two = card_values[card_two]
    else:
        value_two = int(card_two)

    sum_of_values = value_one + value_two

    if sum_of_values > 21 or sum_of_values < 21:
        return False
    else:
        return True


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    # dictionary to map face cards
    card_values = {"A": 11, "J": 10, "Q": 10, "K": 10}

    # Handle card_one
    if card_one in card_values:
        value_one = card_values[card_one]
    else:
        value_one = int(card_one)

    # Handle card_two
    if card_two in card_values:
        value_two = card_values[card_two]
    else:
        value_two = int(card_two)
        
    if value_one == value_two:
        return True
    else:
        return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    # dictionary to map face cards
    card_values = {"A": 1, "J": 10, "Q": 10, "K": 10}

    # Handle card_one
    if card_one in card_values:
        value_one = card_values[card_one]
    else:
        value_one = int(card_one)

    # Handle card_two
    if card_two in card_values:
        value_two = card_values[card_two]
    else:
        value_two = int(card_two)

    sum_of_values = value_one + value_two

    double_down = [9, 10 ,11]

    if sum_of_values in double_down:
        return True
    else:
        return False
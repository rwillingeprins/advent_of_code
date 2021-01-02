def parse_decks_from_file(file_path):
    with open(file_path) as file:
        deck_strings = file.read().split('\n\n')
    return ([int(card_string) for card_string in deck_string.splitlines()[1:]] for deck_string in deck_strings)


def recursive_combat(player_one_deck, player_two_deck):
    memory_set = set()
    while player_one_deck and player_two_deck:
        round_memory = (tuple(player_one_deck), tuple(player_two_deck))
        if round_memory in memory_set:
            return True
        memory_set.add(round_memory)
        player_one_card = player_one_deck.pop(0)
        player_two_card = player_two_deck.pop(0)
        player_one_wins = player_one_card > player_two_card
        if len(player_one_deck) >= player_one_card and len(player_two_deck) >= player_two_card:
            player_one_wins = recursive_combat(player_one_deck[:player_one_card], player_two_deck[:player_two_card])
        if player_one_wins:
            player_one_deck.extend([player_one_card, player_two_card])
        else:
            player_two_deck.extend([player_two_card, player_one_card])
    return bool(player_one_deck)


def score(deck):
    return sum((index + 1) * card for index, card in enumerate(reversed(deck)))


def day22a():
    player_one_deck, player_two_deck = parse_decks_from_file('input/day22.txt')
    while player_one_deck and player_two_deck:
        player_one_card = player_one_deck.pop(0)
        player_two_card = player_two_deck.pop(0)
        if player_one_card > player_two_card:
            player_one_deck.extend([player_one_card, player_two_card])
        else:
            player_two_deck.extend([player_two_card, player_one_card])
    winning_deck = player_one_deck or player_two_deck
    return score(winning_deck)


def day22b():
    player_one_deck, player_two_deck = parse_decks_from_file('input/day22.txt')
    player_one_wins = recursive_combat(player_one_deck, player_two_deck)
    winning_deck = player_one_deck if player_one_wins else player_two_deck
    return score(winning_deck)


print(day22a())
print(day22b())

import sys
from collections import deque

# Card values
VALUE_MAP = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 11, 'Q': 12, 'K': 13, 'A': 1
}

def parse_card(c):
    return int(c) if c.isdigit() else VALUE_MAP[c]

def rearrange_hand(hand, suit_priority):
    suit_order = {suit: i for i, suit in enumerate(suit_priority)}
    return sorted(hand, key=lambda x: (x[0], suit_order[x[1]]))

def simulate_game(N, p1, p2, suit_priority):
    deck1 = deque(p1)  
    deck2 = deque(p2)  
    hand = []
    turn = 0  
    seen = set()
    steps = 0
    max_steps = 10**6

    while deck1 and deck2 and steps < max_steps:
        state = (tuple(deck1), tuple(deck2), tuple(hand), turn)
        if state in seen:
            return "TIE"
        seen.add(state)

        if turn == 0:
            card = deck1.popleft()
        else:
            card = deck2.popleft()
        steps += 1

        if not hand:
            hand.append(card)
            turn = 1 - turn
            continue

        top = hand[-1]
        if (card[0] > top[0] or 
            (card[0] == top[0] and suit_priority.index(card[1]) < suit_priority.index(top[1]))):
            # Win hand
            hand.append(card)
            hand = rearrange_hand(hand, suit_priority)
            if turn == 0:
                deck1.extend(hand)
            else:
                deck2.extend(hand)
            hand = []
            # winner plays again → turn unchanged
        else:
            hand.append(card)
            turn = 1 - turn

    if not deck1 and not deck2:
        return "TIE"
    return "LOSER" if not deck1 else "WINNER"

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    N = int(data[idx])
    idx += 1

    p1, p2 = [], []
    for i in range(N):
        c1, s1 = data[idx], int(data[idx+1])
        c2, s2 = data[idx+2], int(data[idx+3])
        p1.append((parse_card(c1), s1))
        p2.append((parse_card(c2), s2))
        idx += 4

    suit_priority = [int(x) for x in data[idx:idx+4]]

    p1 = rearrange_hand(p1, suit_priority)
    p2 = rearrange_hand(p2, suit_priority)

    print(simulate_game(N, p1, p2, suit_priority))




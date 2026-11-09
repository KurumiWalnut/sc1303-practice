You have a deck of cards with distinct numbers. You'll reveal them like this, starting with the deck face down:

1. Take the top card and reveal it.
2. If cards are left, move the **next** top card to the **bottom** of the deck.
3. Repeat until every card is revealed.

Write `deck_revealed_increasing(deck)` that returns an order to stack the deck (top first) so the cards are revealed in **increasing** order.

### Examples

```text
deck_revealed_increasing([17, 13, 11, 2, 3, 5, 7])   →  [2, 13, 3, 11, 5, 17, 7]
deck_revealed_increasing([1, 1000])                  →  [1, 1000]
```

### Constraints

- Up to 100 000 cards.

Two ways to think about it:

- Compare the strings column by column and stop at the first mismatch.
- Or insert them all into a trie and walk down from the root while there is **exactly one** child and no word ends there.

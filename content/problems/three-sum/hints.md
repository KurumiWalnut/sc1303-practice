Trying every triple is O(N³). Instead:

1. **Sort** `nums`.
2. For each index `i`, find pairs in `nums[i+1:]` that sum to `-nums[i]`, using **two pointers** (as in *Two Sum II*).
3. Skip repeated values, both for `i` and when moving the pointers after a match, so no triplet appears twice.

That's O(N²).

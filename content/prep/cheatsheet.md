## Pick the structure

| The question asks… | Reach for | Cost |
|---|---|---|
| "Have I seen this before?", duplicates | `set` | O(1) per check |
| Counting, most frequent, anagrams | `dict` or `Counter` | O(N) |
| Two values that add up to a target | `dict` of value → index | O(N) |
| Search a sorted list, "first/last position", "smallest x that works" | binary search | O(log N) |
| Pairs or triples in a sorted list | two pointers from both ends | O(N) |
| Overlapping intervals, "in order of …" | sort first | O(N log N) |
| Matching brackets, undo, "next greater" | stack (`list`) | O(1) push and pop |
| First come first served, "first unique", BFS | queue (`deque`) | O(1) at both ends |
| k largest, k smallest, "keep taking the smallest" | heap (`heapq`) | O(log N) per push or pop |
| Words sharing a prefix, autocomplete | trie | O(length of the word) |
| Reachable? Connected parts? Islands? | DFS or BFS | O(V + E) |
| Fewest steps, every move costs the same | BFS | O(V + E) |
| Cheapest path, moves cost different amounts | Dijkstra | O(V²) as in the course, O(E log V) with a heap |
| The same smaller problem comes up again and again | memoization or DP | number of states × work per state |

## Big O at a glance

| Structure | Read by position | Search | Insert | Delete |
|---|---|---|---|---|
| Array (Python `list`) | O(1) | O(N) | O(N), O(1) at the end | O(N), O(1) at the end |
| Ordered array | O(1) | O(log N) | O(N) | O(N) |
| Hash table (`dict`, `set`) | – | O(1) | O(1) | O(1) |
| Stack | top only, O(1) | – | O(1) | O(1) |
| Queue (`deque`) | front only, O(1) | – | O(1) | O(1) |
| Linked list | O(N) | O(N) | O(1) at the head | O(1) at the head |
| BST | – | O(log N), O(N) if lopsided | same as search | same as search |
| AVL tree | – | O(log N) | O(log N) | O(log N) |
| Max-heap | max only, O(1) | O(N) | O(log N) | O(log N), the max |
| Trie | – | O(K), K = word length | O(K) | – |

| Sort | Best | Average | Worst | Remember |
|---|---|---|---|---|
| Bubble | O(N) | O(N²) | O(N²) | best case needs the early exit |
| Selection | O(N²) | O(N²) | O(N²) | at most N − 1 swaps |
| Insertion | O(N) | O(N²) | O(N²) | fast on nearly sorted data |
| Quicksort | O(N log N) | O(N log N) | O(N²) | worst when the pivot is always the smallest or largest, e.g. sorted input |
| Quickselect | O(N) | O(N) | O(N²) | kth smallest without sorting everything |
| Python `sort` / `sorted` | O(N) | O(N log N) | O(N log N) | stable: ties keep their order |

- **Binary search** on N items takes at most ⌊log₂ N⌋ + 1 steps: 17 for 100,000, about 20 for a million.
- **DFS and BFS** visit each vertex and edge once: O(V + E).
- **Drop constants and smaller terms:** 3N² + 5N + 2 is O(N²). Two loops one after the other are O(N); one inside the other is O(N²).

## Python tools

### list

```python
a = [5, 3, 8]
a.append(1)          # O(1): add at the end
a.pop()              # O(1): remove from the end
a.insert(0, 9)       # O(N): everything after it shifts
a.pop(0)             # O(N): for a queue, use a deque
8 in a               # O(N): a linear search
a.sort()             # O(N log N), in place. sorted(a) returns a new list
a[::-1]              # a reversed copy
grid = [[0] * 3 for _ in range(2)]   # 2 rows of 3 (see Traps)
```

### dict, Counter and defaultdict

```python
from collections import Counter, defaultdict

count = {}
for x in [3, 1, 3, 5]:
    count[x] = count.get(x, 0) + 1   # {3: 2, 1: 1, 5: 1}

for key, value in count.items():     # loop over pairs
    print(key, value)

del count[5]                         # O(1). KeyError if the key is missing
count.pop(1)                         # removes the key and returns its value: 1
count.pop(99, None)                  # with a default, a missing key isn't an error
for key in list(count):              # loop over a copy to delete while looping
    if count[key] > 1:
        del count[key]               # count is now {}

c = Counter("swiss")                 # Counter({'s': 3, 'w': 1, 'i': 1})
c.most_common(1)                     # [('s', 3)]
c["w"] -= 1                          # a count of 0 is still a key,
if c["w"] == 0:
    del c["w"]                       # so delete it when it reaches 0

groups = defaultdict(list)           # a missing key starts as []
groups["even"].append(4)
```

### set

```python
seen = set()
seen.add(4)
seen.add(7)
4 in seen              # O(1)
seen.remove(4)         # O(1). KeyError if 4 isn't there
seen.discard(4)        # no error if it isn't there
seen.pop()             # removes and returns any one item (here 7): you can't pick which
{1, 2, 3} & {2, 3, 4}  # {2, 3}     both
{1, 2} | {2, 5}        # {1, 2, 5}  either
{1, 2, 3} - {2}        # {1, 3}     in the first only
```

### deque (queue)

```python
from collections import deque

q = deque([1, 2])
q.append(3)        # add at the back
q.popleft()        # take from the front, O(1)
q.appendleft(0)    # it works at both ends
```

### heapq (min-heap)

```python
import heapq

h = []
heapq.heappush(h, 5)
heapq.heappush(h, 2)
heapq.heappop(h)                 # 2: always the smallest
nums = [4, 1, 7]
heapq.heapify(nums)              # O(N), in place
heapq.heappush(h, -9)            # max-heap: push -x, and negate what you pop
heapq.nlargest(2, [4, 1, 7])     # [7, 4]

# (priority, item) pairs: tuples compare by the first item, then the next
tasks = []
heapq.heappush(tasks, (3, "B"))
heapq.heappush(tasks, (1, "A"))
heapq.heappop(tasks)             # (1, 'A'). Keep one kind of value per heap
```

### bisect (binary search on a sorted list)

```python
import bisect

a = [1, 3, 3, 7]
bisect.bisect_left(a, 3)    # 1: the first index with a[i] >= 3
bisect.bisect_right(a, 3)   # 3: the first index with a[i] > 3
bisect.insort(a, 5)         # [1, 3, 3, 5, 7], O(N) because of the shift
```

### Sorting with a key

```python
intervals = [[8, 10], [1, 3], [2, 6]]
intervals.sort(key=lambda iv: iv[0])          # by start: [[1, 3], [2, 6], [8, 10]]

words = ["kiwi", "fig", "banana", "date"]
words.sort(key=lambda w: (-len(w), w))        # longest first, ties A to Z

from functools import cmp_to_key
strs = ["3", "30", "34", "5", "9"]
strs.sort(key=cmp_to_key(lambda a, b: -1 if a + b > b + a else 1))
"".join(strs)                                  # '9534330': the largest number
```

### Strings

```python
s = "level"
s[::-1]                  # reversed
"".join(["a", "b"])      # build a string from a list: fast. += in a loop is slow
ord("a"), chr(97)        # (97, 'a')
"a b  c".split()         # ['a', 'b', 'c']
s.isdigit(), s.isalpha()
```

### Recursion and memoization

```python
import sys
sys.setrecursionlimit(10_000)      # Python stops at about 1,000 levels by default

def fib(n, memo):                  # the course's way: the caller passes in {}
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

from functools import lru_cache

@lru_cache(maxsize=None)           # the same memo, done for you
def ways(n):                       # climbing stairs: 1 or 2 steps at a time
    return 1 if n <= 1 else ways(n - 1) + ways(n - 2)
```

## The course templates

Names follow the templates from the course site, so these drop straight in.

### Linked list (`linkedList1_template.py`)

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_list(value, head):      # add at the tail: O(N), walk to the end first
    node = head
    while node.next:
        node = node.next
    node.next = Node(value)

def reverse(head):                 # reverse in place and return the new head
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev, head = head, nxt
    return prev
```

A doubly linked list adds `prev` to each node and keeps both `head` and `tail`, so adding or removing at either end is O(1). Fast and slow pointers (one moves 1 step, the other 2) find the middle in one pass.

### Binary search tree (`BinarySearchTree_template.py`)

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left_child = left
        self.right_child = right

def search(search_value, node):
    if node is None or node.value == search_value:
        return node                                  # the node, or None
    if search_value < node.value:
        return search(search_value, node.left_child)
    return search(search_value, node.right_child)

def insert(value, node):                             # node is never None
    if value < node.value:
        if node.left_child is None:
            node.left_child = TreeNode(value)
        else:
            insert(value, node.left_child)
    elif value > node.value:
        if node.right_child is None:
            node.right_child = TreeNode(value)
        else:
            insert(value, node.right_child)

def traverse_inorder(node):                          # prints the values in sorted order
    if node is None:
        return
    traverse_inorder(node.left_child)
    print(node.value)
    traverse_inorder(node.right_child)

def isValidBST(node, low=None, high=None):   # values strictly between low and high
    if node is None:
        return True
    if low is not None and node.value <= low:
        return False
    if high is not None and node.value >= high:
        return False
    return (isValidBST(node.left_child, low, node.value)
            and isValidBST(node.right_child, node.value, high))
```

- **Max:** keep going right. **Min:** keep going left.
- **Delete:** a leaf just goes. A node with one child is replaced by that child. A node with two children takes the value of its **successor** (the smallest value in its right subtree), then that successor is deleted.
- **Traversal orders:** pre-order is node, left, right. In-order is left, node, right (sorted for a BST). Post-order is left, right, node.

### AVL tree (`AVL_tree_template.py`)

The course's balance factor is **right height − left height**. A leaf has height 1, and an empty child has height 0.

```python
def _height(n):
    return n.height if n else 0

def _update_height(n):
    n.height = 1 + max(_height(n.left), _height(n.right))

def _get_balance(n):
    return _height(n.right) - _height(n.left) if n else 0

def _rotate_left(x):               # x is too right-heavy
    y = x.right
    x.right = y.left
    y.left = x
    _update_height(x)              # x is lower now, so update it first
    _update_height(y)
    return y                       # the new root of this subtree

def _rotate_right(y):              # y is too left-heavy
    x = y.left
    y.left = x.right
    x.right = y
    _update_height(y)
    _update_height(x)
    return x
```

After inserting, update the height and check the balance factor on the way back up:

| Node's BF | Child's BF | Case | Fix |
|---|---|---|---|
| −2 | left child ≤ 0 | LL | rotate right |
| −2 | left child +1 | LR | rotate the left child left, then this node right |
| +2 | right child ≥ 0 | RR | rotate left |
| +2 | right child −1 | RL | rotate the right child right, then this node left |

### Max-heap (`Heap_template.py`)

The heap is a list. For index `i`, the parent is `(i - 1) // 2` and the children are `2 * i + 1` and `2 * i + 2`.

```python
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):     # add as the last node, then trickle up
        self.heap.append(value)
        i = len(self.heap) - 1
        while i > 0 and self.heap[i] > self.heap[(i - 1) // 2]:
            parent = (i - 1) // 2
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent

    def delete(self):            # take the root, move the last node up, trickle down
        if not self.heap:
            return None
        root = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            i = 0
            while True:
                left, right, largest = 2 * i + 1, 2 * i + 2, i
                if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                    largest = left
                if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                    largest = right
                if largest == i:
                    break
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest
        return root
```

Using the last node keeps the tree complete, so its height stays O(log N).

### Trie

```python
class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.children["*"] = None   # "*" marks the end of a word

    def search(self, word):      # the node after the last character, or None
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def collect_all_words(self, node=None, word="", words=None):
        node = node or self.root
        words = [] if words is None else words
        for char, child in node.children.items():
            if char == "*":
                words.append(word)
            else:
                self.collect_all_words(child, word + char, words)
        return words

    def autocomplete(self, prefix):
        node = self.search(prefix)
        return self.collect_all_words(node, prefix) if node else []
```

### Graph (`graph_template.py`)

```python
from collections import deque

class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []

    def add_adjacent_vertex(self, vertex):
        self.adjacent_vertices.append(vertex)

def dfs_traverse(vertex, visited_vertices):   # call as dfs_traverse(start, {})
    visited_vertices[vertex.value] = True
    print(vertex.value)
    for adjacent in vertex.adjacent_vertices:
        if not visited_vertices.get(adjacent.value):
            dfs_traverse(adjacent, visited_vertices)

def bfs_traverse(start_vertex):
    visited_vertices = {start_vertex.value: True}   # mark when it joins the queue
    queue = deque([start_vertex])
    while queue:
        vertex = queue.popleft()
        print(vertex.value)
        for adjacent in vertex.adjacent_vertices:
            if not visited_vertices.get(adjacent.value):
                visited_vertices[adjacent.value] = True
                queue.append(adjacent)
```

On a grid, the neighbours of `(r, c)` are the four cells next to it:

```python
def neighbours(grid, r, c):
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            yield nr, nc
```

### Dijkstra (`dijkstra_template.py`)

`City` has a `name` and a `routes` dict from `City` to price. This version uses a heap, and returns the same thing as the template: the cheapest price and the list of city names on the way.

```python
import heapq

def dijkstra_shortest_path(starting_city, final_destination):
    cheapest = {starting_city.name: 0}   # best price so far, by city name
    previous = {}                        # city name -> the stop before it
    visited = set()
    heap = [(0, starting_city.name, starting_city)]
    while heap:
        price, name, city = heapq.heappop(heap)
        if name in visited:
            continue
        visited.add(name)
        for adjacent, cost in city.routes.items():
            new_price = price + cost
            if adjacent.name not in cheapest or new_price < cheapest[adjacent.name]:
                cheapest[adjacent.name] = new_price
                previous[adjacent.name] = name
                heapq.heappush(heap, (new_price, adjacent.name, adjacent))
    path, name = [], final_destination.name
    while name is not None:              # walk back from the destination
        path.insert(0, name)
        name = previous.get(name)
    return cheapest[final_destination.name], path
```

> [!PROF-BUG] Week 12 seminar solution, dijkstra.py
>
> Check whether a city has a price with `name not in cheapest`, not `not cheapest.get(name)`. The start city's price is 0, which counts as missing, so a route back to the start overwrites it.

## Algorithms to know by heart

### Binary search

```python
def binary_search(array, target):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        if array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1                      # here, low is where target would be inserted

# Binary search on the answer: the largest r with r * r <= n
def integer_sqrt(n):
    low, high = 0, n
    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= n:
            low = mid + 1
        else:
            high = mid - 1
    return high
```

### Partition, quicksort and quickselect

Both partitions use the **last** element as the pivot and return the pivot's final index.

```python
def lomuto_partition(array, low, high):
    pivot = array[high]
    b = low                     # the next slot for a value below the pivot
    for a in range(low, high):
        if array[a] < pivot:
            array[a], array[b] = array[b], array[a]
            b += 1
    array[b], array[high] = array[high], array[b]
    return b

def hoare_partition(array, low, high):   # the professor's version
    pivot = array[high]
    a, b = low, high - 1
    while True:
        while a <= b and array[a] <= pivot:
            a += 1
        while a <= b and array[b] >= pivot:
            b -= 1
        if a < b:
            array[a], array[b] = array[b], array[a]
        else:
            break
    array[a], array[high] = array[high], array[a]
    return a

def quick_sort(array, low, high):
    if low < high:
        p = lomuto_partition(array, low, high)
        quick_sort(array, low, p - 1)
        quick_sort(array, p + 1, high)

def quickselect(array, k, low, high):    # the kth smallest, counting k from 0
    p = lomuto_partition(array, low, high)
    if k == p:
        return array[p]
    if k < p:
        return quickselect(array, k, low, p - 1)
    return quickselect(array, k, p + 1, high)
```

### Simple sorts

```python
def bubble_sort(arr):       # early exit, and each pass stops one sooner
    end = len(arr) - 1
    swapped = True
    while swapped and end > 0:
        swapped = False
        for i in range(end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        end -= 1

def selection_sort(arr):    # swap the smallest of the rest into place
    for i in range(len(arr) - 1):
        smallest = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]

def insertion_sort(arr):    # shift bigger values right, drop the key in
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
```

### Two pointers and prefix sums

```python
def pair_with_sum(sorted_nums, target):   # move whichever end fixes the sum
    lo, hi = 0, len(sorted_nums) - 1
    while lo < hi:
        total = sorted_nums[lo] + sorted_nums[hi]
        if total == target:
            return lo, hi
        if total < target:
            lo += 1
        else:
            hi -= 1
    return None

def count_subarrays_with_sum(nums, k):    # running sums seen so far, in a dict
    seen = {0: 1}
    total = count = 0
    for x in nums:
        total += x
        count += seen.get(total - k, 0)
        seen[total] = seen.get(total, 0) + 1
    return count
```

## Input and output on HackerEarth

Many HackerEarth questions read their input and expect you to **print** the answer. If the question gives you a function to complete instead, **return** the answer and don't print anything else.

```python
n = int(input())                         # one number on a line
nums = list(map(int, input().split()))   # numbers on one line, split by spaces
rows = [input() for _ in range(n)]       # n lines

import sys
data = sys.stdin.read().split()          # everything at once: fastest

print(*nums)                             # 1 2 3
print(" ".join(map(str, nums)))          # the same
print(f"{3.14159:.2f}")                  # 3.14
```

## Traps

- `[[0] * m] * n` makes n copies of **one** row. Use `[[0] * m for _ in range(n)]`.
- `list.pop(0)` and `list.insert(0, x)` are O(N). Use a `deque` for a queue.
- `def f(memo={})` shares one dict between every call. Pass `{}` in, as the course does.
- Deep recursion stops at about 1,000 levels. Raise it with `sys.setrecursionlimit`, or use a loop.
- Don't name variables `max`, `min`, `sum`, `list` or `dict`: they hide the built-ins. The BST template's `max` does exactly that.
- `/` always gives a float. Use `//` for indexes: `mid = (low + high) // 2`.
- `heapq` is a **min**-heap. For the largest first, push `-x`.
- Don't add to or remove from a list, dict or set while looping over it. A dict or set stops with `RuntimeError: ... changed size during iteration`. Loop over a copy (`for key in list(d):`), or build a new one.
- Compare values with `==`. Keep `is` for `None`.
- Try the edge cases before you submit: an empty list, one item, all items equal, and the largest input.

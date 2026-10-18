# Algorithms & Data Structures (Python)

**Module:** CMPN203 Algorithms, Year 2 (Autumn 2025), University of Roehampton. **Module mark: 75% (First)**  
Coursework portfolio 76% · closed-book written exam 74%

## Coursework 1: Linear data structures ([`coursework1-linear-data-structures/`](coursework1-linear-data-structures))

### Task 1: Stack arithmetic ([`task1_stack.py`](coursework1-linear-data-structures/task1_stack.py))
The digits of a student ID are pushed onto a stack. Repeatedly pop the top two numbers and push back:
- both odd → **sum**
- both even → **product**
- mixed → **larger − smaller**

until one number remains. Implemented with a custom `Stack` class (list-backed `push`/`pop`/`is_empty`/`size`),
step-by-step trace output, and an extra mode that runs the algorithm on any user-entered number.
Includes a [flowchart](coursework1-linear-data-structures/task1-flowchart.pdf) (distinction component).

```text
Initial stack (bottom - top): [0, 0, 0, 2, 7, 0, 5, 2]
Step 1: mixed - |5 - 2| = 3
Step 2: mixed - |0 - 3| = 3
Step 3: both odd - 7 + 3 = 10
Step 4: both even - 2 * 10 = 20
...
Final value on stack: 0
```

### Task 2: Full name as a singly linked list ([`task2_fullname.py`](coursework1-linear-data-structures/task2_fullname.py))
Each letter of a full name is a `Node(position, letter, part)` where `part` is first/middle/last name.
The `Full_Name` class keeps `head`, `tail` and `size` and implements:

| Method | What it does | Cost |
|---|---|---|
| `Add_element` | Append a node using the tail pointer | O(1) |
| `Add_word` | Append each letter of a word | O(k) |
| `Get_element` | Walk to a position, bounds-checked | O(n) |
| `Search_element` | Print every position of a letter | O(n) |
| `Print_list` / `Print_full_name` | Traverse and format | O(n) |
| `Remove_word` *(distinction)* | Unlink every node of one part, then renumber positions | O(n) |

Driven by a menu-based CLI with input validation.

## Coursework 2: Algorithms report ([`coursework2-algorithms-report/algorithms-report.pdf`](coursework2-algorithms-report/algorithms-report.pdf))
Hand-traced, step by step, on the letters of my name `[f,a,r,h,a,n,a,h,m,e,d,s,a,h,o,l]`:
- **Sorting:** insertion sort (15 passes), merge sort (15 merges), quick sort (last-element pivot, 11 partitions), plus a best/worst-case, space and stability comparison
- **Graphs:** Dijkstra's shortest paths from node A, with a distance table at every step
- **Hashing:** 26-bucket hash table (`h(c) = c − 'a'`) with chaining for repeated letters
- **Trees:** binary search tree built from insertion order, ignoring duplicates

## Run
```bash
cd coursework1-linear-data-structures
python3 task1_stack.py
python3 task2_fullname.py
```
No external packages needed (Python 3.8+).

# Coding Test Solutions

This repository provides plain Python script solutions to two programming problems from the "Coding Test - R&D Team" PDF:

1. **Plus One**  
   Increment a large integer (represented as a list of digits) by one.
2. **Alternate Min-Max Rearrangement**  
   Rearrange an array so that elements alternate between min, max, 2nd-min, 2nd-max, etc.

---

## Files

- **test.py**  
  Contains both function implementations with inline comments explaining the logic:
  - `plus_one(digits: List[int]) -> List[int]`  
  - `alternate_min_max(arr: List[int]) -> List[int]`

- **README.md**  
  This documentation file.

## Requirements

- Python 3.10 or newer

## Usage

1. **Clone or download** this repository.
2. **Run Python Script** 

### Example
```bash
$ python test.py
```

## Functions

### `plus_one(digits)`
- **Input**: List of digits (`[0-9]`) with no leading zeros.
- **Output**: New list of digits representing the original number plus one.
- **Approach**:
  1. Traverse from the last digit backwards.
  2. If digit < 9, increment and return.
  3. If digit == 9, set to 0 and carry on.
  4. If all digits were 9, insert `1` at the front.

### `alternate_min_max(arr)`
- **Input**: List of integers (can be negative, zero, or positive).
- **Output**: New list where elements alternate between smallest, largest, next smallest, next largest, etc.
- **Approach**:
  1. Sort the array ascending.
  2. Use two pointers (`left` at start, `right` at end).
  3. Append `arr[left]` then `arr[right]`, moving pointers inward.
  4. Continue until pointers cross.

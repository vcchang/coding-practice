# Sort array by parity

# Input: array of non-negative integers, arr

# In-place approach
# Time: O(n)  -> check every int in worst case
# Space: O(1) -> in-place uses no extra space

from typing import List
import copy

def sort(arr: List[int]):
    front = 0
    back = len(arr) - 1

    while back > front:
        if arr[front] % 2 != 0:
            while arr[back] % 2 != 0 and back > front:
                back -= 1
            arr[front], arr[back] = arr[back], arr[front]
            front += 1
            back -= 1
        else:
            front += 1
    return arr

if __name__ == "__main__":
    arr = [4, 3, 2, 1, 5]
    originalArr = copy.deepcopy(arr)
    expected = [4, 2, 3, 1, 5]
    actual = sort(arr)
    assert actual == expected
    print(f"Yay sorted the array {originalArr} by parity! Result: {actual}")

    arr2 = [3, 1, 2, 4]
    originalArr2 = copy.deepcopy(arr2)
    expected2 = [4, 2, 1, 3]
    actual2 = sort(arr2)
    assert actual2 == expected2
    print(f"Yay sorted the array {originalArr2} by parity! Result: {actual2}")

    emptyArr = []
    originalEmptyArr = []
    expectedEmpty = []
    actualEmpty = sort(emptyArr)
    assert actualEmpty == expectedEmpty
    print(f"Woop woop sorted the array {originalEmptyArr} by parity! Result: {actualEmpty}")

    arrEvenOnly = [4, 6, 2, 2, 8]
    originalEvenOnlyArr = copy.deepcopy(arrEvenOnly)
    expectedEvenOnly = [4, 6, 2, 2, 8]
    actualEvenOnly = sort(arrEvenOnly)
    assert actualEvenOnly == expectedEvenOnly
    print(f"No sorting needed for this even-only array: {originalEvenOnlyArr}. Result: {actualEvenOnly}")

    arrOddOnly = [3, 5, 9, 1, 7]
    originalOddOnlyArr = copy.deepcopy(arrOddOnly)
    expectedOddOnly = [3, 5, 9, 1, 7]
    actualOddOnly = sort(arrOddOnly)
    assert actualOddOnly == expectedOddOnly
    print(f"No sorting needed for this odd-only array: {originalOddOnlyArr}. Result: {actualOddOnly}")

    arrOneElem = [0]
    originalOneElemArr = copy.deepcopy(arrOneElem)
    expectedOneElem = [0]
    actualOneElem = sort(arrOneElem)
    assert actualOneElem == expectedOneElem
    print(f"Yay sorted the array {originalOneElemArr} by parity! Result: {actualOneElem}")

    arrTwoElem = [0, 1]
    originalTwoElemArr = copy.deepcopy(arrTwoElem)
    expectedTwoElem = [0, 1]
    actualTwoElem = sort(arrTwoElem)
    assert actualTwoElem == expectedTwoElem
    print(f"Yay sorted the array {originalTwoElemArr} by parity! Result: {actualTwoElem}")

    arrTwoElem2 = [1, 0]
    originalTwoElemArr2 = copy.deepcopy(arrTwoElem2)
    expectedTwoElem2 = [0, 1]
    actualTwoElem2 = sort(arrTwoElem2)
    assert actualTwoElem2 == expectedTwoElem2
    print(f"Yay sorted the array {originalTwoElemArr2} by parity! Result: {actualTwoElem2}")

    arrThreeElem = [0, 1, 3]
    originalThreeElemArr = copy.deepcopy(arrThreeElem)
    expectedThreeElem = [0, 1, 3]
    actualThreeElem = sort(arrThreeElem)
    assert actualThreeElem == expectedThreeElem
    print(f"Yay sorted the array {originalThreeElemArr} by parity! Result: {actualThreeElem}")
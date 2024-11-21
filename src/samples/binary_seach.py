def binary_search(arr: list[int], target: int) -> int:
    left: int = 0
    right: int = len(arr) - 1

    while left <= right:
        mid: int = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

print(binary_search([1, 2, 3, 4, 5], 4))

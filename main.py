class BinarySearch:
    @staticmethod
    def binary_search(lst, target):
        if len(lst) <= 0 or target < lst[0] or target > lst[len(lst) - 1]:
            return -1
        else:
            left = 0
            right = len(lst) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if lst[mid] == target:
                    return mid
                elif target < lst[mid]:
                    right = mid - 1
                elif target > lst[mid]:
                    left = mid + 1

        return -1


ls = [1, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(1, 11):
    print(BinarySearch.binary_search(ls, i))

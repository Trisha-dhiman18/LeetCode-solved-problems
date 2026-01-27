# For Linear Search
# Applies on both sorted and unsorted arrays
class Solution:
    def search(self, arr, x):
        for i in range(len(arr)):
            if arr[i] == x:
                return i
        return -1


# Binary Search
# Applies only on sorted arrays
class Solution:
    def search(self, arr, x):
        i = 0
        j = len(arr) - 1

        while i <= j:
            mid = (i + j) // 2

            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                i = mid + 1
            else:
                j = mid - 1

        return -1

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        win_count = 0
        if k > len(arr):
            return max(arr)

        if k == 1:
            return max(arr[0], arr[1])

        while True:
            if arr[0] > arr[1]:
                win_count += 1
                if win_count == k:
                    return arr[0]
                arr.append(arr.pop(1))
            else:
                win_count = 1
                arr.append(arr.pop(0))

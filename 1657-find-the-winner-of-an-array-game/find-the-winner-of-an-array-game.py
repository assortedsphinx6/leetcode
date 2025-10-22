class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr)-1:
            return max(arr)

        champion = arr[0]
        win_streak=0

        for i in range(1,len(arr)):
            if arr[i] > champion:
                champion = arr[i]
                win_streak=1
            else:
                win_streak+=1
            if win_streak ==k:
                return champion
        return champion

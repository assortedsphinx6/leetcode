import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # sort by start time
        intervals.sort(key=lambda x: x[0])
        
        # min-heap for end times
        heap = []
        heapq.heappush(heap, intervals[0][1])
        
        for i in range(1, len(intervals)):
            # if the current meeting starts after the earliest one ends, reuse the room
            if intervals[i][0] >= heap[0]:
                heapq.heappop(heap)
            # push the current meeting’s end time
            heapq.heappush(heap, intervals[i][1])
        
        # the heap size = number of rooms used simultaneously
        return len(heap)
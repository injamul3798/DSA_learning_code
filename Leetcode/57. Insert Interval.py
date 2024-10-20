class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        results = []
        for interval in intervals:
            # If the intervals finish before a new interval starts
            if interval[1] < newInterval[0]:
                results.append(interval)
            # if intervals start after finishng new interval
            elif interval[0] > newInterval[1]:
                results.append(newInterval)
                newInterval = interval
            else:
                newInterval[0] = min(newInterval[0],interval[0])
                newInterval[1] = max(newInterval[1],interval[1])

        results.append(newInterval)
        return results

        
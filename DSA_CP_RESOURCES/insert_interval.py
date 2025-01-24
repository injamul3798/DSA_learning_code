class Solution:
    def insertInterval(self, intervals, newInterval):
        res = []
        for interval in intervals:
            if interval[1]<newInterval[0]:
                res.append(interval)
 
            elif (interval[0] >  newInterval[1]):
                res.append(newInterval)
                newInterval = interval
            else:
                mn = min(interval[0],newInterval[0])
                mx = max(interval[1],newInterval[1])
                newInterval = [mn,mx]
        res.append(newInterval)
        
        return res
        
        
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        intervals = []
        for _ in range(n):
            lis = list(map(int,input().split()))
            intervals.append(lis)
            
        newInterval = list(map(int,input().split()))
        obj  = Solution()
        print(obj.insertInterval(intervals,newInterval))

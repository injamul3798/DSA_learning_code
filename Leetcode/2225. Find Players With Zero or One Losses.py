class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        winner = {}
        one_lost = {}
        for match in matches:
            if  match[0] in winner:
                winner[match[0]] += 1
            else:
                winner[match[0]] = 1

        for match in matches:
            if  match[1] in one_lost:
                one_lost[match[1]] += 1
            else:
                one_lost[match[1]] = 1

       
        for key,value in winner.items():
            if key in one_lost:
                winner.pop(key,None)
        ans1 = []
        for key,value in winner.items():
            ans1.append(key)


        # Okay this part
        ans2 = []
        for key,value in one_lost.items():
            if value==1:
                ans2.append(key)
            else:
                continue
        ans1.sort()
        ans2.sort()

        return [ans1,ans2]
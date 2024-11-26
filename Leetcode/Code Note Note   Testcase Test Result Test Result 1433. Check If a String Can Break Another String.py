class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        final_s1 = sorted(s1)
        final_s2 = sorted(s2)

        cnt1 = cnt2 = 0
        # Check if s1 can break s2
        for i in range(len(final_s1)):
            if final_s1[i] < final_s2[i]:
                cnt1 = 1
                break
        # Check if s2 can break s1
        for i in range(len(final_s1)):
            if final_s1[i] > final_s2[i]:
                cnt2 = 1
                break

        if cnt1 == 0 or cnt2 == 0:
            return True
        else:
            return False

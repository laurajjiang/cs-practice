class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if len(intervals) == 0:
            return True
        intervals.sort(key=lambda x: x[0])
        currMeeting = intervals[0]
        for i in range(1, len(intervals)):
            if currMeeting[1] > intervals[i][0]:
                return False
            currMeeting = intervals[i]
        return True

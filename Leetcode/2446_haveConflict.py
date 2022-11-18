class Solution(object):
    def haveConflict(self, event1, event2):
        """
        :type event1: List[str]
        :type event2: List[str]
        :rtype: bool
        """
        for event in [event1, event2]:
            for i in range(len(event)):
                event[i] = float(event[i].replace(":",".")) 
        if event1[0] < event2[0]:
            return event1[1] >= event2[0]
        else:
            return event2[1] >= event1[0]
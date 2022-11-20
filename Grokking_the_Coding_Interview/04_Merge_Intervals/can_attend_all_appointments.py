def can_attend_all_appointments(intervals):
    intervals.sort(key = lambda x: x[0])
    start, end = 0, 1
    for i in range(1, len(intervals)):
        if intervals[i][start] < intervals[i-1][end]:
            return False
    return True

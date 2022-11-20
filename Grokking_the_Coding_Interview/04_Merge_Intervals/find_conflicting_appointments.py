def find_conflicting_appointments(intervals):
    intervals.sort(key= lambda x: x[0])
    conflicting_appts=[]
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            conflicting_appts.append([intervals[i-1], intervals[i]])
    for appt in conflicting_appts:
        print(f"{appt[0]} and {appt[1]} conflict.")
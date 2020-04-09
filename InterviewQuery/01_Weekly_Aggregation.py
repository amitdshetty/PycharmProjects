from datetime import datetime

class Solution():
    def weekly_aggregation(self, datelist):
        new_date_list = []
        for i in datelist:
            s = datetime.strptime(i, '%Y-%m-%d')
            new_date_list.append(s)
        # print(new_date_list)
        weeks = []
        week = []
        start_date = None
        for i in new_date_list:
            if new_date_list.index(i) == 0:
                week.append(i)
                start_date = i
                continue
            diff = i - start_date
            n = diff.days // 7
            if n == 0:
                # print('hello')
                week.append(i)
            elif n >= 1:
                weeks.append(week)
                # tried clearing the list but it also cleared the previous reference
                week = []
                start_date = i
                week.append(i)
        if len(week) > 0:
            weeks.append(week)
        for j in weeks:
            print(j)


dates = [
'2019-01-01',
'2019-01-02',
'2019-01-08',
'2019-02-01',
'2019-02-02',
'2019-02-05',
]
sol = Solution()
sol.weekly_aggregation(dates)

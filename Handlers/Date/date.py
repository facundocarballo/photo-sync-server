YEAR = 0
MONTH = 1
DAY = 2

YEAR_KEYWORD = 'year'
MONTH_KEYWORD = 'month'
DAY_KEYWORD = 'day'

class Date:
    def __init__(self, date: any) -> None:
        self.year = str(date[YEAR_KEYWORD])
        self.month = str(date[MONTH_KEYWORD])
        self.day = str(date[DAY_KEYWORD])
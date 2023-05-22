import datetime


class Date(object):
    def __init__(self):
        self.date = datetime.datetime(2023, 1, 1).strftime("%Y-%m-%d")

    def get_date(self):
        return self.date

    def set_date(self):
        self.date = datetime.datetime.strptime(
            self.date, "%Y-%m-%d"
        ) + datetime.timedelta(days=1)
        self.date = self.date.strftime("%Y-%m-%d")

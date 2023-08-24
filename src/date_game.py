import datetime
import time
from time import perf_counter


class Date_game(object):
    def __init__(self):
        self.date = datetime.datetime(2022, 1, 1).strftime("%Y-%m-%d")
        self.etat = True
        self.update_time = perf_counter()

    def get_etat(self):
        return self.etat

    def set_etat(self):
        if self.etat == False:
            self.etat = True
        else:
            False

    def get_date(self):
        return self.date

    def set_date(self):
        if perf_counter() - self.update_time >= 1:
            self.update_time = perf_counter()
            self.date = datetime.datetime.strptime(
                self.date, "%Y-%m-%d"
            ) + datetime.timedelta(days=1)
            self.date = self.date.strftime("%Y-%m-%d")

    def game(self):
        while True:
            self.set_date()
            time.sleep(20)

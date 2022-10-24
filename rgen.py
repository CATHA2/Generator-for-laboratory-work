from random import getrandbits
from datetime import timedelta, date
import pickle


class RandomGenerator:
    def __init__(self):

        print("Введіть по черзі день/місяць/рік народження:")
        self.DAY = self._input_("День")
        self.MONTH = self._input_("Місяць")
        self.YEAR = self._input_("Рік")

        self.DAY_NOW = date.today()
        self.DAY_HB = date(day=self.DAY, month=self.MONTH, year=self.YEAR)

        self.difference = int((self.DAY_NOW - self.DAY_HB).days)

        self.DATA = []

        self._random_()

        self.info()

        self._save_()

    def get_date(self):
        print(f'{self.DAY}.{self.MONTH}.{self.YEAR}')

    def info(self):
        print(f'\n'
              f'День народження: {self.DAY_HB.day}.{self.DAY_HB.month}.{self.DAY_HB.year}\n'
              f'Сьогодні: {self.DAY_NOW.day}.{self.DAY_NOW.month}.{self.DAY_NOW.year}\n'
              f'Дні між ними: {(self.DAY_NOW - self.DAY_HB).days}\n'
              f'Даних - {len(self.DATA)}')

    def _random_(self):

        self.action_1 = bool(getrandbits(1))
        self.action_2 = bool(getrandbits(1))
        self.action_3 = bool(getrandbits(1))
        self.action_4 = bool(getrandbits(1))
        self.action_5 = bool(getrandbits(1))

        if self.action_1:
            date_1 = self.DAY_HB + timedelta(days=self.difference)
        else:
            date_1 = (self.DAY_HB - timedelta(days=self.difference))
        if self.action_2:
            data = date_1.day + date_1.month
        else:
            data = date_1.day - date_1.month
        if self.action_3:
            data = data + date_1.year
        else:
            data = data - date_1.year
        if self.action_4:
            data = data * self.difference
        else:
            data = data / self.difference
        data = int(data)
        if self.action_5:
            if data < 0:
                data *= -1
                datalist = list(str(data))
                datalist.reverse()
                data = int(''.join(datalist))
                data *= -1
            else:
                datalist = list(str(data))
                datalist.reverse()
                data = int(''.join(datalist))
        start = data
        stop = data + int(f'{date_1.day}_{date_1.year}_{date_1.month}')
        print(f"Генерація від {start} до {stop}")
        for num in range(start, stop):
            self.DATA.append(num)

    def save_txt(self):
        with open(f"Save.txt", 'w') as file:
            file.write(", ".join(str(item) for item in self.DATA))

    def _save_(self):
        with open(f"Save.pickle", 'wb') as file:
            pickle.dump(self.DATA, file)

    @staticmethod
    def _input_(text):
        value = ''
        while type(value) != type(str):
            try:
                value = int(input(f"{text}: "))
                return value
            except ValueError:
                continue
            except KeyboardInterrupt:
                exit()


if __name__ == '__main__':
    RandomGenerator()

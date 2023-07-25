"""def filterfalse(predicate, iterable):
    if predicate == None:
        return filter(lambda x: not x, iterable)
    else:
        return filter(lambda x: predicate(x) is False, iterable)




numbers = [1, 2, 3, 4, 5]

print(*filterfalse(lambda x: x >= 3, numbers))"""



"""def transpose(matrix):
    res = [item for item in zip(*matrix)]
    return list(map(lambda x: list(x), res))


matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10]]

for row in transpose(matrix):
    print(row)"""


"""def get_min_max(data):
    if data == []:
        return None
    else:
        return (data.index(min(data)), data.index(max(data)))


data = [1, 5, 2, 3, 8, 1]

print(get_min_max(data))"""


"""def starmap(func, iterable):
    z = []
    for i in iterable:
        z.append(func(*i))
    return z


points = [(1, 1, 1), (1, 1, 2), (2, 2, 3)]

print(*starmap(lambda x, y, z: x * y * z, points))"""


"""def get_min_max(iterable):
    min_list = []
    max_list = []
    z = []
    for i in iterable:
        z.append(i)

    if len(z) == 0:
        return None
    else:
        for i in iterable:
            min_list.append(i)
            max_list.append(i)
    return min(min_list), max(max_list)"""


"""def get_min_max(iterable):
    min_list = []
    max_list = []
    z = []
    for i in iterable:
        z.append(i)
        min_list.append(i)
        max_list.append(i)
    if len(z) == 0:
        return None
    else:
        return min(min_list), max(max_list)"""
"""import time, sys
from copy import copy

stat = time.time()
def get_min_max(iterable):
    cop1 = copy(iterable)
    try:
        return min(iterable), max(cop1)
    except:
        return None


data = iter(range(100_000_000))

print(get_min_max(data))

stop = time.time()

print(sys.getsizeof(get_min_max))
print(stop - stat)"""


"""import functools

def seperator(line='*', star=1):
    def dec_separator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            print(line * star)
            return value
        return wrapper
    return dec_separator

@seperator(line='=', star=20)
def say_hi():
    return "Hello!"


print(say_hi())"""


"""infinite_love = iter(lambda: 'i love beegeek!', '')

print(next(infinite_love))
print(next(infinite_love))
print(next(infinite_love))"""


"""def is_iterable(obj):
    if '__iter__' in dir(obj):
        return True
    else:
        return False


objects = [(1, 13), 7.0004, [1, 2, 3]]

for obj in objects:
    print(is_iterable(obj))
"""


"""def is_iterator(obj):
    if '__next__' in dir(obj):
        return True
    else:
        return False


beegeek = filter(None, [0, 0, 1, 1, 0, 1])

print(is_iterator(beegeek))"""


"""from random import choice

def random_numbers(left, right):
    values = list(range(left, right + 1))
    return iter(lambda: choice(values), '')


iterator = random_numbers(1, 10)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))"""


"""class Repeater:
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        return self

    def __next__(self):
        return self.obj


geek = Repeater('geek')

print(next(geek))
print(next(geek))
print(next(geek))"""


"""class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj
        self.times = times
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index > self.times:
            raise StopIteration
        return self.obj

geek = BoundedRepeater('geek', 3)

print(next(geek))
print(next(geek))
print(next(geek))

try:
    print(next(geek))
except StopIteration:
    print('Error')"""


"""class Square:
    def __init__(self, n):
        self.n = n
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index > self.n:
            raise StopIteration
        return self.index**2

squares = Square(1)

print(list(squares))"""


"""class Fibonacci:
    def __init__(self):
        self.first = 1
        self.second = 0
        self.sum_nums = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.first, self.second = self.second, self.first + self.second
        return self.second


fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))"""

"""
class PowerOf:
    def __init__(self, number):
        self.number = number
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        return self.number**self.index


power_of_two = PowerOf(2)

print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))"""


"""class DictItemsIterator:
    def __init__(self, data):
        self.data = data
        self.just_data = [*data]
        self.index = 0
        self.lst_of_tuples = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        else:
            key = self.just_data[self.index]
            value = self.data[key]
            self.index += 1
            return key, value


pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})

print(*pairs)"""


"""class CardDeck():
    def __init__(self):
        self.mast = {1: 'пик', 2: 'треф', 3: 'бубен', 4: 'червей'}
        self.lst_cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
        self.index = 0
        self.card_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 52:
            raise StopIteration

        elif self.index in range(0, 13):
            num = self.lst_cards[self.card_index]
            value = self.mast[1]
            self.card_index += 1
            self.index += 1

            if self.card_index == 13:  # проверка на то если счетчик станет равен 13, то он обнуляется
                self.card_index = 0
            return num + ' ' + value

        elif self.index in range(13, 26):
            num = self.lst_cards[self.card_index]
            value = self.mast[2]
            self.card_index += 1
            self.index += 1

            if self.card_index == 13: # проверка на то если счетчик станет равен 13, то он обнуляется
                self.card_index = 0
            return num + ' ' + value

        elif self.index in range(26, 39):
            num = self.lst_cards[self.card_index]
            value = self.mast[3]
            self.card_index += 1
            self.index += 1

            if self.card_index == 13:
                self.card_index = 0
            return num + ' ' + value

        elif self.index in range(39, 52):
            num = self.lst_cards[self.card_index]
            value = self.mast[4]
            self.card_index += 1
            self.index += 1

            if self.card_index == 13:
                self.card_index = 0
            return num + ' ' + value


cards = list(CardDeck())

print(cards[9])
print(cards[23])
print(cards[37])
print(cards[51])"""


"""class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.iterable):
            self.index = 0
        result = self.iterable[self.index]
        self.index += 1
        return result


cycle = Cycle(range(100_000_000))

print(next(cycle))
print(next(cycle))"""

"""from random import choice

class RandomNumbers:
    def __init__(self, left, right, n):
        self.left = left    # граница первого числа
        self.right = right  # граница последнего числа
        self.n = n          # количество чисел из этих границ, которые нужно вывести
        self.query = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.query >= self.n:
            raise StopIteration
        result = choice(range(self.left, self.right + 1))
        self.query += 1
        return result

iterator = RandomNumbers(1, 1, 3)

print(next(iterator))
print(next(iterator))
print(next(iterator))"""


"""class Alphabet:
    def __init__(self, language):
        self.language = language
        self.ru_index = 0
        self.en_index = 0
        self.ru_str = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        self.en_str = 'abcdefghijklmnopqrstuvwxyz'

    def __iter__(self):
        return self

    def __next__(self):
        if self.language == 'ru':
            if self.ru_index == 32:
                self.ru_index = 0
            result = self.ru_str[self.ru_index]
            self.ru_index += 1
            return result

        elif self.language == 'en':
            if self.en_index == 26:
                self.en_index = 0
            result = self.en_str[self.en_index]
            self.en_index += 1
            return result


en_alpha = Alphabet('en')

letters = [next(en_alpha) for _ in range(28)]

print(*letters)"""


"""class Xrange:
    def __init__(self, start, end, step: int or float = 1):
        self.start = start  # int or float number
        self.end = end      # int or float которое не включается в границу
        self.step = step    # int or float которое является шагом арифмитеческой прогрессии
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):  # предусмотреть вариант с отрицательным шагом
        if self.step > 0:
            if self.start >= self.end:
                raise StopIteration
            res = self.start
            self.start += self.step
            return float(res) if type(self.step) == float else res

        elif self.step < 0:
            if self.end >= self.start:
                raise StopIteration
            res = self.start
            self.start += self.step
            return float(res) if type(self.step) == float else res

xrange = Xrange(5, 10)

print(*xrange)"""



# Ошибка заключалась в том, что я не проверил изначально, что вывод должен быть цикличным. То есть бесконечным.
"""def card_deck(suit):
    z = []
    card_lst = ['пик', 'треф', 'бубен', 'червей']
    card_nominal = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
    for i in card_lst:
        if i != suit:
            z.append(i)

    index_nominal = 0
    index_card_lst = 0
    res_num = 0


    while index_nominal != 13:
        if res_num == 39:
            index_nominal = 0
            index_card_lst = 0
            res_num = 0
        yield card_nominal[index_nominal] + " " + z[index_card_lst]
        index_nominal += 1
        res_num += 1
        if index_nominal == 13:
            index_nominal = 0
            index_card_lst += 1





generator = card_deck('пик')

cards = [next(generator) for _ in range(80)]

print(*cards)"""


"""def matrix_by_elem(matrix):
    for i in matrix:
        yield from i


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(*matrix_by_elem(matrix))"""


"""def palindromes():
    num = 1  # 101
    while True:
        if str(num) == str(num)[::-1]:
            yield num
        num += 1


generator = palindromes()
numbers = [next(generator) for _ in range(30)]

print(*numbers)"""


"""def flatten(nested_list):
    for i in nested_list:
        if type(i) == int:
            yield i
        else:
            yield from flatten(i)


generator = flatten([[1, 2], [[3]], [[4], 5]])

print(*generator)"""


"""class PiggyBank:
    pass

money_box1 = PiggyBank()
money_box2 = PiggyBank()

money_box1.coins = 10
money_box2.coins = 15
money_box2.color = 'pink'"""


"""class PiggyBank:
    content = "coins"
    alternate_name = "penny_bank"

money_box = PiggyBank()"""


"""class Gun:
    def shoot(self):
        print('pif')


gun = Gun()

gun.shoot()
gun.shoot()
gun.shoot()"""


"""class User:
    def __init__(self, name):
        self.name = name
        self.friends = 0

    def add_friends(self, n):
        self.friends += n


user = User('Timur')

user.add_friends(2)
user.add_friends(2)
user.add_friends(3)

print(user.friends)"""


"""class House:
    def __init__(self, color, rooms):
        self.color = color
        self.rooms = rooms

    def paint(self, new_color):
        self.color = new_color

    def add_rooms(self, n):
        self.rooms += n

house = House('white', 4)

print(house.color)
print(house.rooms)"""

"""from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius * 2
        self.area = pi * radius**2



circle = Circle(5)

print(circle.radius)
print(circle.diameter)
print(circle.area)"""


"""class Bee:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_up(self, n):
        self.y += n

    def move_down(self, n):
        self.y -= n

    def move_right(self, n):
        self.x += n

    def move_left(self, n):
        self.x -= n


bee = Bee()

bee.move_right(2)
bee.move_right(2)
bee.move_up(3)
bee.move_left(1)
bee.move_down(1)

print(bee.x, bee.y)"""


"""class Gun:
    def __init__(self):
        self.index = 0
    def shoot(self):
        if self.index % 2 == 0:
            print('pif')
        else:
            print('paf')
        self.index += 1

gun = Gun()

gun.shoot()
gun.shoot()
gun.shoot()
gun.shoot()"""


"""class Gun:
    def __init__(self):
        self.index = 0

    def shoot(self):
        if self.index % 2 == 0:
            print('pif')
        else:
            print('paf')
        self.index += 1

    def shots_count(self):
        return self.index

    def shots_reset(self):
        self.index = 0

gun = Gun()

gun.shoot()
gun.shoot()
print(gun.shots_count())
gun.shots_reset()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())"""


"""class Scales:
    def __init__(self):
        self.right = 0
        self.left = 0

    def add_right(self, kg):
        self.right += kg

    def add_left(self, kg):
        self.left += kg

    def get_result(self):
        if self.right == self.left:
            return 'Весы в равновесии'
        elif self.right > self.left:
            return 'Правая чаша тяжелее'
        else:
            return 'Левая чаша тяжелее'



scales = Scales()

scales.add_right(2)
scales.add_left(1)

print(scales.get_result())"""

"""from math import sqrt

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def abs(self):
        return sqrt(self.x**2 + self.y**2)


vector = Vector(3, 4)

print(vector.x, vector.y)
print(vector.abs())"""


"""class Numbers:
    def __init__(self):
        self.lst = []

    def add_number(self, n):
        self.lst.append(n)

    def get_even(self):
        res = list(filter(lambda x: x % 2 == 0, self.lst))
        return res

    def get_odd(self):
        res = list(filter(lambda x: x % 2 != 0, self.lst))
        return res

numbers = Numbers()

numbers.add_number(1)
numbers.add_number(3)
numbers.add_number(1)

print(numbers.get_even())
print(numbers.get_odd())"""


"""class TextHandler:
    def __init__(self):
        self.lst = []

    def add_words(self, text):
        text1 = text.split()
        self.lst.extend(text1)

    def get_shortest_words(self):
        if self.lst:
            min_word_len = min(self.lst, key=len)
        res = list(filter(lambda x: len(x) == len(min_word_len), self.lst))
        return res

    def get_longest_words(self):
        if self.lst:
            max_word_len = max(self.lst, key=len)
        res = list(filter(lambda x: len(x) == len(max_word_len), self.lst))
        return res


texthandler = TextHandler()
texthandler.add_words('''Я помню чудное мгновенье
Передо мной явилась ты
Как мимолетное виденье
Как гений чистой красоты

В томленьях грусти безнадежной
В тревогах шумной суеты
Звучал мне долго голос нежный
И снились милые черты

Шли годы Бурь порыв мятежный
Рассеял прежние мечты
И я забыл твой голос нежный
Твои небесные черты

В глуши во мраке заточенья
Тянулись тихо дни мои
Без божества без вдохновенья
Без слез без жизни без любви

Душе настало пробужденье
И вот опять явилась ты
Как мимолетное виденье
Как гений чистой красоты

И сердце бьется в упоенье
И для него воскресли вновь
И божество и вдохновенье
И жизнь и слезы и любовь''')

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())"""


"""class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return self.name + ' ' + self.surname

    @fullname.setter
    def fullname(self, new_full_name):
        self.name, self.surname = new_full_name.split()


person = Person('Mike', 'Pondsmith')

person.fullname = 'Troy Baker'
print(person.name)
print(person.surname)"""


"""class Account:
    def __init__(self, login, password):
        self._login = login
        self._password = password




    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, change):
        raise AttributeError("Изменение логина невозможно")

    @property
    def password(self):
        def hash_function(password):
            hash_value = 0
            for char, index in zip(password, range(len(password))):
                hash_value += ord(char) * index
            return hash_value % 10**9
        return hash_function(self._password)




account = Account('hannymad', 'cakeisalie')

print(account.login)
print(account.password)"""


"""from functools import singledispatchmethod


class Formatter:

    @singledispatchmethod
    @staticmethod
    def format(obj):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @format.register(int)
    @staticmethod
    def _format(obj):
        print(f'Целое число: {obj}')

    @format.register(float)
    @staticmethod
    def _format(obj):
        print(f'Вещественное число: {obj}')

    @format.register(tuple)
    @staticmethod
    def _format(obj):
        unpacked_obj = ', '.join(map(str, obj))
        print(f'Элементы кортежа: {unpacked_obj}')

    @format.register(list)
    @staticmethod
    def _format(obj):
        unpacked_obj = ', '.join(map(str, obj))
        print(f'Элементы списка: {unpacked_obj}')

    @format.register(dict)
    @staticmethod
    def _format(obj):
        unpacked_obj = obj.items()
        print('Пары словаря:', ", ".join(map(str, unpacked_obj)))



Formatter.format({'Cuphead': 1, 'Mugman': 3})
Formatter.format({1: 'one', 2: 'two'})
Formatter.format({1: True, 0: False})"""


"""class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.program_name = "GenerationPy"
            cls._instance.environment = "release"
            cls._instance.loglevel = "verbose"
            cls._instance.version = "1.0.0"
        return cls._instance

config = Config()
print(config.__dict__)
print('program_name' in config.__dict__)
print('environment' in config.__dict__)
print('loglevel' in config.__dict__)
print('version' in config.__dict__)"""


"""class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        elif type(other) == tuple and len(other) == 2:
            return self.x == other[0] and self.y == other[1]
        else:
            return NotImplemented



vectors = [Vector(196, 21), Vector(102, 82), Vector(91, 28), Vector(137, 128), Vector(97, 69), Vector(79, 29), Vector(93, 62), Vector(85, 58), Vector(46, 176), Vector(84, 197)]
pairs = [(26, 86), (177, 150), (144, 175), (137, 128), (110, 196), (79, 29), (93, 62), (36, 158), (180, 24), (84, 167)]

for vector, pair in zip(vectors, pairs):
    print(vector == pair, vector != pair)"""


"""from functools import total_ordering

@total_ordering
class Word:

    def __init__(self, word):
        self.word = word

    def __repr__(self):
        return f'Word(\'{self.word}\')'

    def __str__(self):
        return f'{self.word.capitalize()}'

    def __eq__(self, other):
        if isinstance(other, Word):
            return len(self.word) == len(other.word)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Word):
            return len(self.word) < len(other.word)
        return NotImplemented


words = [Word('python'), Word('bee'), Word('geek')]

print(sorted(words))
print(min(words))
print(max(words))"""



"""from functools import total_ordering

@total_ordering
class Month:

    def __init__(self, year, month):
        self.year = year
        self.month = month

    def __repr__(self):
        return f'Month({self.year}, {self.month})'

    def __str__(self):
        return f'{self.year}-{self.month}'

    def __eq__(self, other):
        if isinstance(other, Month):
            return self.year == other.year and self.month == other.month
        elif type(other) == tuple and len(other) == 2:
            return self.year == other[0] and self.month == other[1]
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Month):
            if self.year < other.year: #and self.month < other.month
                return True
            elif self.year == other.year:
                if self.month == other.month:
                    return False
                elif self.month < other.month:
                    return True
            else:
                return False

        elif type(other) == tuple and len(other) == 2:
            if self.year < other[0]:
                return True
            elif self.year == other[0]:
                if self.month == other[1]:
                    return False
                elif self.month < other[1]:
                    return True
            else:
                return False
        return NotImplemented


month = Month(2023, 4)

print(month.__eq__(1))
print(month.__ne__(1.1))
print(month.__gt__(range(5)))
print(month.__lt__([1, 2, 3]))
print(month.__ge__({4, 5, 6}))
print(month.__le__({1: 'one'}))"""


"""from functools import total_ordering

@total_ordering
class Version:

    def __init__(self, version):
        self.version = str(version)

    def __repr__(self):
        if len(self.version) == 5:
            return f'Version(\'{self.version}\')'
        elif len(self.version) == 3:
            return f'Version(\'{self.version}.0\')'
        elif len(self.version) == 1:
            return f'Version(\'{self.version}.0.0\')'

    def __str__(self):
        if len(self.version) == 5:
            return f'{self.version}'
        elif len(self.version) == 3:
            return f'{self.version}.0'
        elif len(self.version) == 1:
            return f'{self.version}.0.0'

    def __eq__(self, other):
        if isinstance(other, Version):
            version_self = self.version.replace('.', '') #self.version.replace('.', '')
            version_other = other.version.replace('.', '') #other.version.replace('.', '')

            def __new_version_self(version_self):
                if len(version_self) == 1:
                    new_version_self = f'{version_self}00'
                    return new_version_self
                elif len(version_self) == 2:
                    new_version_self = f'{version_self}0'
                    return new_version_self
                else:
                    return version_self

            full_new_version = __new_version_self(version_self) # функция добавляющая нули, если их недостаточно

            def __new_version_other(version_other):
                if len(version_other) == 1:
                    new_version_self = f'{version_other}00'
                    return new_version_self
                elif len(version_other) == 2:
                    new_version_self = f'{version_other}0'
                    return new_version_self
                else:
                    return version_other

            full_new_version_other = __new_version_other(version_other)  # функция добавляющая нули, если их недостаточно


            if int(full_new_version[0]) == int(full_new_version_other[0]):
                return True
            elif int(full_new_version[1]) == int(full_new_version_other[1]):
                return True
            elif int(full_new_version[2]) == int(full_new_version_other[2]):
                return True
            else:
                return False
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Version):
            version_self = self.version.replace('.', '')
            version_other = other.version.replace('.', '')

            def __new_version_self(version_self):
                if len(version_self) == 1:
                    new_version_self = f'{version_self}00'
                    return new_version_self
                elif len(version_self) == 2:
                    new_version_self = f'{version_self}0'
                    return new_version_self
                else:
                    return version_self

            full_new_version = __new_version_self(version_self) # функция добавляющая нули, если их недостаточно

            def __new_version_other(version_other):
                if len(version_other) == 1:
                    new_version_self = f'{version_other}00'
                    return new_version_self
                elif len(version_other) == 2:
                    new_version_self = f'{version_other}0'
                    return new_version_self
                else:
                    return version_other

            full_new_version_other = __new_version_other(version_other)  # функция добавляющая нули, если их недостаточно

            #-----------------------------------------------------------------------------------

            if int(full_new_version[0]) < int(full_new_version_other[0]):
                return True
            elif int(full_new_version[1]) < int(full_new_version_other[1]):
                return True
            elif int(full_new_version[2]) < int(full_new_version_other[2]):
                return True
            else:
                return False
        return NotImplemented



versions = [Version('2'), Version('2.1'), Version('1.9.1')]

print(sorted(versions))
print(min(versions))
print(max(versions))"""


"""class Version:
    def __init__(self, version):
        self.version = version.split('.')
        self.version = [int(num) if num else 0 for num in self.version]

    def __str__(self):
        return '.'.join(str(num) for num in self.version)

    def __repr__(self):
        return f"Version('{str(self)}')"

    def __eq__(self, other):
        if isinstance(other, Version):
            return self.version == other.version
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Version):
            return self.version != other.version
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Version):
            return self.version > other.version
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Version):
            return self.version < other.version
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Version):
            return self.version >= other.version
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Version):
            return self.version <= other.version
        return NotImplemented

versions = [Version('2'), Version('2.1'), Version('1.9.1')]

print(sorted(versions))
print(min(versions))
print(max(versions))"""

"""from math import sqrt

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __int__(self):
        return int(sqrt((self.x**2) + (self.y**2)))

    def __float__(self):
        return float(sqrt((self.x**2) + (self.y**2)))

    def __complex__(self):
        return complex(self.x, self.y)



print(bool(Vector(1, 2)))
print(bool(Vector(1, 0)))
print(bool(Vector(0, 1)))
print(bool(Vector(0, 0)))"""


"""class Temperature:

    def __init__(self, temperature):
        self.temperature = temperature

    def __bool__(self):
        return self.temperature > 0

    def __int__(self):
        return int(self.temperature)

    def __float__(self):
        return float(self.temperature)

    def __str__(self):
        return f'{round(self.temperature, 2)}°C'

    def to_fahrenheit(self):
        return self.temperature * (9 / 5) + 32

    @classmethod
    def from_fahrenheit(cls, temperature):
        return (cls((temperature - 32) * (5 / 9)))


t = Temperature.from_fahrenheit(41)

print(t)
print(int(t))
print(float(t))
print(t.to_fahrenheit())"""


"""class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.lst_cart = (x, y, z)

    def __repr__(self):
        return f'Point({self.x}, {self.y}, {self.z})'

    def __iter__(self):
        yield from self.lst_cart


point = Point(1, 2, 3)
x, y, z = point

print(x, y, z)"""


"""class DevelopmentTeam:

    def __init__(self):
        self.lst_jun = []
        self.lst_sen = []

    def __iter__(self):
        yield from self.lst_jun
        yield from self.lst_sen

    def add_junior(self, *args):
        for i in args:
            self.lst_jun.append((i, 'junior'))

    def add_senior(self, *args):
        for i in args:
            self.lst_sen.append((i, 'senior'))


beegeek = DevelopmentTeam()

beegeek.add_junior('Timur')
beegeek.add_junior('Arthur', 'Valery')
print(*beegeek, sep='\n')"""


"""class AttrsIterator:

    def __init__(self, obj):
        self.obj = obj
        self.attrs = list(obj.__dict__.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.attrs):
            raise StopIteration
        red = self.attrs[self.index]
        self.index += 1
        return red

class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

user = User('Debbie', 'Harry', 77)
attrsiterator = AttrsIterator(user)

print(*attrsiterator)"""


"""class SkipIterator:

    def __init__(self, iterable, n):
        self.iterable = list(iterable)
        self.n = n
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.iterable):
            raise StopIteration
        reg = self.iterable[self.index]
        self.index += self.n + 1
        return reg


skipiterator = SkipIterator(iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5)

print(*skipiterator)"""


"""class RandomLooper:

    def __init__(self, *args):
        self.lst_args = []
        for x in args:
            self.lst_args.extend(x)
        self.args = self.lst_args
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        size_args = len(self.args)
        if self.index >= size_args:
            raise StopIteration
        res_elem = self.args[self.index]
        self.index += 1
        return res_elem

randomlooper = RandomLooper(['red', 'blue', 'green', 'purple'])

print(list(randomlooper))
print(list(randomlooper))"""




















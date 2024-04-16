# ZPRP

## Wykład 1
### Informacje organizacyjne:
* kontakt - przez maila w sprawach oficjalnych, inaczej na teams (w większości przypadków teams)
* update'y na galerze - może będą
* główne info na teamsach
* konsultacje zdalnie na teamsach, standardowy termin - środy 18-20, tak naprawdę można dowolny termin

#### Zaliczenie: można się tylko udupić

2 kolosy + projekt, najważniejszy projekt
PR do open source'a maxuje przedmiot, oraz napisanie artykułu naukowego na podstawie projektu też

kolosy - pkt z przedziału {-1, -0.75, -0.5, -0.25, 0}
W przypadku ocen x.25 w finale następuje zaokrąglenie w stronę korzystniejszej oceny.

Można się zwolnić z 2 kol. gdy projekt zostanie przyjęty przed 2 kolosem. no i trzeba mieć ocenę niegorszą niż -1, i też przelicznik pkt na wynik z 2 kol.

na końcu semestru można poprawić kolosa.


#### Projekty
* Michał Rokita - webdev
* Łukasz Neumann i szef - data science i AI

2 kol - 2 zajęcia od końca, 1 kol - po 6/7 wykładach.

projekty - zespoły 3 osobowe - [-3, 0.5] w inkrementacjach 0.25

##### Wymagania niefunkcjonalne projektu
- wysoka jakość kodu,
- reproduktowalność,
- rzetelność,
- zastosowanie nietrywialnych narzędzi

Docsy mają być, testy też, instrukcja, wszystko ma być bo wpierdol

Najpierw ma być design proposal - projekt projektu (3/4 tydzień zajęć):
* harmonogram projektu z podziałem na tygodnie i planowanymi postępami na tydzień (design proposal w jakimś markdownie),
* bibliografia,
* planowany zakres eksperymentów
* planowana funkcjonalność i tech stack

do 4 tygodnia zajęć (będzie termin)

po 3 tygodniach - status update

##### Wymagania ogólne:
* autoformatter np.black , linter,
* środowisko wirtualne,
* skrypty do budowania, testowania, uruchamiania aplikacji,
* dokumentacja,
* instrukcja użytkowania,
* PEP8*,



#### Część merytoryczna

```python
from dis import dis

dis(obj) # można dissasemblować kod napisany w pythonie np. funkcje, nie działa dla f. bibliotecznych (bo napisane w C)
```

Funkcje dodatkowe

```python
hash(float("-inf")) # zwraca hash nie zawsze taki sam, mutowalnych typów nie można zahashować
id(obj) # zwraca id obiektu w pamięci
```

Słownik - niehashowalny, mutowalny, podobnie jak zbiór (set)
klasa zdefiniowana przez użytkownika - jest hashowalna i mutowalna

klasy mają domyślnie zdefiniowane metody ```__eq__``` i ```__hash__```.
domyślny hash hashuje po ```id```

Hash woła ```object.__hash__```

aby zrobić, że klasa jest niehashowalna, trzeba nadpisać funkcję hash

```python
class A:
    __hash__ = None
```

Można też zdefiniować własną funkcję hashującą.
Nadpisując funkcje ```__eq__``` też klasa staje się niehashowalna.


Metody w klasie umożliwiają obsługę naszych klas fajnymi metodami:
```python
class A:
    def __len__(self): # Można wtedy wołać len(objekt)
        pass

    def __iter__(self): # można wołać iter(objekt)
        pass

    def __getitem__(self, idx): # można wołać objekt[i]
        pass
```

zliczanie obiektów
```python
from collections import Counter

# Counter zliczy obiekty w liście i stworzy słownik
# jeszcze jest most_common to zwróci posortowaną listę krotek
```

defaultdict
```python
from collections import defaultdict
d = defaultdict(list) # w arg factory
```

ChainMap

```from collections import ChainMap```
ChainMap - po kilku słownikach możemy przeiterować jakby były 1 mapowaniem
pozwala iterować i szukać kluczy

vars - zwraca metody i zmienne klasy

```python
class B:
    pass

b = B()

vars(b) # zwraca nic no bo to nic nie ma
b.x = 120
vars(b) # zwraca {'x': 120}
```

klasa deque z collections - kolejka dwustronna

```python
from collections import deque
```
gdy wrzucamy z dwuch stron deque jest znacznie szybsze niż defaultowa lista
jest bez wad


## Wykład 2
### Informacje organizacyjne cz.2
Nowa sala - 202 (bez informacji)

#### Dzisiejszy temat - obiektówka w Pythonie
Można sobie w ciele klasy zawołac jakąś funkcje no i pętle sobie pyknąć
W pętli można sobie utworzyć klasę, no ale tylko ostatnia przeżyje

```python
for _ in range(10):
    class A:
        pass

class A:
    print("Hello")

class A:
    for _ in range(10):
        print("Hello")
```

klasa w bebechach przypomina słownik

```python
class A:
    x = 0

a1 = A()
a1.x = 0
>>> a1.x
0
a1.x = 100
>>> a1.x
0
>>> a2.x
0
```

```python
def foo(a, b, /, c, *, d=100, e=200):
    pass
```

arg. pozycyjne - wymagane
te co mają wartość domyślną - opcjonalne
argumenty przed slashem - mogą być tylko pozycyjne - nie można ich podać przez = :

```python
foo(1, 2, 3) # zadziała
foo(a=1, b=2, c=3) # nie zadziała
```

to co między / a * może być pozycyjne i keyword, a to co po * jest tylko słownikowe
tzn. argumenty d, e trzeba podawać przez keyword:

```python
foo(d=10, e=20) # zadziała
```

#### Programowanie obiektowe
W Pythonie nie pisze się getterów i setterów, generalnie zmienne są wyeksponowane

Jednak collections.deque nie jest bez wad - zajmuje więcej pamięci niż zwykła lista (10 razy większy)

Można tworzyć kilka konstruktorów, dostępnych z ciała klasy,
zazwyczaj zaczynają się od słowa "from" np.

```python
from datetime import datetime
dict.fromkeys([*"abc"], 20)

# tworzenie tego świra
class Circle:
    @classmethod
    def from_bbd(cls, bbd):
        radius = bbd / 2.0 / math.sqrt(2.0) # compute the radius somehow
        return cls(radius)
```

Teraz można wołać:

```python
from circle import Circle

c = Circle.from_bbd(10)
```

od teraz pole musi być obliczone na podstawie obwodu... tarapaty

trick z dwoma podłogami:
żeby nie sypało się u ziomeczkow od opon po zmianie wyliczenia:

```python
import math

class Circle:
    def perimeter(self):
        return self.radius * math.pi * 2.0

    __perimeter = perimeter
```

Podwójna podłoga przed nazwą atrybutu:
name mangling - związanie nazwy klasy z nazwą atrybutu. __ przed atrybutem - prywatność wspierana przez język, _ przed atrybutem - prywatność przez konwencję. __ nie blokuje to w 100% zmiany atrybutu no bo mozna zmienić po prawdziwej nazwie, natomiast wiąże nazwę atrybutu z nazwą klasy


Nie możemy trzymać radius - co teraz?
Gettery i settery w sposób pythoniczny - zmiana jak działa '.' (np. w circle.radius)

```python
class Circle:
    """ Represents a Circle"""

    def __init__(self, radius):
        self.radius = radius

    # gettery i settery w pythonie - pythoniczny sposób (pojebana akcja). api jest takie same - można dobierać się do promienia, ale nie jest on przechowywany
    @property
    def radius(self):
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0
```

```
>>> c = Circle(10)
>>> c.radius
10.0
>>> c.radius = 20
>>> c
<__main__.Circle object at 0x7fa2bc095910>
>>> c.radius
20.0
>>> vars(c)
{'diameter': 40.0}
```

Można wykorzystać do stworzenia read-only property:

```python
>>> class A:
...     def __init__(self, a):
...             self._a = a
...     @property
...     def a(self):
...             return self._a
...
>>> a = A(10)
>>> a.a
10
```
Można ominąć i tak
```
>>> a.a = 30
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: can't set attribute
>>> a._a = 50
>>> a.a
50
```

#### Mała klaska, tylko z danymi
NamedTuple z modułu collections

```python
>>> import collections
>>> Point = collections.namedtuple('Point', ['x','y'])
>>> p = Point(10, 20)
>>> p.x
10
>>> p.y
20
>>> x, y = p
>>> x
10
>>> y
20
>>> p.x = 100
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: can't set attribute
>>>
```

niemutowalna, można rozszywać (jak krotka) + nazwane atrybuty

2 (nowszy) sposób - NamedTuple z modułu typing

```python
from typing import NamedTuple

class Color(NamedTuple):
    hue: int
    saturation: float
    lightness: float = 0.5
```

i wykorzystanie:

```
>>> Color
<class '__main__.Color'>
>>> c
Color(hue=33, saturation=1.0, lightness=0.5)
>>> c._replace(hue=20)
Color(hue=20, saturation=1.0, lightness=0.5)
>>> c._asdict()
{'hue': 33, 'saturation': 1.0, 'lightness': 0.5}
>>> tuple(c)
(33, 1.0, 0.5)
>>> h, s, l = c
>>> h
33
>>> s
1.0
>>> l
0.5
>>>
```

Moduł dataclasses:
W przeciwieństwie do NamedTuple dataclass jest mutowalne
daje za darmo ```__repr__```, ```__eq__```, niehaszowalność, porównywalność po atrybutach

```python
In [1]: from dataclasses import dataclass

In [2]: @dataclass
   ...: class Color:
   ...:     hue: int
   ...:     saturation: float
   ...:     lightness: float = 0.5
   ...:

In [3]: c = Color(33, 1.0)

In [4]: c
Out[4]: Color(hue=33, saturation=1.0, lightness=0.5)

In [5]: c.hue
Out[5]: 33

In [6]: c.saturation
Out[6]: 1.0

In [7]: from dataclasses import asdict, astuple

In [8]: asdict(c)
Out[8]: {'hue': 33, 'saturation': 1.0, 'lightness': 0.5}

In [9]: astuple(c)
Out[9]: (33, 1.0, 0.5)

In [10]: c
Out[10]: Color(hue=33, saturation=1.0, lightness=0.5)

In [11]: c.hue
Out[11]: 33

In [12]: c2 = Color(1, 2)

In [13]: c == c2
Out[13]: False
```

Co jak chcemy uczynić tą klasę sortowalną?

```python
@dataclass(order=True, frozen=True)
```

tworzone są dodatkowo metody eq, lt, le, ge, gt,
setattr i delattr zapewniają niemutowalność
można teraz zhashować tą dataklasę i nie jest mutowalna (frozen)

Potężna klasa employee z różnymi funkcjami:

```python
from dataclasses import dataclass, field
from dataclasses import fields
from datetime import datetime
from pprint import pprint

@dataclass(order=True, unsafe_hash=True)
class Employee:
    emp_id: int = field()
    name: str = field()
    gender: str = field()
    salary: int = field(hash=False, repr=False, metadata={"units": "BTC"})
    age: int = field(hash=False)
    viewed_by: list = field(default_factory=list, compare=False, repr=False)

    def access(self, viewer_id):
        self.viewed_by.append({viewer_id, datetime.now()})
```

## Wykład 3
Dekoratory i generatory

Dodatek: paczki cookiecutter - zawierają struktury pojektów do Flaska itp.
też do projektów data science'owych. Można zainstalować pipem/condą.
Umożliwia łatwiejszą pracę z projektem, analizę.

zmienne środowiskowe w osobnym pliku - ```.env```
można skorzystać z pakietu dotenv aby wczytać

### Generatory

Pętla for w pythonie to tak naprawdę wykorzystanie iteratora i wołanie next() aż dostaniemy wyjątek StopIteration.

iter() - zwraca obiekt, który implementuje next - można zaimplementować w klasie ```__next__```

```python
class Compute:
    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        rv = self.last
        self.last += 1
        if self.last > 10:
            raise StopIteration
        sleep(0.5)
        return rv
```
W takim wariancie przechowujemy tylko 1 wartość, oraz możemy szybciej uzyskać pierwszą wyliczoną wartość.
Można też skorzystać w pętli for z klasy.

Zamiast napisania tego tak manualnie można skorzystać z ```yield```.

```python
def compute_gen():
    for i in range(10):
        sleep(0.5)
        yield i
```
Generator - lazy fetch \
Na generatorach zaimplementowane zostało async io

```python
class Program:
    first(): ...
    second(): ...
    third(): ...
    def do_stuff:
        first()
        yield
        second()
        yield
        third()
        yield
```

Można też takie coś robić:
```python
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


def countdown(n):
    print(f"Starting countdown from {n}")
    while n > 0:
        yield n
        n -= 1
    print("Done")
```

Bardziej zaawansowany przykład:
Piszemy funkcję search(), która będzie miała api:
* search(fh, pattern, history)
* fh - filehandle
* pattern - wiadomka
* history - wiadomo

```python
from collections import deque

def search(lines, pattern, history=2):
    previous_lines = deque(max_len=history)

    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == "__main__":
    with open("some_file.txt", 'r') as fh:
        for line, prev_lines in search(fh, pattern="python", history=3):
            for prev_line in prev_lines:
                print(prev_line, end="")
            print(line, end="")
            print("-" * 20)
```

Na 1szym kol - takie coś mniej więcej ale 10 razy większe

Słówko yield zmienia funkcję w generator

isclice() z modułu itertools umożliwia sliceować generatory

### Dekoratory
Przeglądanie funkcji:

```
>>> add(0.5)
10.5
>>> add.__name__
'add'
>>> vars(add)
{}
>>> add.__module__
'__main__'
>>> add.__defaults__
(10,)
>>> add.__code__
<code object add at 0x7f39b6a2e3a0, file "w3_dec.py", line 1>
>>> add.__code__.co_code
b'|\x00|\x01\x17\x00S\x00'
>>> add.__code__.co_nlocals
2
>>> from inspect import getsource
>>> print(getsource(add))
def add(x, y=10):
    return x + y

>>>
```

Dekorator: rozszerzenie funkcji o dodatkową funkcjonalność.

```python
from time import perf_counter


def timer(func):
    def wrapper(*args, **kwargs):
        before = perf_counter()
        rv = func(*args, **kwargs)
        after = perf_counter()
        print("Time taken: ", after - before)
        return rv
    return wrapper


@timer
def add(x, y=10):
    return x + y

@timer
def sub(x, y=10):
    return x - y
```
Wyniki:

```
Time taken:  8.090000847005285e-07
add(10) 20
>>> sub(10)
Time taken:  4.188999810139649e-06
0
>>> @timer
... def hello():
...     print("hello")
...
>>> hello()
hello
Time taken:  0.00017305599976680242
>>> def x(a, b, c, d=10, e=20): return a+b+c+d+e
...
>>> @timer
... def x(a, b, c, d=10, e=20): return a+b+c+d+e
...
>>> x(1, 2, 3)
Time taken:  2.368000423302874e-06
36
>>>
```

Jednak opakowanie trochę popsuło funkcję - nie widzimy już nazwy i docstringa.
Aby naprawić - dodajemy dekorator functools.wraps

```python
def timer(func):
    @functools.wraps(func) # aby uniknąć przesłonięcia tej nazwy funkcji
    def wrapper(*args, **kwargs):
        before = perf_counter()
        rv = func(*args, **kwargs)
        after = perf_counter()
        print("Time taken: ", after - before)
        return rv
    return wrapper
```

Dekorator, który będzie wykonywał funkcję n razy.

```python
def ntimes(n): # dekorator ntimes
    def inner(func):
        @functools.wraps(func) # aby zachować nazwę i doc funkcji (ogólnie dane o funkcji)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                print(f"Running {func.__name__}")
                rv = func(*args, **kwargs)
            return rv
        return wrapper
    return inner
```

Dekorator cache'ujący:

```python
import functools
# w functools jest defaultowo dekorator cache - functools.cache
# istnieje też lru_cache - można ustalić liczbę zapisywanych wartości, domyślnie 128 miejsc

def cached(func):
    saved = {} # można dorobić atrybut w dekoratorze i modyfikować go

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = args + tuple(kwargs.items())
        if key not in saved:
            saved[key] = func(*args, **kwargs)
        return saved[key]
    wrapper.cache = saved # fukcja może mieć atrybuty - jak klasa, dzięki temu możemy podpiąć ten cache do funkcji
    return wrapper

@cached
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)
```

W pakiecie functools istnieje już functools.cache i functools.lru_cache

## Wykład 4
### Dodatek do w3 - dekoratory

Dobre info o dekoratorach na stronie [real python 101](https://realpython.com/primer-on-python-decorators/)

Szablon dekoratora

```python
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
```

Dekoratory z opcjonalnymi argumentami - trzeba trochę pocwaniaczyć.
Funkcja przekazywana do dekoratora jest już opcjonalnym argumentem. Potem * - tylko keywordy
Jeśli f. nie została podana - zwracamy funkcje. Jeśli została podana - dekorator od funkcji.

```python
def name(_func=None, *, key1=value1, key2=value2, ...):
    def decorator_name(func):
        ...  # Create and return a wrapper function.

    if _func is None:
        return decorator_name
    else:
        return decorator_name(_func)
```

Używanie klas jako dekoratorów - jeśli zaimplementujemy metodę ```__call__``` to wtedy można wywoływać klasę jak funkcję. Za pomocą dekoratorów można też zaimplementować singleton.

### Przepis Johna Pythona na przeładowanie metod
W Pythonie w zasadzie nie ma przeładowania metod - ale można wykorzystać dekorator ```@multimethod```,
zaimplementowany wykorzystując generator expression (szybsze niż lista)
generator expression - list comprehension ale bez klamerek np.

```python
nums = [1, 2, 3, 4, 5]
sum([n ** 2 for n in nums]) # tworzy listę i sumuje
sum(n ** 2 for n in nums) # generator expression - szybsze
```

ale wracając do dekoratora multimethod - jest w blogu Van Rossuma

można dostać się do type hintów funkcji za pomocą ```__annotations__```


### Co zamiast ifów?
Zamiast zagłębionych ifów - and
sprawdzanie kilku warunków w kolekcji - można wykorzystać all() i any()

```python
if a == 12 and b == 17 and c == 24 and d == 42: # słabo
# lepiej:
if a in {12, 17, 24, 42}: # dobrze
```

Operacje na zbiorach w pythonie - fajne

```python
>>> nums = {1, 2, 3, 4, 5, 6, 7}
>>> evens = {2, 4, 6}
>>> evens.issubset(nums)
True
>>> evens.issuperset(nums)
False
>>> nums.issuperset(evens)
True
>>> nums.isdisjoint(evens) # sprawdza, czy zbiory nie mają przecięcie - zwraca False jak nie mają
False
>>> other = {120, 428}
>>> nums.isdisjoint(other)
True
>>>
```


### Itertools
* Ciekawe ćwiczenie do zrobienia - samemu zaimplementować itertools.patched, itertools.permutations itp.


### Bazy danych
Wbudowany w bibliotekę standardową mechanizm pracy z sqlite
```python
import sqlite3

conn = sqlite3.connect("demo.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Charlie", 22))
conn.commit()
conn.close()
```

Można korzystać z context managera:

```python
with sqlite3.connect("demo.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
```

Baza danych w pamięci - bez pliku:

```python
con = sqlite3.connect(":memory")
cur = con.execute("CREATE TABLE lang(name, first_appeared)")

data = (
    {"name": "C", "year": 1972},
    {"name": "Fortran", "year": 1957}
)
```

### Menedżery kontekstu
Trzeba zaimplementować ```__enter__``` i ```__exit__```

```python
from sqlite3 import connect

class Temptable:
    def __init__(self, cur):
        self.cur = cur

    def __enter__(self):
        cur.execute("CREATE TABLE points (x INTEGER, y INTEGER)")

    def __exit__(self, exc_type, exc_value, tb): # typ wyjątku, wartość wyjątku
        cur.execute("DROP TABLE points")
```

Wtedy wykorzystanie:

```python

with connect("points.db") as conn:
    cur = conn.cursor()
    with Temptable(cur):
        cur.execute("INSERT INTO points VALUES (1, 2)")
        cur.execute("INSERT INTO points VALUES (1, 1)")
        cur.execute("INSERT INTO points VALUES (2, 2)")
        for row in cur.execute("SELECT x, y FROM points"):
            print(row)

        for row in cur.execute("SELECT sum(x + y) FROM points"):
            print(row)
```

to jest po prostu generator

```python
def temptable(cur):
    cur.execute("CREATE TABLE points (x INTEGER, y INTEGER)")
    yield
    cur.execute("DROP TABLE points")


class Temptable:
    def __init__(self, cur):
        self.cur = cur

    def __enter__(self):
        self.gen = temptable(self.cur)
        next(self.gen)

    def __exit__(self, exc_type, exc_value, tb): # typ wyjątku, wartość wyjątku
        next(self.gen, None)
```

Uogólniona wersja kodu:

```python
from sqlite3 import connect


class ContextManager:
    def __init__(self, gen):
        self.gen = gen

    def __call__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        return self

    def __enter__(self):
        self.gen_instance = self.gen(*self.args, **self.kwargs)
        next(self.gen_instance)

    def __exit__(self, exc_type, exc_value, tb): # typ wyjątku, wartość wyjątku
        next(self.gen_instance, None)


@ContextManager
def temptable(cur):
    cur.execute("CREATE TABLE points (x INTEGER, y INTEGER)")
    yield
    cur.execute("DROP TABLE points")


with connect("points.db") as conn:
    cur = conn.cursor()
    with temptable(cur):
        cur.execute("INSERT INTO points VALUES (1, 2)")
        cur.execute("INSERT INTO points VALUES (1, 1)")
        cur.execute("INSERT INTO points VALUES (2, 2)")
        for row in cur.execute("SELECT x, y FROM points"):
            print(row)

        for row in cur.execute("SELECT sum(x + y) FROM points"):
            print(row)
```

Zamiast pisania tego wszystkiego można wykorzystać pakiet contextlib

```python
@contextmanager
def temptable(cur):
    cur.execute("CREATE TABLE points (x INTEGER, y INTEGER)")
    yield
    cur.execute("DROP TABLE points")
```

Ogólnie:

```python
@contextmanager
def f():
    try:
        yield
    finally:
        yield
```

Można poczytać o tym talki Jamesa Powella

### *args, **kwargs

args - argumenty nienazwane, kwargs - nazwane (key word arguments)


## Wykład 5
### kolejka

Pakiet heapq

kolejka podobna do ```sorted``` ale mogą być przypadki gdzie heapq lepsze, wydajniejsze


```python
import heapq

nums = [1, 8, 2, -4, 5, -7, 22, 33, 4, 38]

print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))
```

Można też sortować takie struktury:

```python
portfolio = [
    {"name": "IBM", "shares": 100, "price": 91.1},
    {"name": "GOOGL", "shares": 76, "price": 543.2},
    {"name": "FB", "shares": 42, "price": 73.2},
    {"name": "ACME", "shares": 167, "price": 143.65},
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s["price"])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s["price"])
```

Lambda - nienazwana funkcja, której z reguły chcemy uzyć w 1 miejscu i o niej zapomnieć

heapq:
nlargest i nsmallest działają dobrze przy małej ilości elementów, do 1 elementu min i max

kolejka priorytetowa z heapq:

```python
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, ((-priority), self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]
```


### Testowanie
#### Doctest
Pokazuje użytkownikowi jak używać funkcji
testują kod
interpreter parsuje test w docstringu
Wywołanie:
```bash
python3 -m doctest square.py -v # -v - verbose, wypisuje output testów na terminal
```

Przykład w kodzie:
```python
def square(x):
    """
    Squares the input.

    >>> square(2)
    4
    >>> square(-2)
    4
    """
    return x * x
```

W zasadzie bezkosztowe testowanie kodu w pythonie
info w dokumentacji Pythona

mypy - narzędzie do statecznego testowania typów w pythonie
(oddzielne narzędzie - można dodać do potoku CI)

type hinty
dużo w module typing

z ciekawych:
```python
from typing import TypeVar, Generic, List, Callable # w 3.10 i wyżej list wspierane zamiast List

T = TypeVar("T")


def filter_list(items: List[T], condition: Callable[[T], bool])
    ...
```

#### Pytest

Jakieś fajne featury pytesta

są wtyczki do Django, Flaska
minusy - dziwna składnia

fixture - dynks (xdd)

```@pytest.fixture``` - wstrzykiwanie obiektu do wszystkich testów


```python
from dataclasses import dataclass
import pytest

@dataclass
class User:
    name: str
    age: int

    @property
    def nickname(self):
        return f"{self.name.lower()}{self.age}"


# Dla uproszczenia testy w tym samym pliku

@pytest.fixture
def user_instance():
    return User("John", 42)


def test_user_nickname_typical(user_instance):
    assert user_instance.nickname == "john42"
```

Taki fixture reużywalny do wszystkich testów

Jak wpiszemy fixture'y w pliku conftest.py to pytest automatycznie będzie rozpoznawał i importował

```bash
pytest -v # verbose - więcej info
pytest --fixtures # podaje dostępne fixture'y
pytest -s # można przechwytywać output z testów
pytest -k # można wywołać 1 test po sygnaturze
```

Zazwyczaj fixture'y jedną z 3 postaci
- realizują logikę
- tworzą obiekty i zwracają
- trochę jak manadzer kontekstu - setup teardown

Przykładowy fixture typu 3:

```python
@pytest.fixture
def temporary_dir(): # juz istnieje ale na testa piszemy fixture co tworzy tymczasowy katalog
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir
```

dekorator @pytest.mark

markery można zarejestrować w pliku pytest.ini
można wywoływać testy według markerów - które markery robimy, które markery nie

Testy sparametryzowane

```python
@pytest.mark.parametrize(
    ("input_n", "expected"),
    [
        (1, 1),
        (-1, 1),
        (2, 4),
        pytest.param(-2, 4, id="negative case"), # w parametryzacji można dodawać nazwy
        Case(input_n=0, expected=0),
        ]
)
def test_square_integers(input_n, expected):
    assert square(input_n) == expected


@pytest.mark.parametrize(
    "input_n",
    [
        "a",
        {},
        [],
    ]
)
def test_square_error(input_n):
    with pytest.raises(TypeError):
        square(input_n)
```

Wtyczka do pytesta - `pytest-benchmark`
Benchmark alokuje ilość czasu na dany test - i sprawdza ile razy wykona fragment kodu

```python
@pytest.fixture
def concat_data():
    destination_list = list(range(10000))
    source_list = list(range(1000, 8000))
    result = list(range(1500, 8000)) + list(range(6500, 10000))
    return destination_list, source_list, result


def test_naive_concatenate(concat_data, benchmark):
    assert benchmark(naive_concatenate, *concat_data[:2], 0, 500) == concat_data[-1] # asercja , czy wynik fcji jest taki jak powinien
    # do f concatenate wstrzykuję 2 elementy tej krotki (destination i source ) oraz offset i offset
```
Nie za dużo kodu a daje statystyki do porównania wydajności
Można wyłączyć:
```shell
pytest -v --benchmark-disable
```
Wtedy wywoła każdy test 1 raz

Inne wtyczki:
* `pytest-coverage` - do obliczenia pokrycia kodu testami
* `pytest-html` - generuje raporty w htmlu z pokrycia testami

```shell
pytest --cov --cov-report=html
```
Inne paradygmaty testowania (nie jednostkowe).
Property based testing - testowanie oparte na własnościach

`reduce` z `functools` - redukuje sekwencję do akumulatora (z paradygmatu funkcyjnego)

Domyślnie hypothesis generuje 100 przypadków testowych - testuje różne typy danych, nietrywialne przypadki
dekoratory:
* `example` - przykładowy przypadek
* `settings` - dodatkowe ustawienia, może być `max_examples` np. = 500, wtedy 500 przypadków

```shell
pytest -v -s --hypothesis-show-statistics
```
Statystyki do testów, ile exampli przeszło, ile nie itp.
```shell
pytest -v -s --hypothesis-show-statistics --verbosity=debug
```
Wtedy dostaniemy wszystkie przypadki jakie zostały wygenerowane

Można też samemu definiować strategię generowania obiektów klas do testów.

Ciekawy przykład w `test_quadratic.py`
<!-- TODO: add link -->

Mutation testing - fault injection
Dodawanie błędów i sprawdzanie jak aplikacja jest na nie odporna. Tworzone mutanty - kod modyfikowany (np. podmiana operatorów) i sprawdzanie jak da radę. Celowo wstrzykujemy błędy i sprawdzamy, czy testy "zabiją" mutanta (czy wywalą popsuty kod).
Przykładowe narzędzie - `mut.py` - nie aż tak popularne (300 gwiazdek).
Inny framework - `cosmicray`.

Uogólniona wersja mutation testowania - `fuzzing` - może być motyfikacja bytecodu Pythona czy dla innych języków skompilowanego kodu.
Przykładowe narzędzie - `Atheris` od Google.

## Wykład 6
### Zarządzanie pakietami, projektem

Dzisiaj z Neumannem
Jak zarządzać projektem pythonowym itp.
[slajdy](https://staff.elka.pw.edu.pl/~lneumann/python_packaging.pdf)

Relevant xkcd

rye - nie jest production ready ale ciekawe narzędzie, najmniej pisania kodu

plik ```pyproject.toml``` dane o pakietach itp.

```pairwise``` w itertoolsach - sliding window, kiedyś by się przydało

za pomocą rye możemy zarządzać pakietami, dzielić na środowiska (np. dodać pytesta tylko do dev, no bo na produkcji wywalone) i zbudować projekt

rich - preview
biblioteka do pracy z narzędziamy cli
można sobie progress bara dodać (pewnie wgl inne rzeczy też na razie to tyle)

kontynuując rye:
opcjonalne pakiety

```bash
rye publish
```
nasz pakiet zostaje publikowany na pipa i wtedy można normalnie zainstalować nasz pakiecik pipem (pip install)

### Zarządzanie wersją Pythona
Nie warto instalować pakietów do systemowej wersji Pythona, jak się zrobi syf to niektóre narzędzia systemu mogą przestać działać

Przykładowe narzędzia do zarządzania wersją Pythona:
* Pyenv
* rye
* hatch
* conda (ale to trochę inna bestia)

### Importowanie w Pythonie

- Moduł
  * Pojedynczy plik ```.py```
- Pakiet
  * katalog z plikiem ```__init__.py```, który może być pusty

W dokumentacji Pythona dobry [tutorial](https://docs.python.org/3/tutorial/modules.html)

Jak działa import?
* korzysta po kolei z tzw. importerów z ```sys.meta_path```
* jednym z nich jest PathFinder, który korzysta z ```sys.path```

[dokumentacja o tych pathach](https://docs.python.org/3/library/sys_path_init.html)

Można modyfikować ```sys.path```

### Środowiska wirtualne

Narzędzia do tworzenia i zarządzania środowiskami wirtualnymi
* Wbudowany moduł ```venv```
* Nakładna na ```venv``` - ```virtualenv```, rekomendacja by używać ```virtualenv``` zamiast ```venv``` (szybsze, potężniejsze)
* ```uv```
* ```pipenv``` - podobny do ```uv```

### Jak instalować pakiety?
```bash
pip install numpy # i prayge
```

W globalnym środowisku może próbować nadpisać
Teraz już zaczynają być obostrzenia, żeby nie instalować na systemowym Pythonie.

Alternatywy:
* ```uv```
* ```pipenv```
* ```poetry```
* ```hatch```
* ```rye```

Przy instalacji pakietów można specyfikować wersję (np. SomePackage >= 1.3), podać konkretną (SomePackage == 1.3), dodawać feature'y (SomePackage[feature1, feature2])

Jak instalować wykonywalne narzędzia Pythonowe?
Za pomocą systemowego managera pakietów (Ubuntu - ```apt```) lub ```pipx```
Automatyczne zarządzanie wirtualnym środowiskiem per narzędzie

### Jak specyfikować zależności?
- Plik ```requirements.txt```
  * Lista pakietów, 1 na linię
  * różne grupy zależności - kilka plików ```requirements.txt```
- Plik ```pyproject.toml```
  * składnia tomlowa
  * podział pakietów na grupy zależności
W ```pyproject.toml``` można dużo napisać (urle projektu, dependecies, optional dependencies, ścieżka do readme, licencji itp.)


### Dependency resolution
Co się dzieje pod spodem jak piszemy ```pip install```?
Wersje poszczególnych zależności nie mogą być ze sobą w konflikcie.

Większość narzędzi do rozwiązywania zależności robi to dla konkretnej wersji Pythona i środowiska (OS)
Obecnie wyjątkiem są narzędzia ```poetry``` i ```pdm```

### Lockfile
- Czasem długo trwa ściąganie pakietu
  * nie da się dostać do zależności pakietu bez ściągnięcia go w całości, uciążliwe jak są pakiety mające duże pliki binarne (numpy)
  * przy wielu niekompatybilnych wersjach pakietów w zależności od algorytmu
    rozwiązywania zależności trzeba sprawdzić wiele różnych wersji zanim trafi się w
    taką, która spełnia wszystkie wymagania
- Standardowo po rozwiązaniu wersji zależności zapisuje się je wraz z metadanymi do tzw. lockfile'a
  * W metadanych oprócz wersji zależności mogą być przechowywane np. wartości
    funkcji skrótu dla plików pakietu, a także informacja jakie zależności ma dany pakiet
- Obecnie w Pythonie nie ma ustandaryzowanego formatu Lockfile, więc różnią się
one w zależności od narzędzia, które go wygeneruje

Generowanie lockfile
- za pomocą ```pip freeze```
- przy użyciu narzędzia np.
  * ```pdm```
  * ```pipenv```
  * ```poetry```
  * ```rye```
- należy wrzucić lockfile'a na repozytorium - umożliwi to reproduktowalność środowiska, zakładając że ten sam OS

### Pakiety SDIST - source distribution
* Zawiera wszystkie pliki, które są potrzebne do zainstalowania i przetestowania
pakietu
* Przypomina środowisko deweloperskie

Pakiety Wheel
* Zawirają wszystkie pliki potrzebne do zainstalowania pakietu

```distutils``` - prehistoria budowania pakietów
* 2000 r.
* moduł deprecated w Pythonie 3.10, usunięty w 3.12
* moduł biblioteki standardowej
* programista pisał w Pythonie kod do budowania swojego pakietu

```setuptools``` - supercharged distutils
* 2004 r.
* lepsze ```distutils```, wiele usprawnień
* wraz z ```packaging``` reimplementuje ```distutils```
* używa się w ```setup.py```
* przez lata standard budowania pakietów
* nadal można korzystać, część projektów nadal korzysta z ```setuptools```

```flit``` - deklaratywne budowanie pakietów
* używanie Pythonia do budowania Pythona - nie taki dobry pomysł
* dzięki temu mamy pyproject.toml i inne narzędzia tego typu

### Budowanie pakietów - podział na frontend i backend
Backend - buduje pakiet w odizolowanym środowisku
* ```setuptools```
* ```flit```
* ```poetry```
* ```pdm```
* ```hatchling ( hatch )```
Frontend - inicjalizuje środowisko i mówi backendowi żeby robił paczkę
* ```build```
* ```poetry```
* ```pdm```
* ```rye```
* ```pip```
* ```tox```

w `pyproject.toml` można zdefiniować konfigurację backendu.

### Jak opublikować pakiet?
* Trzeba założyć konto na PyPi i użyć jednego z narzędzi

### SOTA: jedno narzędzie do wszystkiego
- Obecnie jest ich kilka (kombajnów)
- [Porównianie](https://github.com/pdm-project/pdm#comparisons-to-other-alternatives) - brakuje `rye`
- Kilka najpopularniejszych narzędzi:
  * `pdm`
  * `poetry`
  * `rye` - nie jest production ready
  * `hatch`

`poetry` nie pozwala na specyfikację backendu - korzysta ze swojego oraz trzyma metadane w tablicy `[tool.poetry]` zamiast ustandaryzowanej reprezentacji w `pyproject.toml` (PEP621)


Na kolosie trzeba będzie użyć jeden z tych menedzerów pakietów i zbudować taki projekt i nim zarządzać.
def add(x, y):
    return x + y


class Adder:
    def __call__(self, x, y):
        return x + y


from time import sleep


def compute():
    values = []
    for i in range(10):
        sleep(0.5)
        values.append(i)
    return values


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


def compute_gen():
    for i in range(10):
        sleep(0.5)
        yield i


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

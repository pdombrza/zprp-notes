from sqlite3 import connect
from contextlib import contextmanager


# class ContextManager:
#     def __init__(self, gen):
#         self.gen = gen

#     def __call__(self, *args, **kwargs):
#         self.args, self.kwargs = args, kwargs
#         return self

#     def __enter__(self):
#         self.gen_instance = self.gen(*self.args, **self.kwargs)
#         next(self.gen_instance)

#     def __exit__(self, exc_type, exc_value, tb): # typ wyjątku, wartość wyjątku
#         next(self.gen_instance, None)


# @ContextManager
# def temptable(cur):
#     cur.execute("CREATE TABLE points (x INTEGER, y INTEGER)")
#     yield
#     cur.execute("DROP TABLE points")

@contextmanager
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

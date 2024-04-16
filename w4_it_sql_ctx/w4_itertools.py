import itertools

filenames = ["filename1.txt", "filename2.txt"]
modes = ["r", "w", "a"]
encodings = ["utf-8", None, "latin-1"]

product = list(itertools.product(filenames, modes, encodings))

actions = ["play", "stop", "reject", "rewind"]
permutations = list(itertools.permutations(actions))

colors = ["red", "blue", "green"]
print(list(itertools.combinations(colors)))

# Ciekawe ćwiczenie do zrobienia - samemu zaimplementować itertools.patched, itertools.permutations itp.

from collections import ChainMap

environ = {"a": "path", "b": "os", "c": "test"}

defaults = {"color": "red", "user": "guest"}


# ChainMap - po kilku słownikach możemy przeiterować jakby były 1 mapowaniem

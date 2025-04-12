import contextlib


@contextlib.contextmanager
def eggs():
    yield 42

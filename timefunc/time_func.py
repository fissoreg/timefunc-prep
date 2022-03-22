import timeit

def time_func(func, *args, number = 1, repeat = 1, gc = False):
    """Measure the execution time of `func(*args)`.

    Keyword arguments:
    number -- how many times to execute `func(*args)` for a single measurement
    repeat -- how many measurements
    gc     -- If `True`, disables the garbage collector.
    """
    stmt = 'func(*args)'
    t = timeit.Timer(stmt, 'import gc; gc.enable()' if gc else '',
                     globals=locals())
    t.timeit(number = 1) # warming-up: compilation time
    return t.repeat(repeat = repeat, number = number)
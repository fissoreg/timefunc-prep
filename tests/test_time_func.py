from timefunc.time_func import time_func

def loop(x):
    for _ in range(x):
        pass

def test_no_args():
    time_func(print)

def test_single_arg():
    time_func(loop, 1_000_000)
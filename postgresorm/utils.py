from time import perf_counter


class BadFetch(Exception):
    def __init__(self, thread_num: int, call_num: int):
        self._thread_num = thread_num
        self._call_num = call_num

    def __str__(self):
        return f"Bad fetch in thread {self._thread_num}; call number = {self._call_num}"


def time_counter(func):
    """Marks the time, required to execute given function"""
    def time_counter_wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        time_taken = perf_counter() - start
        print(f"Function {func} ended in {time_taken} s")
        return result

    return time_counter_wrapper

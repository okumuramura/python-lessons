import time

def timeit(repeat=10):
    def decorator(f):
        def wrapper(*args, **kwargs):
            start = time.time()
            for _ in range(repeat):
                result = f(*args, **kwargs)
            end = time.time()
            total = (end - start) / repeat
            print(f'{f.__name__}: {total:.3f} sec')
            return result

        return wrapper
    return decorator


@timeit(repeat=10)
def factorial(n):
    res = 1
    for i in range(n, 0, -1):
        res *= i
    return res


factorial(50000)

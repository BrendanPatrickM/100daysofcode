import time
current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapper():
        start_time = time.time()
        function()
        complete_time = time.time()
        speed = complete_time - start_time
        print(f'{function.__name__} run speed: {speed}')
    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()

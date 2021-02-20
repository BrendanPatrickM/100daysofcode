from time import sleep


def delay_decorator(function):
    def wrapper():
        sleep(2)
        function()
        function()
        function()
    return wrapper


@delay_decorator
def hello():
    print('hello')




hello()
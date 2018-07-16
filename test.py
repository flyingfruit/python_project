# -*- encoding=UTF-8 -*-


def log(test):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(test)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log('试一下')
def hello():
    print('cc')


if __name__ == '__main__':
    hello()

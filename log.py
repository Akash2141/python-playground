from collections.abc import Callable
from functools import wraps

def toLog(message:str):
    def log_wrapper(func):
        @wraps(func)
        async def log(*args, **kwargs):
            print(f"func started {func.__name__} {message}")
            result= await func(*args, **kwargs)
            print(f"func ended {func.__name__} {message}")
            return result
        return log
    return log_wrapper


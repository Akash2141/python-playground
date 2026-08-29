from collections.abc import Callable
from functools import wraps

def toLog(message:str):
    def log_wrapper(func):
        @wraps(func)
        async def log(*args, **kwargs):
            print(f"func started {message}")
            result= await func(*args, **kwargs)
            print(f"func ended {message}")
            return result
        return log
    return log_wrapper


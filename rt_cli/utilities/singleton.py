from typing import Any

class Singleton(type):
    ''' Singleton Metaclass.'''

    __instance = None

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwds)

        return cls.__instance
            

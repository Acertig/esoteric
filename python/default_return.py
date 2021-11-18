def default_return(value = None): 
    def factory(func): 
        def inner(*args, **kwargs): 
            if func(*args, **kwargs) is None: 
                func.__code__ = func.__code__.replace(co_consts = (value, *func.__code__.co_consts[1::]))
                return func(*args, **kwargs)
            return func(*args, **kwargs)
        return inner
    return factory

@default_return(value = "acertig")
def test(): 
    pass

print(test())

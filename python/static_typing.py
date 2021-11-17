import typing 

def static_typing(**options): 
    def factory(func): 
        def inner(*args, **kwargs): 
            
            if not args: 
                return 
            
            custom_exception = options.get("custom_exception", TypeError)
            convert = options.get("convert", False)
            
            type_hints = typing.get_type_hints(func)
            
            if (return_type := type_hints.get("return")): 
                classes = list(type_hints.values())[:-1]
            else: 
                classes = type_hints.values()
            
            post_args = [*args[:len(classes)]]
            
            for cls, arg in zip(classes, post_args): 
                if convert: 
                    try: 
                        arg = cls(arg)
                    except: 
                        continue
                else: 
                    if not isinstance(arg, cls): 
                        raise custom_exception(f"{arg} is not type {cls}")
            
            if (return_value := func(*post_args, **kwargs)) and return_type and not convert: 
                if not isinstance(return_value, return_type): 
                    raise custom_exception(f"return value is not type {return_type}")
            elif convert: 
                try: 
                    return_value = return_type(return_value)
                except: 
                    pass
                            
            return return_value
        return inner
    return factory

@static_typing(convert = True, custom_exception = TypeError)
def test(arg1: int, arg2: str, *args, **kwargs) -> int: 
    return "5"

test(1, 2, 1, 2)


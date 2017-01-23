def f_wrapper(func):
    print("Hello from f_wrapper")
    fibo_cache = {}
    
    def wrapper(*args, **kwargs):
        n = args[0]
        
        if n not in fibo_cache:
            fibo_cache[n] = func(*args, **kwargs)

        return fibo_cache[n]
    return wrapper

@f_wrapper
def f ( n ):
    global global_iterator

    global_iterator = global_iterator + 1
    if n <= 1: 
        return n

    return f(n-1)+f(n-2)

global_iterator = 0

print(f(10))
print(global_iterator)

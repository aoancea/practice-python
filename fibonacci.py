def f ( n ):
    global global_iterator

    global_iterator = global_iterator + 1
    if n <= 1: 
        return n

    return f(n-1)+f(n-2)

global_iterator = 0

print(f(10))
print(global_iterator)

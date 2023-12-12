def productFib(prod):
    fib1, fib2 = 0, 1
    while fib1 * fib2 < prod:
        fib1, fib2 = fib2, fib1 + fib2
    if fib1 * fib2 == prod:
        return [fib1, fib2, True]
    else:
        return [fib1, fib2, False]

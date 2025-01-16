calculations = 0

def fibonacci(n): # O(2^n)
    global calculations
    calculations += 1
    if n < 2:
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Normal: ", fibonacci(35))
print("Normal No of Calculations: ", calculations)

m_calculations = 0
def fibonacciMaster():
    cache = {}
    def fib(n):
        global m_calculations
        m_calculations += 1
        if n in cache:
            return cache[n]
        else:
            if n < 2:
                return n
            else:
                cache[n] = fib(n - 1) + fib(n - 2)
                return cache[n]
            
    return fib

fasterFib = fibonacciMaster()
print("DP: ", fasterFib(35))
print("DP No of Calculations: ", m_calculations)


"""
m_calculations = 0
def fibonacciMaster(): # O(n)
    cache = {}
    def fib(n):
        global m_calculations
        m_calculations += 1

        if n in cache:
            return cache[n]
        else:
            if (n < 2):
                return n
            else:
                cache[n] = fib(n - 1) + fib(n - 2)
                return cache[n]
            
    return fib
"""
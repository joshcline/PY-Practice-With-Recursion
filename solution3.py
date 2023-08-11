# Write code for algorithm 3 below
def nth_fibbonacci(n):
    if n <= 0:
        print("Incorrect Input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return nth_fibbonacci(n-1)+nth_fibbonacci(n-2)
    
print("2nd fib number:")
print(nth_fibbonacci(2))
print("3rd fib number:")
print(nth_fibbonacci(3))
print("4th fib number:")
print(nth_fibbonacci(4))
print("5th fib number:")
print(nth_fibbonacci(5))
print("6th fib number:")
print(nth_fibbonacci(6))
print("7th fib number:")
print(nth_fibbonacci(7))
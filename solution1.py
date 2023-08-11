# Write code for algorithm 1 below
def count_down(n):
    # Base Case
    if n==0:
        return
    
    # Recursive Case
    else:
        print(n)
        count_down(n-1)

# Test Case
n=8
count_down(n)
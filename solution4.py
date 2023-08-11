# Write code for algorithm 4 below
def power_of(a,b):
  if b < 1:
    print("Invalid Input")
  elif b == 1:
    return a
  else:
    return a * power_of(a, b-1)
  
print("2^4:")
print(power_of(2,4))
# Mark Cotter, 2019-01-31
# Calculates the factorial of a number of a positive integer
# Change the starting value of i to get a different factorial

i = 5
ans = 1

# Checks if i is a positive integer
if i <= 0:
    print(i, "is not a positive integer")

# Calculates the factorial of a positive integar
else:
    print("Calculating the factorial of",i)
    while i > 1:
        ans = ans * i
        i = i - 1

# Prints the resulting factorial       
    print("The factorial is",ans)

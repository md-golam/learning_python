# for loop
# sum = 0
# for i in range(100, 13, -2):
#     print(f" current value is {i**2}")
#     sum += i**2
#     print(f"current sum is {sum}")


# print(f"total sum is: {sum}")
# my_name = "kabir"
# for c in my_name:
#     print(c.upper(), end="")
#     if c == "i":
#         print("oops")

# for fd in range(-10, 11):
#     print(fd)
#     for sd in range(1, fd):
#         print("*", end="")

# Number of lines for the equilateral triangle


n = 11
n=int(n)
for i in range(n):
    # Print leading spaces
    for j in range(n - i - 1):
        print(" ", end=" ")
    
    # Print stars
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()
    


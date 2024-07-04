def square(n):
    #n = n*n
    return n*n

print(square(9))

def factorials(b):
    if b == 1 or b == 0:
        return 1
    else:
        return b * factorials(b - 1)
    
def factorialk(b):
    result = 1
    for i in range(1, b+1):
        result = result * i
    return result

print(factorialk(5))
print(factorials(4))

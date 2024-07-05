
print("how many terms you want to sum fibo? : ")
num_series= int(input())

def fibosum(n):
    if n <= 0:
        return 0
    series = [0,1]
    while len(series) <=n:
        next_seq = series[-1]+ series[-2]
        series.append(next_seq)
    return sum(series[:n])

result = fibosum(num_series)
print ('the fibo sum of first  ' + str(num_series) + ' terms is ' + str(result))


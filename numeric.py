fisrt_digit = 3
second_digit = 5

result = second_digit // fisrt_digit

# print(type(fisrt_digit))
# print(result)
# print(type(result))

# num = input("type the number: ")
# num = float(num)
# num = abs(num)
# print(num + 5)
# n = 11
# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end=" ")
    
#     for j in range(2 * i + 1):
#         print("*", " ")
#         print()
# n= 1
# print(f"the factorial is {n}" )
# def divby42(a):
#     try:
#         return 42/a
#     except ZeroDivisionError :
#         print("you entered zero in numerator")
# print(divby42(42))
# print(divby42(21))
# print(divby42(0))
# print(divby42(5))
print(" please tell me upto what digit you want the fibonacci sum?")
n= input()
n= int(n)
sum=0
for i in range(0,n+1):
    fibo=sum+i
    sum=fibo
print(f"the fibonacci sum is {sum}")
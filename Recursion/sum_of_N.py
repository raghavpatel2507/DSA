#method-1
#o(n)
# def sum_of_N(sum,i,N):
#     if i>N:
#         print(sum)
#         return
#     sum_of_N(sum+i,i+1,N)

# sum_of_N(0,1,5)

#method-2
#o(n)
# def sum_of_N(N):
#     if N==1:
#         return 1
#     return N+sum_of_N(N-1)

# print(sum_of_N(5))

#method-3
#o(1)
def sum_of_N(n):
    return (n*(n+1))//2

print(sum_of_N(5))
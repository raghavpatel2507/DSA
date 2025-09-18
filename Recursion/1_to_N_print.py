def print_numbers(i,N):
    if i > N:
        return
    print(i)
    print_numbers(i+1,N)

print_numbers(1,5)
#121 -> rev->121 -pelindrome no
#123 ->rev->321 -not


n=121
num=n
rev=0

while num>0:
    ld=num%10
    rev=rev*10+ld
    num=num//10

if n==rev:
    print("This is a pelindrome number")
else:
    print("not a pelindrome number")

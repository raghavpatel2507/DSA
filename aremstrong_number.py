#153=1**3+5**3+3**3=153 -armstrong number

n=123
num=n
total=0

nod=len(str(n))
while num>0:
    ld=num%10
    total=total+ld**nod
    num=num//10

if n==total:
    print("this is armstrong number")
else:
    print("Not a armstrong number")
s="nitin"

left=0
right=len(s)-1


def check_pelindrome(s,left,right):
    while left < right:
        if s[left]!=s[right]:
            return False
        else:
            left+=1
            right-=1
    return True

print(check_pelindrome(s,left,right))

        



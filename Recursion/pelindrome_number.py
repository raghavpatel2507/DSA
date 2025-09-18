s="nitina"

def check_pelindrome(s,left,right):
    if left>=right:
        return True
    if s[left]!=s[right]:
        return False
    return check_pelindrome(s,left+1,right-1)

print(check_pelindrome(s,left=0,right=len(s)-1))
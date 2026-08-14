import sys
lines=sys.stdin.read().splitlines()
max_len=max(len(line) for line in lines)
print('*'*(max_len+2))
bias_left=True
for line in lines:
    spaces=max_len-len(line)
    left=spaces//2
    right=spaces-left
    if spaces%2==1:
        if bias_left:
            left,right=left+1,right
        else:
            left,right=left,right+1
        bias_left=not bias_left
    print('*'+' '*left+line+' '*right+'*')
print('*'*(max_len+2))

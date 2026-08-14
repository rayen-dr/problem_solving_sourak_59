'''
 ▄▄▄▄▄     ▄▄    ▄▄  ▄▄    ▄▄  ▄▄                    ▄▄▄▄       ▄▄     ▄▄▄▄▄▄    ▄▄▄   ▄▄     ▄▄    ▄▄▄    ▄▄▄ ▄▄▄   ▄▄ 
 ██▀▀▀██   ██    ██  ██    ██  ██                   ██▀▀██     ████    ██▀▀▀▀██  ███   ██    ████    ██▄  ▄██  ███   ██ 
 ██    ██  ██    ██  ██    ██  ██                  ██    ██    ████    ██    ██  ██▀█  ██    ████     ██▄▄██   ██▀█  ██ 
 ██    ██  ████████  ██    ██  ██                  ██    ██   ██  ██   ███████   ██ ██ ██   ██  ██     ▀██▀    ██ ██ ██ 
 ██    ██  ██    ██  ██    ██  ██         █████    ██    ██   ██████   ██  ▀██▄  ██  █▄██   ██████      ██     ██  █▄██ 
 ██▄▄▄██   ██    ██  ▀██▄▄██▀  ██▄▄▄▄▄▄             ██▄▄██▀  ▄██  ██▄  ██    ██  ██   ███  ▄██  ██▄     ██     ██   ███ 
 ▀▀▀▀▀     ▀▀    ▀▀    ▀▀▀▀    ▀▀▀▀▀▀▀▀              ▀▀▀██   ▀▀    ▀▀  ▀▀    ▀▀▀ ▀▀   ▀▀▀  ▀▀    ▀▀     ▀▀     ▀▀   ▀▀▀ 
'''  


def bin_search(pmax,n,val):
 low,high,ans=0,n-1,-1
 while low<=high:
  mid=(low+high)//2
  if pmax[mid]<=val:ans=mid;low=mid+1
  else:high=mid-1
 return ans
def solve():
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    k=list(map(int,input().split()))
    pmax=[0]*n;psum=[0]*n
    pmax[0]=psum[0]=a[0]
    for j in range(1,n):
        pmax[j]=max(pmax[j-1],a[j])
        psum[j]=psum[j-1]+a[j]
    res=[]
    for v in k:
        ind=bin_search(pmax,n,v)
        res.append(0 if ind==-1 else psum[ind])
    print(' '.join(map(str,res)))

def main():
    t=int(input())
    for _ in range(t):
        solve()

if __name__=="__main__":
    main()
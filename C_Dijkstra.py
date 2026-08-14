import heapq,sys
input=sys.stdin.readline
def dijkstra(n,adj):
    INF=10**18
    dist=[INF]*(n+1)
    parent=[-1]*(n+1)
    dist[1]=0
    pq=[(0,1)]
    while pq:
        d,u=heapq.heappop(pq)
        if d>dist[u]: continue
        for v,w in adj[u]:
            if dist[u]+w<dist[v]:
                dist[v]=dist[u]+w
                parent[v]=u
                heapq.heappush(pq,(dist[v],v))
    return dist,parent

def main():
    n,m=map(int,input().split())
    adj=[[] for _ in range(n+1)]
    for _ in range(m):
        a,b,w=map(int,input().split())
        adj[a].append((b,w))
        adj[b].append((a,w))
    dist,parent=dijkstra(n,adj)
    if dist[n]==10**18:
        print(-1); return
    path=[]
    v=n
    while v!=-1:
        path.append(v)
        v=parent[v]
    print(" ".join(map(str,path[::-1])))

if __name__=="__main__":
    main()

from collections import deque
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    queue=deque([(0,0)])
    visited=set([(0,0)])
    steps=0
    found=False
    while queue:
        size=len(queue)
        for _ in range(size):
            x,y=queue.popleft()
            if x==a and y==b:
                print(steps)
                found=True
                break
            nx,ny=x,y+1
            if (nx,ny) not in visited:
                queue.append((nx,ny))
                visited.add((nx,ny))
            nx,ny=nx+1,ny
            if (nx,ny) not in visited:
                queue.append((nx,ny))
                visited.add((nx,ny))
            nx,ny=x,y-1
            if nx>=0 and ny>=0:    
                if (nx,ny) not in visited:
                    queue.append((nx,ny))
                    visited.add((nx,ny))
                nx,ny=nx+1,ny
                if (nx,ny) not in visited:
                    visited.add((nx,ny))
                    queue.append((nx,ny))
        if found:
            break
        steps+=1



n,m=map(int,input().split())
r='안녕'
b=[]
a=''
for i in range(1,n+1):
    b+=str(i)

for a in range(m):
    i,j=map(int,input().split())
    y=b[i-1]
    z=b[j-1]
    b[i-1]=z
    b[j-1]=y
for i in b:
    str(a)+=str(i)+' '
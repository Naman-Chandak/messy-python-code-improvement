# grade calc
a=[["Aarav",78,85,92],["Diya",66,71,58],["Kabir",90,95,88],["Meera",45,52,60]]
x=0
y=[]
for i in a:
    n=i[0]
    t=i[1]+i[2]+i[3]
    p=t/3
    if p>=90:
        g="A"
    elif p>=75:
        g="B"
    elif p>=60:
        g="C"
    elif p>=50:
        g="D"
    else:
        g="F"
    print(n,"-",t,"-",round(p,2),"-",g)
    x=x+p
    y.append([n,p])
z=x/len(a)
print("class avg",round(z,2))
m=0
mn=""
for i in y:
    if i[1]>m:
        m=i[1]
        mn=i[0]
print("topper",mn,round(m,2))
c=0
for i in y:
    if i[1]>=50:
        c=c+1
print("passed",c,"out of",len(a))
l=0
ln=""
l=1000
for i in y:
    if i[1]<l:
        l=i[1]
        ln=i[0]
print("lowest",ln,round(l,2))

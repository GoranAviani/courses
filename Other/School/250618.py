def izlet(x,y,m):
    if x<y*m:
        return 'DA'
    else:
        return 'NE'

u=int(input('Unesi broj učenika: '))
a=int(input('Unesi broj autobusa: '))
m=int(input('Unesi broj sjedećih mjesta u autobusu: '))
print(izlet(u,a,m))
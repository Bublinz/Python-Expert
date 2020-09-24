x = ['7','3','4','8','9']
print(x.index('4'))
y = ['hello', 'obi', 0.34]
print(y.index('obi'))
m = [7,3,4,8,9]
m.append(5)
print(m)
s = ['hello', 'obi', 0.34]
s.insert(1, 'add')
print(s)
egg = ['hello']
egg.append('word')
print(egg)
n= [7,3,4,8,9,5]
n.remove(4)
print(n)
g = [7,3,4,5,8,9,5]
g.remove(5)
print(g)
a = [7,3,4,5,6,1,8,9,2,5]
a.sort()
print(a)
b = [3,7,4,5,6,1,8,9,2,5]
b.sort(reverse = True)
print(b)
z = ['x','w','G','g','M','A','a','Q','n','i','q']
z.sort(key = str.lower)
print(z)

class node:
    def __init__(self,val):
        self.data = val
        self.next = None
a = node(30) # Inital Head
b = node(10)
c = node(20)
d = node(15)
e = node(25)

a.next = b
a.next.next = c
c.next = d
d.next = e
temp = a
l = []
while temp!=None:
    l += [temp.data]
    temp = temp.next
l.sort()
print(l)
head1 = node(l[0])
temp1 = head1
i = 1
while i<len(l):
    head1.next = node(l[i])
    head1 = head1.next
    i += 1
# print(temp1.data)
li = []
while temp1 != None:
    p = temp1.data
    li.append(p)
    temp1 = temp1.next
print(li)

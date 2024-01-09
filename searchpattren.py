txt = "geeksforgeeks"
pat = "geek"
l = []
for i in range(len(txt)-len(pat)+1):
    if txt[i:i+len(pat)] == pat:
        l.append(i+1)
print(l)

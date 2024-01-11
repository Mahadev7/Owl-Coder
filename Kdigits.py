s = '149811'
k = 3
st= [s[0]]
for i in range(1,len(s)):
    if len(st) == 0:
        st.append((s[i]))
    elif s[i] > st[-1]:
        st.append((s[i]))
    else:
        while k and len(st) and s[i]<st[-1]:
            st.pop()
            k-=1
        st.append(s[i])
while k:
    st.pop()
    k-=1
stri = "".join(st).lstrip("0")
print(stri)

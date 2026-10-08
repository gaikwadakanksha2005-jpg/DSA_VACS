s="slient"
t="listen"

arr=[0]*26

for i in range(len(s)):
    arr[ord(s[i])-97]+=1

for i in range(len(t)):
    arr[ord(t[i])-97] -=1

if arr==[0]*26:
    print("Anagram")
else:
    print("Not Anaram")           


with open('in.txt') as fh:
    s = fh.read().strip()
   
for i in range(14, len(s)):
    candidate = s[i-14:i] 
    #print(candidate)
    if len(set(candidate)) == 14:
        print(i)
        break

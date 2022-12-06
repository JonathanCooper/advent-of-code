

with open('in.txt') as fh:
    s = fh.read().strip()
   
for i in range(4, len(s)):
    candidate = s[i-4:i] 
    #print(candidate)
    if len(set(candidate)) == 4:
        print(i)
        break

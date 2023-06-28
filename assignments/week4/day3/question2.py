'''
Two strings are considered “almost equivalent” if they have the same length AND for each lowercase letter x, the number of occurrences of x in the two strings differs by no more than 3. 
'''

def compare(s, t):
	#strings must be same length
    if len(s) != len(t):
        return False
    #get the difference in char frequencies for each str
    freq = {}
    for char in s:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
            
    for char in t:
        if char in freq:
            freq[char]-=1
        else:
            freq[char]=1

    #check if the diff between any chars is greater than 3
    for key in freq:
        if abs(freq[key]) > 3:
            return False

    return True

def areAlmostEquivalent(s, t):
    result = []
    
    #s and t both have N elements
    for i in range(len(s)):
        if compare(s[i], t[i]):
            result.append("YES")
        else:
            result.append("NO")

    return result


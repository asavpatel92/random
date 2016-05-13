def is_substring(str1, str2):
    temp = {}
    for char in set(str1):
        temp[char] = True
        
    for char in set(str2):
        if temp.get(char):
            print "YES"
            return
    print "NO"
    return

def main():
    test = int(raw_input().strip())
 
    for _ in xrange(test):
        s1 = set(raw_input().strip().lower())
        s2 = set(raw_input().strip().lower())
        is_substring(s1, s2)
            
main()
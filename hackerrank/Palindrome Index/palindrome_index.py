# https://www.hackerrank.com/challenges/palindrome-index

def is_palindrome(s):
    for i in xrange(len(s) // 2):
        if (s[i] != s[len(s)-i-1]):
            return False
    return True

def palindrome_index(s):
    for idx in xrange((len(s)+1)//2):
        if s[idx] != s[len(s)-idx-1]:
            if is_palindrome(s[:idx]+s[idx+1:]):
                return idx
            else:
                return len(s)-idx-1
    return -1

def main():
    test = int(raw_input().strip())
    
    for _ in xrange(test):
        print palindrome_index(raw_input().strip())

main()
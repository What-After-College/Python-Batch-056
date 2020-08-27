
#   HackerRank.com presents "Pythonist 2".

# https://www.hackerrank.com/challenges/swap-case/problem 

def swap_case(s):
    ans = ''
    for i in s:
        if not i.islower():
            ans += i.lower()
        else:
            ans += i.upper()
            
    return ans


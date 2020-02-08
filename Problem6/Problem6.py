#!/bin/python3

def check(ip):
    stk = [] # initialise a list as stack
    open_br = ['{', '[', '('] # create a list of open_br brackets
    close = ['}', ']', ')'] # create a list of closed brackets
    pairs = { '}':'{',']': '[', ')':'(' } # create dict of open_br-close pairs
    for v in ip:
        if (v in open_br): # append open_br bracket
            stk.insert(0, v)
        # check if close bracket appears first
        if (v in close): 
            if ((pairs[v] not in stk) or (pairs[v] != stk[0])):
                return "NO"
            else:
                stk.pop(0) # pop open_br bracket if closed appears            
# check if stack is empty after iterating through the input string chars
    result = 'YES' if (stk == []) else 'NO'
    return(result)

if __name__ == '__main__':
    t = int(input()) # accept number of inputs to be fed

    for t_itr in range(t):
        ip  = input()  # accept individual input
        print(check(ip)) # evaluate input string



"""
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
def longest_run(L):
    dec = 0
    inc = 0
    maxrun = 0
    ans = 0

    for char in range(len(L) - 1):
        if (L[char] <= L[char + 1]):
            dec += 1
            if dec > maxrun:
                maxrun = dec
                ans = char + 1
        else:
            dec = 0
        if (L[char] >= L[char + 1]):
            inc += 1            
            if inc > maxrun:
                maxrun = inc
                ans = char + 1
        else:
            inc = 0
        
    strt = ans - maxrun
    return sum(L[strt:ans + 1])

def solution(a):
    if (len(a) == 0):
        return -1
    pos = 0
    count = 0
    while pos >= 0 and pos < len(a):
        if (a[pos] == 0): return -1
        jump = a[pos]
        a[pos] = 0
        pos += jump
        count += 1
    return count
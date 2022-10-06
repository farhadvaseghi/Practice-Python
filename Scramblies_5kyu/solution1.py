def str_dic(s):
    dic_char={}
    for i in s:
        if i in dic_char:
            dic_char[i] += 1
        else:
            dic_char.update({i:1})
    return dic_char
def scramble(s1, s2):
    d1 = str_dic(s1)
    d2 = str_dic(s2)
    for i in d2:
        if i not in d1 or d2[i]>d1[i]:
                return False
    return True 
def is_pangram(s):
    dic_alphabet = {}
    s = s.lower().replace(" ", "")

    for letter in s:
        if letter.isalpha():
            if letter in dic_alphabet:
                dic_alphabet[letter] +=1
            else:
                dic_alphabet.update({letter:1})
    if len(dic_alphabet.keys())==26:
        return True
    else:
        return False



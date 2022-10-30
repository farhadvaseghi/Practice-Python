def most_money(students):
    dic_info = {person.name:person.fives*5 + person.tens*10 + person.twenties*20 for person in students}  
    if len(set(dic_info.values()))==1 and len(dic_info)>1 :
        return "all"
    else:
        return max(dic_info, key=dic_info.get)
            
def split_the_bill(x):
    sum = 0 
    for value in x.values():
        sum+=value 
    avg = sum/len(x)
    result = {}
    for key, value in x.items():
        result[key]=round(value-avg, 2)
    return result
def split_the_bill(x):
    avg = sum(x.values())/len(x)
    return {key: round(x[key]-avg, 2) for key in x}
def draw(n):
    
    m = n//2
    h =  [("◢" + "■" * (m-2) + "◣") * 2]
    h += ["■" * n for _ in range(n//6)]
    h += [("◥" + "■" * 2 * (m-1-i) + "◤").center(n, " ") for i in range(m)]
    return "\n".join(h)
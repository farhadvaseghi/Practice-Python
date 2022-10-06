def int32_to_ip(int32):
    binary = bin(int32)
    binary = binary[2:]
    if len(binary)%8 != 0:
        b = (int(len(binary)/8)+1)*8 - len(binary)
    else:
        b=0
    add = b*"0"
    r = add+binary
    d = [str(int(r[i:i+8],2)) for i in range(0,len(r),8)]
    
    if len(d) != 0:
        b = ["0" for i in range(4-len(d))]
        d = b+d
    out = ".".join(d) 
    return out
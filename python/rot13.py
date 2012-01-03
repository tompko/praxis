plain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rotate = plain[13:] + plain[:13]

rotdict = dict(zip(plain + plain.lower(), rotate + rotate.lower()))

def rot13(text):
    ret = ""
    for t in text:
        if t in rotdict:
            ret += rotdict[t]
        else:
            ret += t
    return ret

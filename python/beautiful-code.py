def match(re, text):
    """match: search for re anywhere in text"""
    if re[0] == '^':
        return matchhere(re[1:], text)
    if matchhere(re, text):
        return True

    while len(text) > 0:
        text = text[1:]
        if matchhere(re, text):
            return True
    return False

def matchhere(re, text):
    """matchhere: search for re at beginning of text"""
    if len(re) == 0:
        return True
    if len(re) > 1 and re[1] == '*':
        return matchstar(re[0], re[2:], text)
    if re[0] == '$' and len(re) == 1:
        return len(text) == 0
    if len(text) > 0 and (re[0]=='.' or re[0]==text[0]):
        return matchhere(re[1:], text[1:])
    return False

def matchstar(c, re, text):
    """matchstar: search for c*re at beginning of text"""
    if matchhere(re, text):
        return True
    while len(text) > 0 and (text[0] == c or c == "."):
        text = text[1:]
        if matchhere(re, text):
            return True
    return False

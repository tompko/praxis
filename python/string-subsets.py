def string_subset(string, sub_string):
    string_count = {}
    sub_string_count = {}
    
    for s in string.upper():
        string_count[s] = string_count.get(s, 0) + 1
    for s in sub_string.upper():
        sub_string_count[s] = sub_string_count.get(s, 0) + 1

    for c, v in sub_string_count.iteritems():
        if v > string_count[c]:
            return False
    return True
        

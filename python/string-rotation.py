def string_rotation(string1, string2):
    if len(string1) != len(string2):
        return False

    concat = string1 + string1

    if concat.find(string2) >= 0:
        return True
    return False

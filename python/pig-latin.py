def pig_latin_to_english(string):
    words = string.split()
    english = []

    for w in words:
        suff,post = w.split("-")
        if post == "way":
            english.append(suff)
        else:
            english.append(post[:-2] + suff)

    return " ".join(english)

def english_to_pig_latin(string):
    words = string.split()
    pig_latin= []

    for w in words:
        if w[0] in "aeiou":
            pig_latin.append(w+"-way")
        else:
            post = "-"
            while w[0] not in "aeiou":
                post += w[0]
                w = w[1:]
            pig_latin.append(w + post + "ay")

    return " ".join(pig_latin)

morse = {"a": ".-", "b": "-.", "c": "-.-.", "d": "-..", "e": ".",
         "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---",
         "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
         "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
         "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--",
         "z": "--..", "1": ".----", "2": "..---", "3": "...--",
         "4": "....-", "5": ".....", "6": "-....", "7": "--...",
         "8": "---..", "9": "----.", "0": "-----"}

plain = {}
for key, val in morse.iteritems():
    plain[val] = key


def plain_to_morse(text):
    ret = []
    for word in text.split():
        ret.append(" ".join([morse[x.lower()] for x in word]))
    return "  ".join(ret)

def morse_to_plain(morse):
    words = morse.split("  ")
    ret = []
    for word in words:
        nword = ""
        chars = word.split()
        for c in chars:
            nword += plain[c]
        ret.append(nword)
    return " ".join(ret)

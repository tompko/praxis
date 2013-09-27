class LiteralCharacter():
    def match(self, text):
        if text[0] == self.character:
            return True
        return False

    def repeat(self):
        return self.repeats

    @staticmethod
    def parse_match(re, elements):
        return True
    
    def parse(self, re):
        self.character, ret = read_char(re)
        self.repeats, ret = repeats(ret)
        return ret

class Dot():
    def match(self, text):
        return True

    def repeat(self):
        return self.repeats

    @staticmethod
    def parse_match(re, elements):
        return re[0] == "."

    def parse(self, re):
        assert(re[0] == ".")
        re = re[1:]
        self.repeats, re = repeats(re)
        return re

class Beginning():
    def match(self, text):
        raise NotImplemented

    def repeat(self):
        raise NotImplemented

    @staticmethod
    def parse_match(re, elements):
        return elements == [] and re[0] == "^"

    def parse(self, re):
        assert(re[0] == "^")
        return re[1:]

class End():
    def match(self, text):
        return len(text) == 0

    def repeat(self):
        return False

    @staticmethod
    def parse_match(re, elements):
        return re[0] == "$" and len(re) == 1

    def parse(self, re):
        assert(re[0] == "$")
        assert(len(re) == 1)
        return ""

class CharacterClass():
    def match(self, text):
        if self.negated:
            return text[0] not in self.characters
        return text[0] in self.characters

    def repeat(self):
        return self.repeats

    @staticmethod
    def parse_match(re, elements):
        return re[0] == "["

    def parse(self, re):
        assert(re[0] == "[")
        re = re[1:]
        self.characters = []
        self.negated = False
        if re[0] == "^":
            self.negated = True
            re = re[1:]
        while re[0] != "]":
            char, re = read_char(re)
            self.characters.append(char)
        re = re[1:]
        self.repeats, re = repeats(re)
        return re

def repeats(re):
    ret = False
    if not re:
        return ret, re
    if re[0] == "*":
        ret = True
        re = re[1:]
    return ret, re

def read_char(text):
    if text[0] == "\\":
        if text[1] == "n":
            return "\n", text[2:]
        elif text[1] == "t":
            return "\t", text[2:]
        else:
            return text[1], text[2:]
    return text[0], text[1:]

def parse(re):
    """Parses a regular expression and returns a list of regex elements"""
    elements = []

    classes = [Beginning,
               End,
               Dot,
               CharacterClass,
               LiteralCharacter]

    while re:
        for cl in classes:
            if cl.parse_match(re, elements):
                elem = cl()
                re = elem.parse(re)
                elements.append(elem)
                break

    return elements

def matchstar(c, compiled, text):
    if matchhere(compiled, text):
        return True
    
    while len(text) > 0 and c.match(text):
        text = text[1:]
        if matchhere(compiled, text):
            return True
    return False

def matchhere(compiled, text):
    if len(compiled) == 0:
        return True
    if compiled[0].repeat():
        return matchstar(compiled[0], compiled[1:], text)
    if compiled[0].match(text):
        return matchhere(compiled[1:], text[1:])
    return False

def match(compiled, text):
    if isinstance(compiled[0], Beginning):
        return matchhere(compiled[1:], text)

    while len(text) > 0:
        if matchhere(compiled, text):
            return True
        text = text[1:]
    return False

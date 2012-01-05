import unittest

class LiteralCharacter():
    def match(self, text):
        if len(text) == 0:
            return False
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
        if len(text) == 0:
            return False
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
        if len(text) == 0:
            return False
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
            if char == "-" and re[0] != "]" and len(self.characters) > 0:
                limit, re = read_char(re)
                for i in range(ord(self.characters[-1]), ord(limit)):
                    self.characters.append(chr(i))
                char = limit
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
    """Parses a regular expression and returns a list of re_match elements"""
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
    if len(compiled) == 0:
        return True
    
    if isinstance(compiled[0], Beginning):
        return matchhere(compiled[1:], text)

    while len(text) > 0:
        if matchhere(compiled, text):
            return True
        text = text[1:]
    return False

def re_match(re, text):
    comp = parse(re)
    return match(comp, text)

class Testre_matchEngine(unittest.TestCase):
    def test_re_match(self):
        self.assertEquals(re_match("", ""), True)
        self.assertEquals(re_match("", "a"), True)
        self.assertEquals(re_match("a", ""), False)
        self.assertEquals(re_match("a", "a"), True)
        self.assertEquals(re_match("a", "b"), False)
        self.assertEquals(re_match("a", "ab"), True)
        self.assertEquals(re_match("a", "ba"), True)
        self.assertEquals(re_match("a", "aa"), True)
        self.assertEquals(re_match("ab", "a"), False)
        self.assertEquals(re_match("ab", "ab"), True)
        self.assertEquals(re_match("ab", "ba"), False)
        self.assertEquals(re_match("ab", "aab"), True)
        self.assertEquals(re_match("ab", "bab"), True)
        self.assertEquals(re_match("ab", "abab"), True)
        self.assertEquals(re_match("ab", "ac"), False)
        self.assertEquals(re_match("ab", "acb"), False)
        self.assertEquals(re_match("\n", "a\n"), True)
        self.assertEquals(re_match("\n", "abc"), False)
        self.assertEquals(re_match("\t", "a\t"), True)
        self.assertEquals(re_match("\t", "abc"), False)
        self.assertEquals(re_match(r"\b", "abc"), True)
        self.assertEquals(re_match(r"\b", "ac"), False)
        self.assertEquals(re_match(r"a\b", "ab"), True)
        self.assertEquals(re_match(r"a\b", "ba"), False)
        self.assertEquals(re_match("^ab", "abc"), True)
        self.assertEquals(re_match("^ab", "aab"), False)
        self.assertEquals(re_match("ab$", "ab"), True)
        self.assertEquals(re_match("ab$", "aab"), True)
        self.assertEquals(re_match("ab$", "aba"), False)
        self.assertEquals(re_match("^ab$", "ab"), True)
        self.assertEquals(re_match("^ab$", "abc"), False)
        self.assertEquals(re_match(".", ""), False)
        self.assertEquals(re_match(".", "a"), True)
        self.assertEquals(re_match("a.", "a"), False)
        self.assertEquals(re_match("a.", "ab"), True)
        self.assertEquals(re_match("a.", "bb"), False)
        self.assertEquals(re_match("[abc]", "a"), True)
        self.assertEquals(re_match("[abc]", "b"), True)
        self.assertEquals(re_match("[abc]", "c"), True)
        self.assertEquals(re_match("[abc]", "d"), False)
        self.assertEquals(re_match("[a-c]", "a"), True)
        self.assertEquals(re_match("[a-c]", "b"), True)
        self.assertEquals(re_match("[a-c]", "c"), True)
        self.assertEquals(re_match("[a-c]", "d"), False)
        self.assertEquals(re_match("[A-C]", "A"), True)
        self.assertEquals(re_match("[A-C]", "B"), True)
        self.assertEquals(re_match("[A-C]", "C"), True)
        self.assertEquals(re_match("[A-C]", "D"), False)
        self.assertEquals(re_match("[1-3]", "1"), True)
        self.assertEquals(re_match("[1-3]", "2"), True)
        self.assertEquals(re_match("[1-3]", "3"), True)
        self.assertEquals(re_match("[1-3]", "4"), False)
        self.assertEquals(re_match("[c-a]", "a"), True)
        self.assertEquals(re_match("[c-a]", "b"), False)
        self.assertEquals(re_match("[-]", "-"), True)
        self.assertEquals(re_match("[-]", "a"), False)
        self.assertEquals(re_match("[\n]", "\n"), True)
        self.assertEquals(re_match("[\t]", "\t"), True)
        self.assertEquals(re_match("[\n]", "a"), False)
        self.assertEquals(re_match("[\t]", "a"), False)
        self.assertEquals(re_match("[a-cd-f]", "e"), True)
        self.assertEquals(re_match("[a-cd-f]", "g"), False)
        self.assertEquals(re_match("[^abc]", "a"), False)
        self.assertEquals(re_match("[^abc]", "b"), False)
        self.assertEquals(re_match("[^abc]", "c"), False)
        self.assertEquals(re_match("[^abc]", "d"), True)
        self.assertEquals(re_match("[^a-c]", "a"), False)
        self.assertEquals(re_match("[^a-c]", "b"), False)
        self.assertEquals(re_match("[^a-c]", "c"), False)
        self.assertEquals(re_match("[^a-c]", "d"), True)
        self.assertEquals(re_match("[^A-C]", "A"), False)
        self.assertEquals(re_match("[^A-C]", "B"), False)
        self.assertEquals(re_match("[^A-C]", "C"), False)
        self.assertEquals(re_match("[^A-C]", "D"), True)
        self.assertEquals(re_match("[^1-3]", "1"), False)
        self.assertEquals(re_match("[^1-3]", "2"), False)
        self.assertEquals(re_match("[^1-3]", "3"), False)
        self.assertEquals(re_match("[^1-3]", "4"), True)
        self.assertEquals(re_match("[^c-a]", "a"), False)
        self.assertEquals(re_match("[^c-a]", "b"), True)
        self.assertEquals(re_match("[^-]", "-"), False)
        self.assertEquals(re_match("[^-]", "a"), True)
        self.assertEquals(re_match("[^\n]", "\n"), False)
        self.assertEquals(re_match("[^\t]", "\t"), False)
        self.assertEquals(re_match("[^\n]", "a"), True)
        self.assertEquals(re_match("[^\t]", "a"), True)
        self.assertEquals(re_match("[^a-cd-f]", "e"), False)
        self.assertEquals(re_match("[^a-cd-f]", "g"), True)
        self.assertEquals(re_match("a*", "aaa"), True)
        self.assertEquals(re_match("a*", "bbb"), True)
        self.assertEquals(re_match("bb*", "abc"), True)
        self.assertEquals(re_match("aa*", "bc"), False)
        self.assertEquals(re_match("ab*c", "abbc"), True)
        self.assertEquals(re_match("ab*c", "ac"), True)
        self.assertEquals(re_match("ab*c", "abc"), True)
        self.assertEquals(re_match("a.*c", "abbc"), True)
        self.assertEquals(re_match("a.*c", "ac"), True)
        self.assertEquals(re_match("a.*c", "abc"), True)
        self.assertEquals(re_match("a[b-d]*e", "abcde"), True)
        self.assertEquals(re_match("a[b-d]*e", "axe"), False)
        self.assertEquals(re_match("a*a*a", "a"), True)
        self.assertEquals(re_match("a*a*a", "aaa"), True)
        self.assertEquals(re_match("a*a*a", "b"), False)

if __name__ == "__main__":
    unittest.main()

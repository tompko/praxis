roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50,
                "C": 100, "D": 500, "M": 1000}

int_to_roman = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
                (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
                

def parse_roman(number):
    ret, index, limit = 0, 0, len(number) - 1

    while index < limit:
        if roman_to_int[number[index]] < roman_to_int[number[index + 1]]:
            ret -= roman_to_int[number[index]]
        else:
            ret += roman_to_int[number[index]]
        index += 1
    ret += roman_to_int[number[-1]]
    return ret

def print_roman(number):
    curr = 0
    ret = ""
    while number > 0:
        if number >= int_to_roman[curr][0]:
            number -= int_to_roman[curr][0]
            ret += int_to_roman[curr][1]
        else:
            curr += 1
    return ret

def add_roman(a, b):
    return print_roman(parse_roman(a) + parse_roman(b))

if __name__ == "__main__":
    print add_roman("CCCLXIX", "CDXLVIII")

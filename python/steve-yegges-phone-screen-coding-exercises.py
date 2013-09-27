#Write a function to reverse a string.
def str_reverse(string):
    return string[::-1]

#Write a function to compute the Nth fibonacci number.
def fibbonacci(n):
    a,b = 0,1

    for i in range(n):
        a,b = b, a+b
    return a

#Print out the grade-school multiplication table up to 12 x 12.
def mul_table():
    for i in range(1, 13):
        print "".join(["%4i" % (j*i) for j in range(1,13)])
    
#Write a function that sums up integers from a text file, one per line.
def sum_file(path):
    with open(path) as fin:
        numbers = fin.read().split()
        return reduce(lambda x, y: x + int(y), numbers, 0)

#Write a function to print the odd numbers from 1 to 99.
def odd_numbers():
    print [x for x in range(100) if x % 2 == 1]

#Find the largest int value in an int array.
def int_max(xs):
    #return max(xs)
    return reduce(lambda x,y: max(x, y), xs)

#Format an RGB value (three 1-byte numbers) as a 6-digit hexadecimal string.
def rgb_colour(r, g, b):
    return "0x%02x%02x%02x" % (r, g, b)

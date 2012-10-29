"""Steve Yegge's Phone-Screen Coding Exercises: A simple set of programming
exercises based on a blog entry by Steve Yegge"""

def question1(string):
    """Write a function to reverse a string."""
    return string[::-1]

def question2(n):
    """Write a function to compute the Nth fibonacci number.

    Instead of the given recursive solution which takes exponential
    time, we use an interative version taking linear time.
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def question3():
    """Print out the grade-school multiplication table up to 12 x 12."""
    for i in range(1, 13):
        print "".join(["{0:4}".format(i*j) for j in range(1, 13)])

def question4(file_path):
    """Write a function that sums up integers from a text file, one per line."""
    with open(file_path) as text_file:
        return sum([int(x.strip()) for x in text_file.read().split()])

def question5():
    """Write a function to print the odd numbers from 1 to 99."""
    for i in range(1, 100, 2):
        print i

def question6(ns):
    """Find the largest int value in an int array."""
    return max(ns)

def question7(r, g, b):
    """Format an RGB value (three 1-byte numbers) as a 6-digit
    hexadecimal string."""
    return "{r:02x}{g:02x}{b:02x}".format(r=r, g=g, b=b)

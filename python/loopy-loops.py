count = 1

def count_up():
    global count
    print count
    count += 1

def call_twice(foo):
    foo(); foo()

def call_five(foo):
    call_twice(lambda: call_twice(foo)); foo()

def call_ten(foo):
    call_twice(lambda: call_five(foo))

def call_hundred(foo):
    call_ten(lambda: call_ten(foo))

def call_thousand(foo):
    call_ten(lambda: call_hundred(foo))

def count_to_1000():
    global count
    count = 1
    call_thousand(count_up)

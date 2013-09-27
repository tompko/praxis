def look_and_say():
    term = "1"

    while True:
        yield term
        new_term = ""
        curr = term[0]
        count = 0
        for t in term:
            
            if t == curr:
                count += 1
            else:
                new_term += str(count) + curr
                curr = t
                count = 1
        new_term += str(count) + curr
        term = new_term

import praxis

keys = [708894553, 704488409, 705674273, 707478271, 710167019, 708093251,
        702013379, 704030867, 708691187, 708374743, 712748719, 713581951,
        704387447, 707015741, 704308279, 710872423, 707947453, 704996429,
        706323757, 705031051, 714623803]

def attack1():
    factorise = {}

    for i in range(len(keys)):
        for j in range(i):
            div = praxis.gcd(keys[i], keys[j])
            if div != 1:
                factorise[keys[i]] = (div, keys[i] / div)
                factorise[keys[j]] = (div, keys[j] / div)

    return factorise

def attack2():
    prod = reduce(lambda x, y: x*y, keys, 1)

    factorise = {}
    
    for key in keys:
        div = praxis.gcd(key, (prod % (key*key)) / key)
        if div != 1:
            factorise[key] = (div, key / div)
    return factorise

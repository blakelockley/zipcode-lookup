def first(t):
    return t[0]


def read_zipcodes():
    for line in open('zipcode.txt'):
        state, upper, lower = line.strip().split(';')
        yield state, int(upper), int(lower)


def find_state(value):
    for state, lower, upper in read_zipcodes():
        if lower <= value <= upper:
            return state

    return None 


def dense_map():
    """Produce a dense map to provide N(1) lookup for valid zipcode"""
    
    mapping = {}
    for state, lower, upper in read_zipcodes():
        for zipcode in range(lower, upper + 1):
            mapping[zipcode] = state
    
    return mapping


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) != 2:
        print(f"usage: python {sys.argv[0]} [-d | --dense | <zipcode>]")
        exit(1)

    if sys.argv[1] in ["-d", "--dense"]:
        print(dense_map())
        exit(0) 

    arg = int(sys.argv[1])

    result = find_state(arg)
    print(result)


def first(t):
    return t[0]


def read_zipcodes():
    for line in open('zipcode.txt'):
        state, upper, lower = line.strip().split(';')
        yield state, int(upper), int(lower)


def find_state(value):
    lower_map = []
    upper_map = []

    for state, lower, upper in read_zipcodes():
        lower_map.append((lower, state))
        upper_map.append((upper, state))

    lower_map.sort(key=first)
    upper_map.sort(key=first, reverse=True)

    upper_result = None
    for lower, state in lower_map:
        if lower > value:
            break
        upper_result = state

    lower_result = None
    for upper, state in upper_map:
        if upper < value:
            break
        lower_result = state

    if lower_result == upper_result:
        # Value found in valid range
        return lower_result

    # No valid range found
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


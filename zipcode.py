def first(t):
    return t[0]


def second(t):
    return t[1]


def main(value):
    lower_map = []
    upper_map = []

    for line in open('zipcode.txt'):
        state, lower, upper = line.strip().split(';')
        lower_map.append((int(lower), state))
        upper_map.append((int(upper), state))

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

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print(f"usage: python {sys.argv[0]} <zipcode>")
        exit(1)

    arg = int(sys.argv[1])

    result = main(arg)
    print(result)
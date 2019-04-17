def first(t):
    return t[0]


def read_zipcodes(input_path):
    for line in open(input_path):
        state, upper, lower = line.strip().split(';')
        yield state, int(upper), int(lower)


def find_state(input_path, value):
    for state, lower, upper in read_zipcodes(input_path):
        if lower <= value <= upper:
            return state

    return None 


def dense_map(input_path):
    """Produce a dense map to provide N(1) lookup for valid zipcode"""
    
    mapping = {}
    for state, lower, upper in read_zipcodes(input_path):
        for zipcode in range(lower, upper + 1):
            mapping[zipcode] = state
    
    return mapping


def json_map(input_path):
    import json

    padded_map = {}
    for (zipcode, state) in dense_map(input_path).items():
        padded_zipcode = str(zipcode).rjust(5, '0')
        padded_map[padded_zipcode] = state

    return json.dumps(padded_map, indent=4)

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) != 3:
        print(f"usage: python {sys.argv[0]} <input-file> [--json | --dense | <zipcode>]")
        exit(1)

    input_path = sys.argv[1]
    
    if sys.argv[2] in ["-j", "--json"]:
        print(json_map(input_path))

    elif sys.argv[2] in ["-d", "--dense"]:
        print(dense_map(input_path))

    else:
        arg = int(sys.argv[2])
        print(find_state(input_path, arg))


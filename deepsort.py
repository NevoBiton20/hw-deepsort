def deep_sorted(x:any)->str:
    if isinstance(x, str):
        # Try to convert string to number
        try:
            return int(x)
        except ValueError:
            try:
                return float(x)
            except ValueError:
                return x
    elif isinstance(x, dict):
        return {k: deep_sorted(x[k]) for k in sorted(x.keys())}
    elif isinstance(x, list):
        sorted_elements = [deep_sorted(k) for k in x]
        return sorted(sorted_elements, key=lambda k: serialize(k))
    elif isinstance(x, tuple):
        sorted_elements = [deep_sorted(k) for k in x]
        return tuple(sorted(sorted_elements, key=lambda k: serialize(k)))
    elif isinstance(x, set):
        sorted_elements = [deep_sorted(k) for k in x]
        return set(sorted(sorted_elements, key=lambda k: serialize(k)))
    else:
        return x


def serialize(obj):
    if isinstance(obj, dict):
        inner = ", ".join(f'"{k}": {serialize(v)}' for k, v in obj.items())
        return "{" + inner + "}"
    elif isinstance(obj, list):
        return "[" + ", ".join(serialize(x) for x in obj) + "]"
    elif isinstance(obj, tuple):
        if len(obj) == 1:
            return "(" + serialize(obj[0]) + ",)"
        return "(" + ", ".join(serialize(x) for x in obj) + ")"
    elif isinstance(obj, set):
        inner = ", ".join(serialize(x) for x in sorted(obj, key=lambda x: serialize(x)))
        return "{" + inner + "}"
    elif isinstance(obj, str):
        return f'"{obj}"'
    else:
        return str(obj)


def deep_sort_to_string(obj):
    sorted_obj = deep_sorted(obj)
    return serialize(sorted_obj)

if __name__ == '__main__':
    x=eval(input())
    print(deep_sorted(x))
    import doctest
    print (doctest.testmod())

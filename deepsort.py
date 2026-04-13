def deep_sorted(x: any) -> str:
    if isinstance(x, dict):
        items = sorted(x.items(), key=lambda kv: repr(kv[0]))
        s = '{'
        first = True
        for k, v in items:
            if not first:
                s += ', '
            s += deep_sorted(k) + ': ' + deep_sorted(v)
            first = False
        s += '}'
        return s

    if isinstance(x, list):
        vals = sorted(x, key=repr)
        s = '['
        first = True
        for v in vals:
            if not first:
                s += ', '
            s += deep_sorted(v)
            first = False
        s += ']'
        return s

    if isinstance(x, tuple):
        vals = sorted(x, key=repr)
        s = '('
        first = True
        for v in vals:
            if not first:
                s += ', '
            s += deep_sorted(v)
            first = False
        if len(vals) == 1:
            s += ','
        s += ')'
        return s

    if isinstance(x, set):
        vals = sorted(x, key=repr)
        s = '{'
        first = True
        for v in vals:
            if not first:
                s += ', '
            s += deep_sorted(v)
            first = False
        s += '}'
        return s

    return repr(x)

if __name__ == '__main__':
    x=eval(input()) 
    print(deep_sorted(x))
    import doctest
    print(doctest.testmod())

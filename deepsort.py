def deep_sorted(x: any) -> str:
    def sort_key(v):
        try:
            return (0, int(v))
        except:
            return (1, str(v))

    def out(v):
        if isinstance(v, str):
            try:
                return str(int(v))
            except:
                return repr(v)
        return repr(v) if isinstance(v, str) else str(v)

    if isinstance(x, dict):
        items = sorted(x.items(), key=lambda kv: sort_key(kv[0]))
        return '{' + ', '.join(f'{deep_sorted(k)}: {deep_sorted(v)}' for k, v in items) + '}'
    if isinstance(x, list):
        return '[' + ', '.join(deep_sorted(v) for v in sorted(x, key=sort_key)) + ']'
    if isinstance(x, tuple):
        s = ', '.join(deep_sorted(v) for v in sorted(x, key=sort_key))
        return '(' + s + (',' if len(x) == 1 else '') + ')'
    if isinstance(x, set):
        return '{' + ', '.join(deep_sorted(v) for v in sorted(x, key=sort_key)) + '}'
    return out(x)


if __name__ == '__main__':
    x=eval(input()) 
    print(deep_sorted(x))
    import doctest
    print(doctest.testmod())

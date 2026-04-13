def deep_sorted(x: any) -> str:
    if isinstance(x, dict):
        items = sorted(x.items(), key=lambda kv: repr(kv[0]))
        return '{' + ', '.join(f'{deep_sorted(k)}: {deep_sorted(v)}' for k, v in items) + '}'
    if isinstance(x, list):
        return '[' + ', '.join(deep_sorted(v) for v in sorted(x, key=repr)) + ']'
    if isinstance(x, tuple):
        s = ', '.join(deep_sorted(v) for v in sorted(x, key=repr))
        return '(' + s + (',' if len(x) == 1 else '') + ')'
    if isinstance(x, set):
        return '{' + ', '.join(deep_sorted(v) for v in sorted(x, key=repr)) + '}'
    return repr(x)


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())

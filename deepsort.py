def deep_sorted(x: any) -> str:
    if isinstance(x, dict):
        items = sorted(x.items(), key=lambda kv: str(kv[0]))
        return '{' + ', '.join(f'{deep_sorted(k)}: {deep_sorted(v)}' for k, v in items) + '}'
    if isinstance(x, list):
        return '[' + ', '.join(deep_sorted(v) for v in sorted(x, key=str)) + ']'
    if isinstance(x, tuple):
        s = ', '.join(deep_sorted(v) for v in sorted(x, key=str))
        return '(' + s + (',' if len(x) == 1 else '') + ')'
    if isinstance(x, set):
        return '{' + ', '.join(deep_sorted(v) for v in sorted(x, key=str)) + '}'
    return str(x)


if __name__ == '__main__':
    print(deep_sorted([1, {'a': 2, 'b': (4, 3, [5, 2]), 'c': [9, 8]}, (7, 6), '10']))

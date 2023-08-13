def partitions(n, s, m=None, expression=[]):
    global lines_printed
    if m is None:
        m = n
    if n == 0:
        if expression == "":
            print(n)
        elif lines_printed < s:
            print(" + ".join(expression))
            lines_printed += 1
        elif lines_printed == s:
            print('. . .')
            lines_printed += 1
        return 1
    if n < 0 or m == 0:
        return 0
    with_m = partitions(n - m, s, m, expression + [str(m)])
    without_m = partitions(n, s, m - 1, expression)
    return with_m + without_m


lines_printed = 0
n, s = map(int ,input('Enter n, s: ').split())
ways = partitions(n, s)
print(f"Total: {ways}")

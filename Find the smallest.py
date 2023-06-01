def smallest(n):
    digits = list(map(lambda x: x, str(n)))
    vars = []
    for i, digit in enumerate(digits):
        dgs = list(digits)
        dgs.pop(i)
        for j in range(len(digits)):
            var = list(dgs)
            var.insert(j, digit)
            var = int(''.join(var))
            vars.append([var, i, j])

    return min(vars, key=lambda x: x[0])
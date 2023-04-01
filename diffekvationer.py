from funktioner import f, g, h

equations = [
    ["y' + ay = b", ["a", "b"], f],
    ["y' + ay = bx + c", ["a", "b", "c"], g],
    ["y' + ay = bsin(kx) + ccos(kx)", ["a", "b", "c", "k"], h]
]

for i, v in enumerate(equations):
    print(i+1, v[0])

eq = int(input("\nEq: "))-1
print("")

values = []

for i, v in enumerate(equations[eq][1]):
    values.append(float(input(v + ": ")))

print("")

equations[eq][2](values)

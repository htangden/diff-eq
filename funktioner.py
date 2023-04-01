

def f(values): # y' + ay = b
    a, b = values[0], values[1]
    print(f"y = {b/a} + Ce^({-a}x)")

def g(values): # y' + ay = bx + c
    a, b, c = values[0], values[1], values[2]
    print(f"y = {b/a}x + {(c-b/a)/a} + Ce^({-a}x)")

def h(values): # y' + ay = bsin(kx) + ccos(kx)
    a, b, c, k = values[0], values[1], values[2], values[3]
    beta = (c*a-k*b)/(a**2+k**2)
    alfa = (b+k*beta)/a
    print(f"y = {alfa}sin({k}x) + {beta}cos({k}x) +  Ce^({-a}x)")
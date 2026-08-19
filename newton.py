def f(x):
    return (x+10)**2

def deriv(f, x, eps=0.001):
    return (f(x + eps) - f(x)) / eps

def second_deriv(f, x, eps=0.001):
    return (deriv(f, x + eps) - deriv(f, x)) / eps

def optimize(x0, f, eps=0.1):
    x = x0
    x_prev = x0 + eps
    while abs(x - x_prev) > eps:
        x_prev = x
        x = x - deriv(f, x) / second_deriv(f, x)
        print(x)

    return x


print(optimize(1000, f))

# import numpy as np
# optimize(2.5, np.cos)
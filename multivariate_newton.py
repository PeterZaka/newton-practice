import numpy as np
import numdifftools as nd

def f(x):
    return x[0]**2 + 3*x[0]*(x[1] - 10) + 5*(x[1] - 10)**2


def iterate_step(f, x):
    hessian_func = nd.Hessian(f)
    hessian_matrix = hessian_func(x)
    
    inverse_hessian = np.linalg.inv(hessian_matrix)
    
    grad_func = nd.Gradient(f)
    gradient = grad_func(x)

    return x - np.matmul(inverse_hessian, gradient)


def optimize(f, x0, eps=1e-10):
    """
    Uses multivariate Newton's method to find min or max point near x0 for function f, with eps

    Args:
        f - Function
        x0 - Starting point
        eps - Epsilon
    Output:
        Float of point near min or max point
    """
    if eps < 0:
        raise ValueError("`eps` must be positive")
    
    x = np.array(x0)
    dist = eps
    while abs(dist) >= eps:
        x_prev = x
        x = iterate_step(f, x)

        dist = np.linalg.norm(x - x_prev)
        print(x)

    return x

print(optimize(f, [30, 20]))

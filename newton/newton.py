def f(x):
    """Sample function for (x+10)^2"""
    return (x + 10) ** 2


def deriv(f, x, eps=1e-7):
    """Takes the derivative of f at x, with eps"""
    return (f(x + eps) - f(x)) / eps


def second_deriv(f, x, eps=1e-7):
    """Takes the second derivative of f at x, with eps"""
    return (deriv(f, x + eps) - deriv(f, x)) / eps


def optimize(x0, f, eps=1e-6):
    """
    Uses Newton's method to find min or max point near x0 for function f, with eps

    Args:
        x0 - Starting point
        f - Function
        eps - Epsilon
    Output:
        Float of point near min or max point
    """
    if not isinstance(x0, (int, float)):
        raise TypeError("`x0` must be numeric")

    if eps <= 0:
        raise ValueError("`eps` must be positive")
        
    x = x0
    x_prev = x0 + eps
    while abs(x - x_prev) >= eps:
        x_prev = x
        x = x - deriv(f, x) / second_deriv(f, x)
        print(x)

    return x


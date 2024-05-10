def unify(x, y, theta={}):
    if theta is None:
        return None
    elif x == y:
        return theta
    elif isinstance(x, str) and x[0].isupper():
        return {**theta, x: y} if x not in theta else unify(theta[x], y, theta)
    elif isinstance(y, str) and y[0].isupper():
        return {**theta, y: x} if y not in theta else unify(x, theta[y], theta)
    elif isinstance(x, list) and isinstance(y, list):
        return None if len(x) != len(y) else unify_lists(x, y, theta)
    else:
        return None

def unify_lists(x, y, theta={}):
    return theta if not x else unify_lists(x[1:], y[1:], unify(x[0], y[0], theta))

theta = unify(['father', 'X', 'Y','Z'], ['father', 'John', 'Alice','Bob'])
print("Substitutions:", theta)

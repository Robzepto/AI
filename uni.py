def is_variable(term):
    return isinstance(term, str) and term[0].isupper()
def unify_lists(x, y, theta):
    if len(x) != len(y):
        return None
    for xi, yi in zip(x, y):
        theta = unify(xi, yi, theta)
        if theta is None:
            return None
    return theta
    
def unify_var(var, x, theta):
    if var in theta:
        return unify(theta[var], x, theta)
    elif x in theta:
        return unify(var, theta[x], theta)
    else:
        theta[var] = x
        return theta
        
def unify(x, y, theta):
    if theta is None:
        return None
    elif x == y:
        return theta
    elif is_variable(x):
        return unify_var(x, y, theta)
    elif is_variable(y):
        return unify_var(y, x, theta)
    elif isinstance(x, list) and isinstance(y, list):
        return unify_lists(x, y, theta)
    else:
        return None

theta = unify(['father', 'X', 'Y','Z'], ['father', 'John', 'Alice','Bob'], {})
print("Substitutions:", theta)

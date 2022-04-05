

def is_even(x):
    return x % 2 == 0


def solve_quadratic(a, b, c):
    import math
    d = (b**2-4*a*c)
    if(d > 0):
        root1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
        root2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
        print(root1, root2)

    elif(d == 0):
        root1 = -b / (2 * a)
        print(root1)

    else:
        return None

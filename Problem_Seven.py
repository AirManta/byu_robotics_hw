import sympy as sp

"""ert = sp.sqrt(3) 
print(ert)

print(ert)

A = sp.Matrix ([
        [1, 0, 0],
        [0, 1/2, -(ert/2)],
        [0, (ert/2), (1/2)]

    ])

B = sp.Matrix ([
        [0, 0, -1],
        [0, 1, 0],
        [1, 0, 0]

    ])

C = A.T * B

sp.pprint(C)
"""

Theta, phi = sp.symbols(' Theta phi')




## 3D Transformations
def rotx(theta: float):
    """
    R = rotx(theta)

    :param float theta: angle of rotation (rad)
    :return R: 3x3 numpy array representing rotation about x-axis by amount theta
    """
    ## TODO - Fill this out
    R = sp.Matrix ([
        [1, 0, 0],
        [0, sp.cos(theta), -sp.sin(theta)],
        [0, sp.sin(theta), sp.cos(theta)]

    ])

    return R


def roty(theta: float):
    """
    R = roty(theta)

    :param float theta: angle of rotation (rad)
    :return R: 3x3 numpy array representing rotation about y-axis by amount theta
    """
    ## TODO - Fill this out
    R = sp.Matrix ([
        [sp.cos(theta), 0, sp.sin(theta)],
        [0, 1, 0],
        [-sp.sin(theta), 0, sp.cos(theta)]

    ])

    return R


def rotz(theta: float):
    """
    R = rotz(theta)

    :param float theta: angle of rotation (rad)
    :return R: 3x3 numpy array representing rotation about z-axis by amount theta
    """
    ## TODO - Fill this out
    R = sp.Matrix ([
        [sp.cos(theta), -sp.sin(theta), 0],
        [sp.sin(theta), sp.cos(theta), 0],
        [0, 0, 1]

    ])

    return R


# inverse of rotation matrix
def rot_inv(R):
    '''
    R_inv = rot_inv(R)

    :param NDArray R: 2x2 or 3x3 numpy array representing a proper rotation matrix
    :return R_inv: 2x2 or 3x3 inverse of the input rotation matrix
    '''
    ## TODO - Fill this out
    R_inv = R.transpose()

    return R_inv


R_seven = rotx(Theta) * roty(phi) * rotz(sp.pi) * roty(-phi) * rotx(-Theta)

print()
sp.pprint(R_seven)
print()


# sp.simplify() to simplify cosines
# from IPython.display import display, Math
# display(Math(sp.latex(print statement here)))
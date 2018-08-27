This method for solving a pair of simultaneous linear equations reduces one equation to one that has only a single variable. Once this has been done, the solution is the same as that for when one line was vertical or parallel. This method is known as the Gaussian elimination method.

Example 1

a = 3x + 2y = 8
b = 2x + 3y = 11

Step 1 - Multiple each equation to give rise to the same leading coefficient
a * 2 = 6x + 4y = 16
b * 3 = 6x + 9y = 33

Step 2 - Subtract one equation from the other
b - a = 5y = 17

Step 3 - Solve remaining equation
5y / 5 = 17 / 5 = 3 2/5 = y

Step 4 - Substitute above into initial equations and solve
a = 3x + 6 4/5 = 8
b = 2x + 10 1/5 = 11
3x = 6/5 && 2x = 4/5
5x = 10/5 || 2
5x / 5 = 2/5 = x

Solution --> x = 2/5, y = 3 2/5

Alternatively using Cramer's rule

Given (numbers below should be subscript):
    a1x + b1x + c1x = d1x
    a2x + b2x + c2x = d2x
    a3x + b3x + c3x = d3x

D = Determinant = (below) != 0

    | a1 b1 c1 |
    | a2 b2 c2 |
    | a3 b3 c3 |

Dx = Determinant of x

    | d1 b1 c1 |
    | d2 b2 c2 |
    | d3 b3 c3 |

Dy = Determinant of y

    | a1 d1 c1 |
    | a2 d2 c2 |
    | a3 d3 c3 |

Dz = Determinant of z

    | a1 b1 d1 |
    | a2 b2 d2 |
    | a3 b3 d3 |

x = Dx / D
y = Dy / D
z = Dz / D

Example
4x + 5y - 2z = -14 = d1
7x - y + 2z = 42 = d2
3x + y + 4z = 28 = d3

D = (below)
    | 4 5 -2 |       | a b c |
    | 7 -1 2 |   =   | d e f |
    | 3 1  4 |       | g h i |
D = a(ei - fh) - b(di - fg) - c(dh - eg)
Dx = replace 4 above with d1 (-14)
             7            d2 (42)
             3            d3 (28)
Dy...
Dz...

Vectors
Basis vectors i^, j^ (k^)
Vectors are associative
Vector addition gives a resultant vector with a magnitude
 [1, 2] + [3, 4] = [4, 6]
Scalars applied to vectors work on individual components
4[1, 2] = [4*1, 4*2] = [4, 8]
Magnitude of a vector v ([2, 3]) = sqrt(ai**2 + bj**2) = sqrt(4 + 9) = |v| = sqrt of sum of products squared
Dot product of 2 vectors (r=[a, b], s=[c, d]) = a*c + b*d = r.s
Dot products are commutative = order of ops not important = r.s = s.r

Projections TODO Scalar and Vector projection
Two vectors are orthogonal (at 90 deg) if dot product = 0
Consider projections using torch shone orthogonal to vector projected onto and shadow cast by vector projecting onto this
a = [1, 2] b = [3, 4]
Projection of a onto b = Proj b a =
((a.b) / (|b|**2)) * b = (11 / 25) * [3, 4] = [33/25, 44/25] = [1.32, 1.76] = Vector Projection
Scalar Projection = Magnitude of above vector projection
a.b / |b| = 11 / 5


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

Basic vectors = i^ [1, 0], j^ [0, 1]
A vector [3, 1] implies 3*i^ + 1*j^ = [3, 1]
Our vector can be though of as to scalars acting on the basis vectors
When changing basis vectors (e.g. b1 = [1, 2], b2  = [-1, 0.5]), the given vector acts similarly in scaling the new basis
A vector [3, 1] implies 3*b1 + 1*b2 = [3, 6] + [-1, 0.5] = [2, 6.5]

To work back from a non-standard basis to i^ and j^, find inverse of basis vectors, then multiple vector as above to inverse

Basis Vectors are linearly independent, but vectors defined in that space are linearly dependent on the basis vectors

vvv Re-read
If a vector can not be defined in terms of the basis vectors, then it itself must be another basis vector (thus dimensions increment)

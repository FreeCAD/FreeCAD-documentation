# Rigid Transformation Math
*This page is under construction. Test LaTex capability*

Rotations can be represented as orthogonal 3 x 3 matrices. Acting on a position vector they generate the rotated coordinates by $x^\prime = Rx$. Rotations keep the origin fixed. A general (proper) rigid motion combines a rotation with a translation $x^\prime = x + a$, that is $x^\prime = Rx + a$. (A proper rigid motion is one that preserves lengths and angles, but excludes reflections. A FreeCAD placement is such.)

There is a very useful representation, used by FreeCAD\'s *Placement*, of these proper rigid motions by 4 x 4 matrices of the special form $\begin{pmatrix}
R & a \\
0 & 1
\end{pmatrix}$. The rigid motion $x^\prime = Rx + a$ then takes the matrix form $\begin{pmatrix}
x^\prime \\
0 
\end{pmatrix}
=
\begin{pmatrix}
R & a \\
0 & 1
\end{pmatrix}
\begin{pmatrix}
x \\
0
\end{pmatrix}$. In this compact notation, R is the 3 by 3 rotation matrix, and $a$, $x$ and $x^\prime$ are 3 by 1 column position vectors. In FreeCAD we can construct the Placement from its constituent Rotation and displacement.

    R = App.Rotation(App.Vector(0,0,1), 120) # 120 degree rotation about z-axis
    a = App.Vector(10,0,0) # displacement of 10 along x axis
    pl = App.Placement(a, R) # construct placement, can retrieve a as pl.Base, R as pl.Rotation

In terms of the matrices, we can decompose the general transformation into its constituent translation and rotation. $\begin{pmatrix}
R &a \\
0 &1 
\end{pmatrix}
=
\begin{pmatrix}
I & a \\
0 & 1
\end{pmatrix}
\begin{pmatrix}
R & o \\
0 & 1
\end{pmatrix}$, where $I$ is the Identity matrix and $o$ is the 0-vector. Note that in terms of operations, we read the matrices from right to left, i. e. we first rotate $x$, then we translate it $Rx + a\leftarrow Rx\leftarrow x$.



---
![](images/Button_right.svg) [documentation index](../README.md) > Rigid Transformation Math

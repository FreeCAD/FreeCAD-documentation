# B-Splines
This page describes how to use B-splines in FreeCAD. It gives also background information what B-splines are and for what applications they are useful.

## Motivation

If you know already about B-splines and their application, you can directly continue with section [B-splines in FreeCAD](#B-splines_in_FreeCAD.md).

Let\'s assume you want to design a part that should be produced with a 3D printer. The part must have an edge this way   *

 <img alt="" src=images/B-splines_Motivation-start.png  style="width   *450px;"> 

You have to print the part in direction of the sketch\'s bottom to the top. Outer support structures might not be an option. Therefore you need to add a support directly to your part. What options do you have?

-   Option 1   * you could add a line from point (20, 0) to point (80, 40)   *

 <img alt="" src=images/B-splines_Motivation-line.png  style="width   *450px;"> 

However this solution needs a lot of volume, thus weight and material.

-   Option 2   * you can connect the two points with an arc of a circle. To save volume, the arc should end tangentially in point (80,40). Then your solution looks like this   *

 <img alt="" src=images/B-splines_Motivation-circle.png  style="width   *450px;"> 

OK. But at the bottom you don\'t need immediate support.

-   Option 3   * you could save some more volume if the connection between the 2 points is a curve that begins tangentially at (0, 20) and ends tangentially at (80, 40)   *

 <img alt="" src=images/B-splines_Motivation-bezier.png  style="width   *450px;"> 

So a curve with which you can connect two points tangentially to a reference point can be very useful for constructions. Bézier curves provide this feature.

## Bézier curves 

### Derivation

Bézier curves are polynomials to describe the connection between 2 points. The simplest polynomial connecting 2 points is a line ($A*x^1+B$) thus linear Bézier curves are also line segments   *

 ![](images/Bezier_linear_anim.gif )  
*Animation 1   * Linear Bézier curve.*

However a polynomial becomes useful when we can control it. So there should be a point between the 2 endpoints that allows us to define how the endpoints are connected. Like in the above example option 3 the curve is helpful when it starts and ends tangentially to lines crossing the endpoints. And this is a main feature of Bézier curves. So let\'s add a control point between the 2 endpoints. The curve will start tangentially towards this control point, meaning it is tangential to the line that we can draw between the startpoint and the control point. Going backwards from the endpoint the curve will also be tangential to the line we can draw between the control point and the end point. Animation 2 shows how such a curve looks.

 ![](images/Bezier_quadratic_anim.gif )  
*Animation 2   * Quadratic Bézier curve. P1 is hereby the control point.*

The animation makes clear what the curve basically is - a transition from P0 to P2 by rotating the line P0-P1 to become the line P1-P2. Therefore we get the nice tangential start/end feature.

Such a curve can only be described by a quadratic polynomial. (The number of left-hand/right-hand turns + 1 is the necessary polynomial order. A quadratic polynomial is a single turn, a cubic polynomial has two turn, and so on.) Therefore a Bézier curve with one control point is a quadratic (second order) Bézier curve.

Having only one control point is often not sufficient. Take the above motivation example. There in option 3 we end the curve tangentially in x-direction. But how can you connect the points (20, 0) and (80, 40) so that the curve ends tangentially in y-direction? To achieve this you need first a right-hand and then a left-hand turn, so a cubic (third order) polynomial. And that means for a Bézier curve that we need (or you can say we gain) a second control point. Animation 3 shows a cubic Bézier curve.

 ![](images/Bezier_cubic_anim.gif )  
*Animation 3   * Cubic Bézier curve.*

To answer the question, the solution with the tangential y-direction ending for the example is this one   *

 <img alt="" src=images/B-splines_Motivation-cubic-bezier.png  style="width   *450px;"> 

### Rules

In the derivation you might already noticed some \"rules\" for Bézier curves   *

-   The polynomial degree is also the degree of the curves.
-   If you need $n$ turns, you need at least a $n+1$ degree Bézier curve.
-   A Bézier curve always begins tangentially to the line between the startpoint and the first control point (and ends tangentially to the line between the last control point and the endpoint).

### Math

If you are interested to understand the background math, here are the basics.

A Bézier curve is calculated using this formula   *

$\quad
\textrm{Bezier}(n,t)=\sum_{i=0}^{n}\underbrace{\binom{n}{i}}_{\text{polynomial term}}\underbrace{\left(1-t\right)^{n-i}t^{i}}_{\text{polynomial term}}\; \underbrace{P_{i}}_{\text{point coordinate}}$

*n* is hereby the degree of the curve. So a Bézier curve of degree *n* is a polygon with order *n*. The factors $P_{i}$ are hereby in fact the coordinates of the Bézier curves\' control points. For a visualization see [Controlling Bézier curvatures](https   *//pomax.github.io/bezierinfo/#control).

If you are further interested, have a look at [The mathematics of Bézier curves](https   *//pomax.github.io/bezierinfo/#explanation) with a nicely animated derivation of the math of Bézier curves.

## B-Splines 

### Basics

[This video](https   *//www.youtube.com/watch?v=bE1MrrqBAl8) lists at the beginning the practical problems with Bézier curves. For example that adding or changing a control point changes the whole curve. These problems can be resolved by joining several Bézier curves. The result is a so-called spline, in particular a B-spline (basis spline). The video also explains that a union of quadratic Bézier curves forms a uniform quadratic B-spline and that a union of cubic Bézier curves forms a uniform cubic B-spline.

From the videos we can collect useful \"rules\" for B-splines   *

-   The first and last control point is the end/start point of the spline.
-   Like for Bézier curves, splines always begin tangentially to the line between the startpoint and the first control point (and end tangentially to the line between the last control point and the endpoint).
-   A union of $S$ Bézier curves with the degree $D$ has $S+D$ control points.
    -   Since one is in most cases working with cubic B-splines we can then state that $N$ control points lead to $N-3$ Bézier segments and in turn $N-4$ segment junction points.
-   A B-spline with the degree $D$ offers at every point a continuous $D-1$ order derivative.
    -   For a cubic B-spline this means that the curvature (second order derivative) does not change when traveling from one segment to the next one. This is a very useful feature as we will later see.

If you are interested in more details about B-Spline properties, have a look at [this video](https   *//www.youtube.com/watch?v=xXJylM2S72s).

#### Basis

Since we will only introduce the basics of B-spline, we don\'t go here into the details.

The basis constructs the spline. Looking at the definition of Bézier curves in section [Math](#Math.md) we remember that a Bézier curve is a linear combination of polynomials with the x/y coordinate of each of the control points as a factor. These polynomials are called Bernstein polynomials.

As several Bézier curves are combined to form a spline, we get a set of Bernstein polynomials forming the spline (they are the basis). As we want to overcome the mentioned limitations of Bézier curves, we don\'t geometrically combine the different Bernstein polynomials of the Bézier curves, but define Bernstein polynomials over the whole geometrical range of the spline. So we **don\'t combine** the Bézier curves with its Bernstein polynomials, which would be

$$\textrm{Bezier-combination}=\begin{cases}
  \sum_{i=0}^{n}P_{i}\cdot B_{i,n}(t),  & 0\le t\le1\\
  \sum_{i=0}^{n}P_{i+n}\cdot B_{i,n}(t-1), & 1\le t\le2\\
\cdots
\end{cases}$$

whereas $B_{i,n}(t)$ is the i-th Bernstein polynomial with order $n$ and the coefficients $P_{i}$ are the point coordinates of the Bézier curve control points. But we use a **different set of functions** that are defined over the whole spline range   *

$$\textrm{B-spline}= \sum_{i=0}^{n}p_{i}\cdot N_{i,n}(t)$$.

Note that in general $N_{i,n}(t) \ne B_{i,n}(t)$, and the Bezier control points $\{P_1, P_2,\dots\}$ are different from B-spline control points $\{p_1, p_2,\dots\}$.

The different $N_{i,n}(t)$ are defined piecewise where the interval of every piece is the interval of the Bézier piece. When the lengths of all $N_{i,n}$ pieces is equal, we speak of a uniform spline. (In literature this is often denoted as equal travel time $t$ per piece.)

To understand how the $p_{i}$ are the coordinates of the B-spline control points, see the first minute of [this video](https   *//www.youtube.com/watch?v=dPPTCy4L4rY&list=PL8bSwVy8_IcMvtI70tZoYesCS0hGVO5qd).

#### Knot vector 

As derived above, B-splines are created out of $N_{i,n}$ piecewise polynomials with continuity up to a certain derivative between the pieces. The endpoints of the piece\'s definition interval are called knots. For a spline defined over $k$ pieces, there are $k+1$ knots given by the so-called *knot vector*   *$\{t_0, t_1, t_2,\dots, t_k\}$ whereas $t_0 < t_1 < t_2 < \dots < t_k$

The knot vector comprises the knots of the $N_{i,n}$ basis functions that define the B-spline, see [this video](https   *//www.youtube.com/watch?v=ni5NNPCVvDY). The basis functions of a B-spline can be calculated using the knot vector and a creation algorithm, see [this video](https   *//www.youtube.com/watch?v=hrsO45AHtbs).

The derivative until which continuity exists is given by the multiplicity $m$. Therefore we can specify a vector with the multiplicity for every knot   * $\{m_0, m_1,\dots, m_k\}$. A knot on a spline with degree *d* and the multiplicity *m* tells that the curve left and right to the knot has at least an equal *n* order derivative (called *C*^*n*^ continuity) whereas $n=d-m$.

### Non-uniform B-splines 

The derivation of B-splines from Bézier curves have the mathematical consequence that in B-splines every polynomial piece has the same length. Such B-splines are called *uniform*. The more general case is that they can but must not have the same length. Such *non-uniform* splines have the advantage that one can control how close the splines cross its control point. Mathematically this is achieved by defining the different $N_{i,n}$ pieces at different intervals. If for example a B-spline is defined for the interval \[0, 1\], it is uniform if all its e.g. 5 pieces are also defined in this interval. If now $N_{1,4}$ is only defined in the interval \[0, 0.6\] (outside the interval it is set to zero), it is shorter and thus the spline becomes non-uniform.

As described above the parameters of the knots are described by the knot vector. So the knot vector stores the definition intervals. When now one piece gets another interval, also the knot vector changes, see [this video](https   *//www.youtube.com/watch?v=w-l5R70y6u0) for a visualization.

### Rational B-splines 

A further generalization can be made for B-splines by introducing weights for the control points. This way it can be controlled \"how important\" a control point is.

The equation for such a spline is

$$c(n, t)=\cfrac{\sum_{i=0}^{n}d_{i}N_{i, n}(t)\cdot w_i}{\sum_{i=0}^{n}N_{i, n}(t)\cdot w_i}$$

Notice that the function is no longer a polynomial, but a rational function, and these splines are called rational B-splines. Observe that when all $w_i$ are equal, the equation reduces to a regular non-rational B-spline. So non-rational B-splines are a subset of rational B-splines.

Non-uniform and rational B-splines are often called **[NURBS](https   *//en.wikipedia.org/wiki/Non-uniform_rational_B-spline)** and are widely used in geometric modeling.

## B-splines in FreeCAD 

FreeCAD offers to create uniform or non-uniform B-splines of any degree in 2D via the [Sketcher workbench](Sketcher_Workbench.md).

### Creation

To create B-splines, go into a sketch and use the toolbar button **[<img src=images/Sketcher_CreateBSpline.svg style="width   *16px"> [Create B-spline](Sketcher_CreateBSpline.md)**. Then left-click to set a control point, move the mouse left-click to set the next control point and so on. Finally right-click to finish the definition and create the B-spline.

By default uniform cubic splines are created, except there are not enough control points to do this. So when you create a B-spline with only 2 control points, you get of course a spline that is single linear Bézier curve, for 3 control points you get a quadratic Bézier curve, first with 5 control points you get a cubic B-spline consisting of 2 Bézier segments. (Starting 0.20) You can also use press D while making creating a B-spline to set it\'s degree (it will still fall to a lower degree if less points are provided).

To create periodic B-splines (B-splines that form a closed curve), use the toolbar button **[<img src=images/Sketcher_CreatePeriodicBSpline.svg style="width   *16px"> [Periodic B-spline](Sketcher_CreatePeriodicBSpline.md)**. It is not necessary to set the last control point onto the first one because the B-spline will automatically be closed   *

 ![](images/Sketcher_Periodic-B-spline-creation.gif ) 

B-splines can also be generated out of existing sketch segments. To do this, select the elements and press the the toolbar button **[<img src=images/Sketcher_BSplineApproximate.svg style="width   *24px"> [Convert Geometry to B-spline](Sketcher_BSplineApproximate.md)**.

While creating a B-spline, its degree can be specified by pressing the **D** key. With this, the default to create a cubic B-spline if possible, can be overridden. <small>(v0.20)</small> 

### Changing the Degree 

To change the degree, select the B-spline and use either the toolbar button **[<img src=images/Sketcher_BSplineIncreaseDegree.svg style="width   *24px"> [Increase B-spline degree](Sketcher_BSplineIncreaseDegree.md)** or **[<img src=images/Sketcher_BSplineDecreaseDegree.svg style="width   *24px"> [Decrease B-spline degree](Sketcher_BSplineDecreaseDegree.md)**.

**Note   *** Decreasing the degree cannot revert a prior increase of the degree, see the Wiki page [Decrease B-spline degree](Sketcher_BSplineDecreaseDegree.md) for an explanation.

### Changing the Knot Multiplicity 

The points where two Bézier curves are connected to form the B-spline are called knots. The knot multiplicity determines how the Bézier parts are connected, see the Wiki page [Increase knot multiplicity](Sketcher_BSplineIncreaseKnotMultiplicity.md) for details.

To change the knot multiplicity, use the toolbar buttons **[<img src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg style="width   *24px"> [B-spline increase knot multiplicity](Sketcher_BSplineIncreaseKnotMultiplicity.md)** or **[<img src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg style="width   *24px"> [B-spline decrease knot multiplicity](Sketcher_BSplineDecreaseKnotMultiplicity.md)**.

**Note   *** Creating two B-Splines that are connected to each other will not unite to a single new B-spline. So their connection point is not a knot. The only way to get a new knot in an existing B-spline is to decrease the degree. However, you may get many new knots. Thus the better choice is to redraw the B-spline with more control points.

### Changing the Weight 

Around every control point you see a dark yellow circle. Its radius sets the weight for the corresponding control point. By default all circles have the radius *1*. This is indicated with a radius constraint for the first control point circle.

To create a rational B-spline the weights have to be made independent. To achieve that you can delete the constraint that all circles are equal and then set different radius constraints for the circles.

If no radius constraint is set, you can also change the radius by dragging   *

 ![](images/Sketcher_Changing-control-point-weigth-dragging.gif ) 

In the dragging example you see that a high weight attracts the curve to the control point while a very low weight changes the curve so as if the control point does almost not exist.

When you look at the [creation function](#Rational_B-splines.md) for non-uniform rational B-splines you see that a weight of zero would lead to a division by zero. Negative weights are theoretically possible but they are not supported. Therefore you can only specify weights greater than zero.

**Note   *** When dragging points, knots or widths, the circle diameters denoting the weight will change. This is because the diameter depends on the overall B-spline length for visualization reasons. The actual weight is not changed.

### Editing Knots 

New knots can be added using the **[<img src=images/Sketcher_BSplineInsertKnot.svg style="width   *24px"> [B-spline insert knot](Sketcher_BSplineInsertKnot.md)** button. <small>(v0.20)</small> 

A knot is deleted by decreasing it\'s degree to 0 (i.e applying **[<img src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg style="width   *24px"> [B-spline decrease knot multiplicity](Sketcher_BSplineDecreaseKnotMultiplicity.md)** when it\'s degree is 1).

Changing the parameter value of a knot is not yet supported.

### Display Information 

Since the form of a B-spline does not tell much about its properties, FreeCAD offers [different tools](Sketcher_Workbench#Sketcher_B-spline_tools.md) to display the properties   *

+++
| Property              | Toolbar button                                                                                                                          |
+++
| **Degree**            |                                                                                                                          |
|                       | **[<img src=images/Sketcher_BSplineDegree.svg style="width   *16px"> [Show/Hide B-spline degree](Sketcher_BSplineDegree.md)**                                |
|                       |                                                                                                                                      |
+++
| **Control polygon**   |                                                                                                                          |
|                       | **[<img src=images/Sketcher_BSplinePolygon.svg style="width   *16px"> [Show/hide B-spline control polygon](Sketcher_BSplinePolygon.md)**                     |
|                       |                                                                                                                                      |
+++
| **Curvature comb**    |                                                                                                                          |
|                       | **[<img src=images/Sketcher_BSplineComb.svg style="width   *16px"> [Show/hide B-spline curvature comb](Sketcher_BSplineComb.md)**                            |
|                       |                                                                                                                                      |
+++
| **Knot multiplicity** |                                                                                                                          |
|                       | **[<img src=images/Sketcher_BSplineKnotMultiplicity.svg style="width   *16px"> [Show/hide B-spline knot multiplicity](Sketcher_BSplineKnotMultiplicity.md)** |
|                       |                                                                                                                                      |
+++
| **Weights**           |                                                                                                                          |
|                       | **[<img src=images/Sketcher_BSplinePoleWeight.svg style="width   *16px"> [Show/hide B-spline control point weight](Sketcher_BSplinePoleWeight.md)**          |
|                       |                                                                                                                                      |
+++

### Limitations

At the moment (FreeCAD 0.20) there are some limitations when using splines you should know   *

1.  You cannot set tangential constraints.In this example <img alt="" src=images/Sketcher_spline-limit-tangential.png  style="width   *450px;"> you want to assure that the spline touches the blue curve 2 times tangentially. This would be useful because the blue line could for example be the spatial border for your design.
2.  You cannot create an offset curve for a B-spline using the tool [Draft Offset](Draft_Offset.md).

## Typical Use Cases 

According to the properties of B-splines, there are 3 main use cases   *

1.  Curves that start/end tangentially to a certain direction. An example for this is the motivation example [above](#Motivation.md).
2.  Curves describing larger designs and providing the freedom of local changes. See [this example](#Designing.md) below.
3.  Curves providing a certain continuity (derivative). See [this example](#Continuity_at_Geometric_Transitions.md) below.

### Designing

Take for example the case that you design a housing of a kitchen mixer. Its desired shape should look like this one   *

 ![](images/Sketcher_spline-exmple-mixer-shell.png ) 

To define the outer form it is advantageous to use a B-spline because when you change a control point to change the curvature at the bottom, the curvature at the side and top will not be changed   *

 ![](images/Sketcher_spline-exmple-mixer-sketch.gif ) 

### Continuity at Geometric Transitions 

There are several cases where it is physically necessary to have a certain surface continuity at geometric transitions. Take for example the inner walls of a fluid channel. When you have a change in the diameter of the channel, you don\'t want to have an edge because edges would introduce turbulences. Therefore, like in the motivation example [above](#Motivation.md), one uses splines for this purpose.

The development of the Bézier curves was initially triggered by the French car industry. Besides the saving of material and the reduction of the air flow drag, the look of the cars should also be improved. And when you look at the fancy design of French cars from the 60\'s and 70\'s you see that the Bézier curves gave car design a boost.

Let\'s take for example this task in the design of cars   * The car fender should \"look nice\". Here is a basic sketch of our task   *

 <img alt="" src=images/Spline-Fender-sketch1.svg  style="width   *250px;"> 

\"Looking nice\" means that the (potential) customer looks at the fender and does not see unexpected light reflections and also no sudden changes in the reflection from the automotive paint at all. So what do you need to avoid changes in the reflections? Looking closely to the fender   *

 <img alt="" src=images/Spline-Fender-sketch2.svg  style="width   *300px;">  
*At the spatial area above the edge the intensity of reflected light is low (denoted by the red ellipse) because no light is directly reflected in the direction from the edge to the eye.*

you see when there is an edge, there is a spatial area where the reflected light has less intensity and this is what you will notice when looking at the fender. To avoid this you need a continuous change in the slope of your surface elements. The slope is the first order derivative and as explained in section [Basics](#Basics.md), a second degree (quadratic) B-spline offers at every point a continuous first order derivative.

But is this really sufficient? At the point of geometric transition we have now at both sides the same slope, but the slope might change differently at both sides. Then we have this situation   *

 <img alt="" src=images/Spline-Fender-sketch3.svg  style="width   *300px;"> 

So we have also spatial areas in which the intensity of reflected light is different. To avoid this, we need at the geometrical point of transition also a continuity of the second order derivative and thus a cubic B-spline.



---
![](images/Right_arrow.png) [documentation index](../README.md) > B-Splines

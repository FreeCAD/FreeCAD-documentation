---
- GuiCommand:
   Name:Sketcher BSplinePoleWeight
   MenuLocation:Sketch → Sketcher B-spline tools → Show/hide B-spline control point weight
   Workbenches:[Sketcher](Sketcher_Workbench.md)
   Version:0.19
   SeeAlso:[Sketcher Create B-spline](Sketcher_CompCreateBSpline.md)
---

## Description

Shows or hides the display of the **weights** for the control points of a B-spline curve (see [below](#Weight_Explanation.md) for an explanation of weights).

 <img alt="" src=images/sketcher_BSplineWeightShow.png  style="width:468px;">  
*B-spline with control point weights displayed in brackets*

## Usage

1.  Select a B-spline and use the toolbar button **<img src=images/Sketcher_BSplinePoleWeight.svg style="width:16px"> [Show/Hide B-spline control point weight](Sketcher_BSplinePoleWeight.md)**.

## Weight Explanation 

B-splines are basically a combination of [Bézier curves](B-Splines#B.C3.A9zier_curves.md) (nicely explained in [this](https://www.youtube.com/watch?v=bE1MrrqBAl8) and [this](https://www.youtube.com/watch?v=xXJylM2S72s) video).

The Bézier curve is calculated using this formula:

$\quad
\textrm{Bezier}(n,t)=\sum_{i=0}^{n}\underbrace{\binom{n}{i}}_{\text{polynomial term}}\underbrace{\left(1-t\right)^{n-i}t^{i}}_{\text{polynomial term}}\; \underbrace{P_{i}}_{\text{point coordinate}}$

*n* is hereby the degree of the curve. So a Bézier curve of degree *n* is a polygon with order *n*. The factors $P_{i}$ are hereby in fact the coordinates of the Bézier curves\' control points. For a visualization see [this page](https://pomax.github.io/bezierinfo/#control).

The term weight in FreeCAD is a bit misleading because in literature the factors $P_{i}$ are often called weights as well. FreeCAD\'s weights are something different. The idea of these weights is to modify the spline so that the different control points are \"weighted\". The idea is that a point with weight 2 should have twice as much influence than a point with weight 1. This is achieved by using this different formula to calculate the spline:

$\quad
\mathrm{Rational\ Bezier}(n,t)=\cfrac{\sum_{i=0}^{n}\binom{n}{i}\left(1-t\right)^{n-i}t^{i}w_{i}P_{i}}{\sum_{i=0}^{n}\binom{n}{i}\left(1-t\right)^{n-i}t^{i}w_{i}\;\;\;\,}$

whereby $w_{i}$ is the weight for the point $P_{i}$.

This is a new class of Bézier curves because despite the points are indeed weighted as desired, the curve is no longer a polynomial but a fractional polynomial. Therefore these curves are called rational Bézier curves and the B-splines is then called rational B-splines.

The consequence is that you gain more flexibility in defining the spline shape. If all weights are equal, the shape of the spline does not change. So the weights relative to each other is important, not the value alone. For example this spline has exactly the same shape as the one in the first image:

 <img alt="" src=images/sketcher_BSplineWeightDouble.png  style="width:468px;">  
*Same B-spline as in first image but with different absolute weight values*

A weight of zero would be a singularity in the equation to calculate the rational Bézier curves, therefore FreeCAD assures that it cannot become zero. Nevertheless, small values have the same effect as if the control point would almost not exist:

 <img alt="" src=images/sketcher_BSplineWeightZero.png  style="width:468px;">  
*Same B-spline with an almost zero weight control point*

## Changing Weights 

How to change weights is described in [ this Wiki page](B-Splines#Changing_the_Weight.md).




 {{Sketcher Tools navi}} 

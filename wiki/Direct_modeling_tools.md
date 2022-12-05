# Direct modeling tools
**An effort to implement direct modelling methodologies is currently being explored at https://github.com/MariwanJ/Design456**

This page is dedicated to the description of the [Google Summer of Code 2017](Google_Summer_of_Code.md) project idea regarding direct modeling.

## Outline

FreeCADs is a feature-based parametric modeling system, hence different modeling steps depend on one or multiple previous steps. Each step is at the same time a tool/operation, and a geometrical object, resulting from that operation. This mix of operation and object is called a feature. Direct modeling, often presented as the opposite of parametric modeling, allows to graphically move vertices, push or pull faces and edges to modify the geometry of an object.

Watch an introduction to direct modeling on <https://www.youtube.com/watch?v=RMrvjAPxyN0>

The two concepts could however easily coexist in FreeCAD. Each operation performed via direct modeling could be stored into a new feature, that would successively modify the previous object by adding transformations, such as a displacement of a vertex, an edge, or a face, or extrusion of a certain face.

This GSoC project aims at throwing the bases of the necessary feature(s) to hold such transformations as parameters, and the 3D manipulators to allow the user to modify an existing 3D object by clicking and dragging on the screen.

## Details

1.  Get familiar with OpenCasCade, FreeCADs geometric modeling kernel, and understand the geometry structure, and how complex 3D objects are constructed.
2.  Get familiar with Coin, FreeCADs 3D display manager, and understand how to create manipulators and interact with the 3D scene.
3.  Understand how FreeCADs parametric objects (features) are constructed and work
4.  Study and document existing direct modeling applications and techniques through available online videos and identify potentially useful direct modeling operations to be performed in FreeCAD. Study which pieces of information each of these operations requires, and how to store that information using FreeCAD\'s available parameters.
5.  Throw the bases of a feature, or a family of features, that can hold the necessary information, and perform the transformations. This can be done in either C++ or Python, or, ideally, a C++ core extensible in Python.
6.  Throw the bases of a manipulator, or family of manipulators, to allow the user to perform transformations by pushing and dragging on-screen, and experiment with ergonomy and usability. This can be done in either C++ or Python.

## Expected Outcome 

1.  A documentation of the various possible and useful direct modeling operations that should be performable in FreeCAD, and how each of them would translate into parametric objects (features).
2.  An implementation of a base feature, or family of features in FreeCAD, that can perform basic operations (proof of concept), that can be easily extended to support more operations in the future
3.  Experiments and/or implementation of a Coin manipulation system, that would provide the FreeCAD user with nice and ergonomic ways to interact with the geometry and perform transformations. This could also benefit other areas of FreeCAD.

## Future Possibilities 

Since direct modeling is a huge area in constant evolution, the work done in this GSoC will only cover a small part of it. But if the bases are done right, extending them will be easy and could develop very far.

## Project Properties 

### Skills

-   Programming language C++ or Python
-   Good understanding and use of APIs from FreeCAD and OpenCasCade
-   Knowledge of 3D modeling, topology and computational geometry is a plus

### Difficulty

Medium

### Additional Information 

-   Ticket [#3353: Direct modeling tools](https://tracker.freecadweb.org/view.php?id=3353) tracking efforts to implement this feature
-   Ticket [#1367: Extend Draft Edit mode to work with 3D shapes](https://tracker.freecadweb.org/view.php?id=1367)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Google Summer of Code](Category_Google Summer of Code.md) > Direct modeling tools

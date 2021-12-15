# Extend Part workbench python API
This page is dedicated to the Google Summer of Code project regarding the extension of the Python Part workbench API

## Outline

FreeCAD as a CAD system depends on a geometry kernel providing geometry and topology data structures as well as algorithms for manipulating them. The one in use, OpenCASCADE, is exposed through the Part workbench which wraps the relevant classes in python objects. This leads to a comprehensive API for geometric manipulations and calculations. Currently 3D geometry data structures are available as well as all relevant topological datastructures and algorithms. However, often geometric calculations are done in a plane, hence inherently 2D. This is also true for all parameter space curves, e.g. the pcurves of edges on a face. Hence the current 3D only API is too verbose for many use cases, where the additional z-Value is not needed at all. Furthermore extracting pcurves from topology as well as setting pcurves in the creation of topology is currently limited.

The goal of this project is to provide wrappers for all relevant 2D geometry types as well as algorithms for creation of those. Then those types can be used to extend the 3D geometry and topology APIs. This should round up the geometric scripting possibilities in FreeCAD and make it a full fledged calculational geometry tool.

## Details

1.  Get familiar with FreeCADs way of wrapping objects in python as well as with the geom2d package of open cascade which should be wrapped. A good understanding of the possibilities in both APIs is required
2.  Wrap the 2D geometry types in a FreeCAD compliant way ensuring they match nicely in the existing API and are easy to use. This means they should respect possible FreeCAD types like Vectors etc.
3.  Design an API for the advanced 2D geometry type creation facilities available in OpenCASCADE and implement those functionalities in FreeCAD. Those creations with constraints are highly valuable and one reason to prefer 2D over 3D geometry, hence the API should be simply and expressive.
4.  Wrap further available 2D algorithms like intersection and projection to allow full featured working with the new geometry types
5.  Extend the 3D API where needed to work with 2D types. This includes 3D geometry and topology, e.g. pcurves, projection and creation.

## Expected Outcome 

1.  Full 2D geometry API supporting all relevant geometry types, advanced creation and manipulation possibilities for 2D geometry as well as interoperability between 2D and 3D geometry and topology
2.  Full Documentation of the API in the Python wrapper itself accessible in the code completion of the console
3.  Documentation and usage examples in the Wiki
4.  Test cases verifying the working of the new wrapper

## Future Possibilities 

When finished with the geometry API there is plenty of room in extending the topology API with advanced functionality and more algorithms. This involves API design, as many algorithms cannot be simply wrapped as functions. OpenCASCADE is very feature rich and creating an full-featured wrapper is a huge task.

## Project Properties 

### Skills

-   Programming language mainly C++ and some Python
-   Knowledge of Python wrapping and preferable experience with PyCXX
-   Understand and use of APIs from FreeCAD and OpenCASCADE required

### Difficulty

Easy

### Additional Information 

_

---
[documentation index](../README.md) > [API](Category_API.md) > Extend Part workbench python API

# Topological Naming Project/pt-br


This page is dedicated to the description of the Google Summer of Code project idea regarding topological naming. For the topic in itself please see [Naming project](Naming_project.md). The linked wiki page can also serve as a starting point to get into the naming problem.

## Outline

FreeCAD is a parametric modeling system, hence different modeling steps depend on one or more previous steps. Changes done to one object propagate through the modeling history to all dependent objects. This is achieved through a linking system, implemented with properties. This linking is very robust when done on a whole-object basis. However, many links need to be more fine grained and link to subparts of an object. In the Part workbench environment, for example, many links go to special topology entities like vertices, edges or faces. The stability of those links depend on the exact naming of the topology elements after a recompute. This is currently not guaranteed within FreeCAD, which can lead to many errors in the dependent modeling steps after simple changes to a base object. As the current development direction of FreeCAD seems to lead to a stronger use of those links the naming issue needs to be resolved.

The GSoC project aims at laying the foundation to solve this issue and to prove the chosen approach on test cases. The preferred approach to solve the issue is described [here](https://docs.google.com/document/d/1-d2JD8RH13ar7QPh_SpX2H5eiNND4DiCPBmGwA2R9Ug/edit), with an implementation started [here](https://github.com/ickby/FreeCAD_sf_master/tree/Naming).

## Details

1.  Get familiar with opencascade, FreeCADs geometric modeling kernel, and grasp how the topology data structure works and how algorithms share, change and generate topology. Preferable the student already worked with opencascade, as the library is complex and getting into takes it\'s time.
2.  Get familiar with FreeCADs linking system and how it links to topology entities in the opencascade datastructures. It is also important to understand the usage of occ in FreeCAD, the use of a dedicated topology class combined with direct use of occ algorithms outside of that class. This dual approach may not be ideal for a solution of the naming problem, hence a good understanding of it is required.
3.  Start implementing a Identifier class that stores the creation history of a shape. Identify all data needed to make it unique and detail the interface.
4.  Integrate the identifier class into the Topology data structue and port a few first algorithms to use it. Also extend the Topology class python interface to allow the use of the identifiers for extracting subshapes.
5.  Create a set of test cases to show the effectiveness of the implementation.

## Expected Outcome 

1.  A first implementation within FreeCAD to show the working algorithm
2.  A set of test cases integrated into the available test system which show major cases of the topological naming problem and how they are resolved by the prototype implementation

## Future Possibilities 

If this project is finished successfully a full integration into the FreeCAD source can be part of further contribution or even a own GSoC project

## Project Properties 

### Skills

-   Programming language C++
-   Deep understanding and use of APIs from FreeCAD and opencascade
-   Ability to read and understand scientific texts and papers
-   Knowledge of 3D modeling, topology and computational geometry is a plus

### Difficulty

Hard

### Additional Information 

[Category:Google Summer of Code](Category:Google_Summer_of_Code.md)

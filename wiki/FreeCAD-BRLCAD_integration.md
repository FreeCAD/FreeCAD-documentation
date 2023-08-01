# FreeCAD-BRLCAD integration
This page is dedicated to the description of the [Google Summer of Code 2023](Google_Summer_of_Code.md) project idea of integrating FreeCAD and BRL-CAD.

**Obsolete**: This page has been moved to <https://github.com/FreeCAD/FreeCAD/issues/8557>

## Outline

FreeCAD and [BRL-CAD](http://www.brlcad.org) are very complementary applications: BRL-CAD is a powerful engine which could do with a better modelling UI, and FreeCAD has an increasingly vast modelling UI but could make great use of the support for large models that BRL-CAD can offer.

FreeCAD being highly modular, and BRL-CAD having a C+ API, building a BRL-CAD module for FreeCAD is totally possible. This way, it would be possible to open BRL-CAD models (that are usually called databases, because they are often made of a collection of models) in FreeCAD, and it would also be possible to use FreeCAD as a modelling tool for BRL-CAD.

This project idea will require a reasonable knowledge of C++, and, since it involves two different applications, a versatile mind able to learn quickly and navigate between many different concepts, as they are implemented differently in both applications.

This project would be mentored commonly by both FreeCAD and BRL-CAD developers.

## Details

1.  Get familiar with how FreeCAD and BRL-CAD work, what are their strengths and limitations, how they differ, how parametric modelling works in both of them
2.  Successfully compile both applications
3.  Get familiar with the BRL-CAD API
4.  Understand how FreeCAD parametric objects (features) are constructed and work, and how the view provider system works. We will basically be constructing FreeCAD view providers around BRL-CAD objects
5.  Also study the command-line interface tools offered by BRL-CAD, and assess if and how any of these could be put into use
6.  Implement basic import: Allow to open a BRL-CAD database and display its contents in FreeCAD
7.  Implement a couple of BRL-CAD-based objects: Or, how to use the FreeCAD modelling tools to produce BRL-CAD objects
8.  Implement basic saving: How the BRL-CAD-based FreeCAD objects can be saved to a BRL-CAD database, and design a strategy for possible support of other FreeCAD objects

## Expected Outcome 

1.  Documentation. Since this is a large task, that might not fit in a single GSOC project, other people (or yourself) will likely work on this project after the GSOC period ends. They must be able to take on the work where it has been stopped. Also, the first steps of this project will involve a lot of research, that should be made as available as possible to others.
2.  A basic prototype, that allows to open and visualize BRL-CAD databases in FreeCAD, and shows how modelling and saving BRL-CAD objects can work in FreeCAD

## Future Possibilities 

1.  Such an integration could go a very long way, as both applications are very complex, and if the \"wedding\" works well, new possible fields of use could emerge. Also, we think this kind of inter-project integration could pave the way for more, so the possibilities are vast.

## Project Properties 

### Skills

-   Programming language: C++
-   Good understanding and use of APIs from FreeCAD and BRL-CAD
-   Knowledge of 3D modeling, topology and computational geometry is a plus

### Difficulty

High, mostly because you have two different applications to learn and work with

### Project size 

350h

### Additional Information 

-   Potential mentors: [Yorik](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68) (FreeCAD), [rossberg](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=23847) (BRL-CAD)



---
⏵ [documentation index](../README.md) > FreeCAD-BRLCAD integration

# PartDesign project

 


{{VeryImportantMessage|
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
}}

 

Here the project plan for the **PartDesign** as part of the [Development roadmap](Development_roadmap.md).

## Purpose and principles 

This is a software development project aimed to implement the Part Design capabilities. Its about implementing some **core features** into the CAD modules of FreeCAD, **Part, PartDesign and Assembly**.

The development steps are planned here and tracked in the Issue tracking system to get a well formed change log: [Issue tracker](http://apps.sourceforge.net/mantisbt/free-cad/my_view_page.php)

## Outcome

Aim of the project is to enable FreeCAD accomplish a design task like the one at the right.

 <img alt="" src=images/Gripper.jpg  style="width:300px;">



This will be achieved by using the **Sketcher** and the **PartDesign** workbench to design a special part and **Part** to load a standard part as STEP (like the linear bearing). The **Assembly** puts it all together with constraints.

Also an important outcome is the **Feature editing methodology**. Which gives the user an intuitive approach to instantiating and editing features. This is important for all other Modules and Workbenches to become, to comply to a consistent user interface!

 <img alt="" src=images/TaskPanel.jpg  style="width:400px;">

![](images/CAD_Modeling.gif‎ ) 

### Sketcher

A parametric sketcher with a geometrical constraints solver, for more details see the **[Sketcher project](Sketcher_project.md)**.

### PartDesign

#### Body feature 

Since a history based modelling can have a lot of steps leading to the final shape a bracket is needed. That\'s the body, which holds the final outcome of the modelling and acts as a group to all the features of the history tree.

#### Pad feature 

A Pad feature extrude a Sketch (or any Part2DObject) in its normal direction. Always guaranty a solid, or fail.

#### Pocket feature 

Imprint a sketch in a base solid either defined by depth or \"Up to last \| Up to first\". Also guaranty a solid.

#### Bore feature 

A Very good bore parameter definition from the NaroCad specification: 

  ----------------------------------------------------------------------- ------------------------------------------------------------------------- -----------------------------------------------------------------------
  <img alt="" src=images/Counterbore_settings.png  style="width:300px;">   <img alt="" src=images/Counterbore_settings2.png  style="width:300px;">   <img alt="" src=images/Countersink_settings.png  style="width:300px;">
  ----------------------------------------------------------------------- ------------------------------------------------------------------------- -----------------------------------------------------------------------

  : **NaroCAD Bore definitions**



#### Pattern

Replicate one of the above features

##### **RectangularPattern**

Replicate one of the above features along an x,y pattern

##### **CircularPattern**

Replicate one of the above features along a pattern in polar coordinates

##### **ScriptedPattern**

Replicate one of the above features according to a general rule provided in form of a script.

## Brainstorming

### What others do 

-   [SolidWorks examples](http://www.youtube.com/watch?v=cVXQmDStHus)

### Pattern Implementation 

The Pattern feature class can be implemented as a tabular pattern and serve as a base class for the Rectangular, Circular and Scripted Pattern features. These derived classes will only have to fill in the repetitions table of the base class.

Each line of the repetitions table of the base Pattern class has to hold at least a transformation matrix to applied to the Placement of the original feature to be replicated. Additionally we could have optional transformation rules like for example manipulating some parameter value the feature to be replicated (e.g. in order to create a pattern of holes with varying radius).

## Organizing

### Modeling objects hierarchy 

This [UML](http://en.wikipedia.org/wiki/Unified_Modeling_Language) chart shows the planed object hierarchy and its relationships. Yellow is a abstract base class, blue implemented and grey is planed.

<img alt="" src=images/PartDesign_ModlingObjectsHirachy.png  style="width:1000px;">

## Tutorials

[PartDesign Bearingholder Tutorial I](PartDesign_Bearingholder_Tutorial_I.md)

[PartDesign Bearingholder Tutorial II](PartDesign_Bearingholder_Tutorial_II.md)

## Next actions 

Next actions are defined in the [Roadmap](http://www.freecadweb.org/tracker/roadmap_page.php) entry for PartDesign:

### Body

Since the parametric/associative nature of the PartDesign we need finally a \"Body\" which groups and organizes a construction history. The Body itself holds the end result as a shape and has grouped as children the PartDesign features. It also defines the actual head of the modeling history. Its also related to the [Assembly project](Assembly_project.md) since its the building block for products and compounds.

### Additional features 

The Pad and Pocket features are the first teaser for the PartDesign. There is still work to do especially the visibility control and the visual manipulators. But then additional features are needed.

#### Pattern 

Pattern feature which repeatingly apply a Pad or Pocket feature according to a circular or rectangular patter. An [Example in IronCAD](http://www.ironcad.com/index.php/support/learning-center). **Done \[jrheinlaender\]**

#### BoreHole

Classical bore hole with all parameters for threading and counter bore\...

#### Sweep

Sweeps a Sketch along a curve and create a Solid.

#### Revolve

Rotate a Sketch along one of its Axis and a certain angle. **Done \[jrheinlaender et al.\]**

## TODO List 

1.  **Fillet/Chamfer Part**
    1.  Apply fillet/chamfer operation to different selection types (face/faces pair/whole body)\*
2.  **Pad Tool**
    1.  Create \'up to next\' mode **DONE** \[**mrlukeparry**\]
    2.  Create \'up to surface/face\' mode \[**mrlukeparry**\]
    3.  Create draft property for pad **DONE** \[**mrlukeparry**\]
    4.  If pad is selected on face automatically create a sketch?
    5.  Create \'midplane\' mode **DONE** \[**jrheinlaender**\]
3.  **Pocket Tool**
    1.  Create \'up to first\', \'up to last\', \'through all\', \'up to surface/face\' modes **DONE** \[**jrheinlaender**\]
    2.  If pocket is selected on face automatically create a sketch?
4.  **Revolution Part**
    1.  Allow a generic line segment/axis to be used for reference
    2.  Create \'midplane\' mode **DONE** \[**jrheinlaender**\]
5.  **Hole Feature** Create ISO presentation of threads according to ISO 6410--1 standard in partial thread
6.  **Pattern Feature** **DONE** \[**jrheinlaender**\]
7.  **Sweep Feature**
8.  **Body Feature**
9.  **Reference Geometry**
    1.  Plane
10. **Mirror Tool** **DONE** \[**jrheinlaender**\]
11. **Copy feature Tool**

 

[Category:Roadmap](Category:Roadmap.md)

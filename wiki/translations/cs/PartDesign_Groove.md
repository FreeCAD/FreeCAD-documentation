# PartDesign Groove/cs
---
 GuiCommand:   Name: PartDesign_Groove   Name/cs: PartDesign Groove   Workbenches: PartDesign Workbench/cs   Návrh dílu, Complete|MenuLocation: PartDesign -> Groove---


</div>


<div class="mw-translate-fuzzy">

## Úvod

Tento nástroj otáčí náčrtem nebo 2D objektem podle zadané osy a odebírá materiál z podkladu. Například, obrázek ukazuje drážku vyříznutou na hřídeli. <img alt="" src=images/Groove_example.png  style="width:500px;"> 


</div>

The **Groove** tool revolves a selected sketch or profile about a given axis, cutting out material from the support .

![](images/PartDesign_Groove_example.svg )



*Above: sketch (A) is revolved around axis (B); resulting groove on solid (C) is shown right.*

## Usage

1.  Select the sketch to be revolved.

    :   A face on the existing solid can alternatively be used. <small>(v0.17)</small> 
    :   The sketch must be mapped to the planar face of an existing solid or Part Design feature, or an error message will appear. {{VersionMinus|0.16}}
2.  Press the **<img src="images/PartDesign_Groove.svg" width=24px> '''Groove'''** button.
3.  Set the Groove parameters (see next section).
4.  Press **OK**.


<div class="mw-translate-fuzzy">

## Volby

![](images/partdesign_groove_parameters.png ) Při vytváření drážky, dialogové okno \'parametry drážky\' nabízí několik parametrů, které specifikují jak by se náčrt měl otáčet. Mají stejný význam jako u vlastnosti [otáčení](PartDesign_Revolution#Options.md).


</div>

When creating a groove, the **Groove parameters** dialogue offers several parameters specifying how the sketch should be revolved.

+++
| ![](images/partdesign_groove_parameters.png ) | ### Axis                                                                                                                                                                                                                                                                                                |
|                                                                          |                                                                                                                                                                                                                                                                                                         |
|                                                                          | This option specifies the axis about which the sketch is to be revolved.                                                                                                                                                                                                                                |
|                                                                          |                                                                                                                                                                                                                                                                                                         |
|                                                                          | -   **Vertical sketch axis**: selects the vertical sketch axis .                                                                                                                                                                                                                                        |
|                                                                          | -   **Horizontal sketch axis**: selects the horizontal sketch axis.                                                                                                                                                                                                                                     |
|                                                                          | -   **Sketch axis**: selects a construction line contained in the sketch used by the Groove. The first construction line created in the sketch will be labelled *Sketch axis 0*. The drop down list will contain one custom sketch axis for each construction line. {{VersionMinus|0.16}} |
|                                                                          | -   **Construction line**: selects a construction line contained in the sketch used by the Groove. The drop down list will contain an entry for each construction line. The first construction line created in the sketch will be labelled *Construction line 1*. <small>(v0.17)</small>     |
|                                                                          | -   **Base (X/Y/Z) axis**: selects the X, Y or Z axis of the Body\'s Origin; <small>(v0.17)</small>                                                                                                                                                                                          |
|                                                                          | -   **Select reference\...**: allows selection in the 3D view of an edge on the Body, or a [datum line](PartDesign_Line.md). <small>(v0.17)</small>                                                                                                                                  |
|                                                                          |                                                                                                                                                                                                                                                                                                         |
|                                                                          | ### Angle                                                                                                                                                                                                                                                                                               |
|                                                                          |                                                                                                                                                                                                                                                                                                         |
|                                                                          | This controls the angle through which the groove is to be formed, e.g. 360° would be a full, contiguous revolution. It is not possible to specify negative angles (use the **Reversed** option instead) or angles greater than 360° .                                                                   |
|                                                                          |                                                                                                                                                                                                                                                                                                         |
|                                                                          | ### Symmetric to plane                                                                                                                                                                                                                                                             |
|                                                                          |                                                                                                                                                                                                                                                                                                         |
|                                                                          | If checked, the groove will extend half of the specified angle in both directions from the sketch plane .                                                                                                                                                                                               |
|                                                                          |                                                                                                                                                                                                                                                                                                         |
|                                                                          | ### Reversed                                                                                                                                                                                                                                                                                            |
|                                                                          |                                                                                                                                                                                                                                                                                                         |
|                                                                          | If checked, the direction of revolution is reversed from default clockwise to counterclockwise .                                                                                                                                                                                                        |
+++

## Properties

Below are properties which can be defined after creation of the feature. Data properties *Base* and *Axis* are uneditable .

-    **Angle**: angle of rotation. See [Angle](#Angle.md) .

-    **Label**: label given to the operation, can be changed at convenience.

-    **Midplane**: true or false. See [Symmetric to plane](#Symmetric_to_plane.md).

-    **Reversed**: true or false. See [Reversed](#Reversed.md).

-    **Refine**: true or false. If set to true, cleans the solid from residual edges left by features. See [Part RefineShape](Part_RefineShape.md) for more details. <small>(v0.17)</small> 





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Groove/cs

---
- GuiCommand:
   Name: Part JoinConnect
   MenuLocation: Part -> Join -> Connect objects
   Workbenches: Part_Workbench
   Version: 0.16
   SeeAlso: Part_JoinEmbed, Part_JoinCutout, Part_Boolean, Part_Thickness
---

# Part JoinConnect/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Instrument de conectare pentru îmbinarea inerioarelor a două obiecte goale-tip perete (de ex. Conducte). Poate asocia, de asemenea, cu cochiliile și filamente/polilinii.


</div>

![600px](images/JoinFeatures_Connect.png)

## Usage


<div class="mw-translate-fuzzy">

## Cum se folosește 

1.  Select objects to be connected.
    The order of selection is not important, since the action of the tool is symmetric. It is enough to select one sub-shape of each object (e.g., faces). You can also select a compound containing all the shapes to be connected, e.g. [Draft Array](Draft_Array.md).
2.  Invoke the Part JoinConnect command.


</div>


<div class="mw-translate-fuzzy">

Se creează un obiect parametric Connect. Obiectele originale sunt ascunse, iar rezultatul intersecției este afișat în vizualizarea 3D.


</div>

## Properties


{{TitleProperty|Connect}}


<div class="mw-translate-fuzzy">

## Proprietăți


{{TitleProperty|Connect}}

-    **Objects**: List of objects to be connected. Generally, at least two objects are needed, but a single compound containing the shapes to connect will do as well. (as of FreeCAD v0.17.8053, this property is not displayed in property editor, and can only be accessed via Python).

-    **Refine**: Sets whether to apply [Refine](Part_RefineShape.md) operation or not, to the final shape. The default value is determined by a \'Automatically refine shape after boolean operation\' checkbox in PartDesign preferences.

-    **Tolerance**: \"fuzziness\" value. This is an extra tolerance to apply when searching for intersections, in addition to tolerances stored in the input shapes.


</div>

## Example


<div class="mw-translate-fuzzy">

## Exemplu

1.  Create a pipe by applying [thickness](Part_Thickness.md) to a [cylinder](Part_Cylinder.md):
    ![320px](images/JoinFeatures_Example_step1.png)
2.  Create another, smaller diameter pipe, and [place](Placement.md) it so that it pierces the wall of the first pipe:
    ![320px](images/JoinFeatures_Example_step2.png)
3.  Select the first pipe and the second pipe, and click the \'Connect objects\' option from the Join tools dropdown toolbar button.
    ![320px](images/JoinFeatures_Example_step3_Connect.png)
4.  Use some cross-section tool ([Clipping plane](Std_ToggleClipPlane.md), [Arch Section Plane](Arch_SectionPlane.md), [Arch Cut Plane](Arch_CutPlane.md)) to reveal internals. On the picture below, Arch Section Plane is used.
    ![320px](images/JoinFeatures_Example_step4_Connect.png)


</div>

## Algorithm


<div class="mw-translate-fuzzy">

## Algoritm

Algoritmii din spatele instrumentelor de conectare sunt relativ de simple, iar înțelegerea acestora este importantă pentru utilizarea corectă a instrumentelor. Algoritmul Connect, în special, este un pic mai complex decât alții, însă în general este suficient să ne gândim la acesta ca la o variantă simetrică [Embed algorithm](Part_JoinEmbed#Algorithm.md)


</div>


<div class="mw-translate-fuzzy">

1\. Each object is split into pieces by intersections with other objects. (see [Part BooleanFragments](Part_BooleanFragments.md))


</div>

2\. From the pieces of an object, only the largest one is kept; all the rest are thrown away.

3\. Intersection pieces that touch at least two objects are added to result. Then, the pieces are joined together to form the result of Connect.

### Notes


<div class="mw-translate-fuzzy">

### Note

-   Dacă la etapa 1 fiecare obiect rămâne într-o singură bucată, rezultatul Connect va fi echivalent cu [union](Part_Fuse/ro.md) de obiecte.
-   Now, all compounds supplied are exploded prior to connecting. This means that self-intersecting compounds, which are invalid for all other Boolean operations, are valid for Connect. (This may be changed in the future.)
-   The \"largest\" piece is the one that has largest mass. That is, for solids, volumes are compared; for shells and faces, areas are compared, and so on.
-   Since FreeCAD v0.17.8053, and if OCC version is 6.9.0 and above, Connect is almost as fast as all other Boolean operations. For older versions, Connect is approximately 5 times slower than a regular Boolean operation, and works only on solids.


</div>

## Script


<div class="mw-translate-fuzzy">

Instrumentul Join poate fi folosit în [macros](macros.md) și din consola python utilizând următoarea funcție:


</div>

**BOPTools.JoinFeatures.makeConnect(name)**

-   Creates an empty Connect feature. The \'Objects\' property must be assigned explicitly, afterwards.
-   Returns the newly created object.

Connect can also be applied to plain shapes, without the need to have a document object, via:

**Part.BOPTools.JoinAPI.connect(list_of_shapes, tolerance = 0.0)**

This can be useful for making custom Python scripted features.

Exempluː


{{code|code=
import Part
j = Part.BOPTools.JoinFeatures.makeConnect(name= 'Connect')
j.Objects = FreeCADGui.Selection.getSelection()
}}


<div class="mw-translate-fuzzy">

The tool itself is implemented in Python, see /Mod/Part/BOPTools/JoinFeatures.py under where FreeCAD is installed.


</div>



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part JoinConnect/ro

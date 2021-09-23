---
- GuiCommand:
   Name:Part JoinCutout
   MenuLocation:Part → Join → Cutout for Object
   Workbenches:[Part](Part_Workbench.md)
   Version:0.16
   SeeAlso:[Part JoinConnect](Part_JoinConnect.md), [Part JoinEmbed](Part_JoinEmbed.md), [Part Boolean](Part_Boolean.md), [Part Thickness](Part_Thickness.md)
---

# Part JoinCutout/ro


</div>


<div class="mw-translate-fuzzy">

## Descriere

Coutout tool creates a cutout in a walled object (e.g., a pipe) to fit another walled object.


</div>

The <img alt="" src=images/Part_JoinCutout.svg  style="width:24px;"> [Part JoinCutout](Part_JoinCutout.md) tool creates a cutout in a walled object (e.g., a pipe) to fit another walled object.

![600px](images/JoinFeatures_Cutout.png)

## Usage


<div class="mw-translate-fuzzy">

## How to use 

1.  Select the base object first, then the object to define the cutout.
    The order of selection is important. It is enough to select one sub-shape of each object (e.g., faces).
2.  Invoke the Part JoinCutout command.


</div>


<div class="mw-translate-fuzzy">

A Part JoinFeature object is created, with Mode set to \'Cutout\'. Original objects are hidden, and the result of cutting is shown in 3D view.


</div>

## Properties


{{TitleProperty|Base}}


<div class="mw-translate-fuzzy">

## Properties 


{{TitleProperty|Base}}

-    **Base**: Reference to base object (the one to make the cutout in). The object should be a single solid.

-    **Tool**: Reference to tool object (the object that is to fit into the cutout). The object can be a single solid, or a [valid compound](Part_MakeCompound.md) of solids.

-    **Mode**: The mode of operation, equals \'Cutout\' (Changing that will transform the tool into another Part\_JoinXXX). The value of \'bypass\' can be used to temporarily disable the long computations (a compound of Base and Tool will be created, which is a fast operation).

-    **Refine**: Sets whether to apply [Refine](Part_RefineShape.md) operation or not, to the final shape. The default value is determined by a \'Automatically refine shape after boolean operation\' checkbox in PartDesign preferences. When Mode property is \'bypass\', Refine is ignored (never applied).


</div>

## Example


<div class="mw-translate-fuzzy">

## Examplu

1.  Create a pipe by applying [thickness](Part_Thickness.md) to a [cylinder](Part_Cylinder.md):
    ![320px](images/JoinFeatures_Example_step1.png)
2.  Create another, smaller diameter pipe, and [place](Placement.md) it so that it pierces the wall of the first pipe:
    ![320px](images/JoinFeatures_Example_step2.png)
3.  Select the first pipe, then the second pipe (order of selection is important), and click the \'Cutout for object\' option from the Join tools dropdown toolbar button.
    ![320px](images/JoinFeatures_Example_step3_Cutout.png)


</div>

## Algorithm


<div class="mw-translate-fuzzy">

## Algoritm

Algoritmii din spatele instrumentelor de conectare sunt destul de simple, iar înțelegerea acestora este importantă pentru utilizarea corectă a instrumentelor.


</div>


<div class="mw-translate-fuzzy">

1\. Base object is [boolean-cut](Part_Cut.md) with Tool object. The resulting shape is a set ([compound](Part_MakeCompound.md)) of non-intersecting solids (typically, two).


</div>

2\. The resulting compound is filtered: only the largest solid is kept.


<div class="mw-translate-fuzzy">

3\. If Refine property is true, the resulting shape is [refined](Part_RefineShape.md).
![800px](images/JoinFeatures-Algo-Cutout.png)


</div>

### Notes


<div class="mw-translate-fuzzy">

### Notă

-   Dacă după pasul 1, obiectul rămâne într-o singură bucată, rezultatul Cutout va fi echivalent cu [ boolean cut](Cut_Cut.md) al Base with Tool.
-   Now, the tool will produce unexpected result, if a compound is supplied as Base. This may be changed in the future.
-   Because the largest piece is determined by comparing volumes of pieces, the tool can only work with solids. This may be changed in the future.


</div>

## Programare-Script 

Instrumentul Join poate fi utilizat în [macros](macros.md) și de la consola python utilizând umătoarea funcție:


```pythonJoinFeatures.makePartJoinFeature(name = 'Cutout', mode = 'Cutout')```

-   Creates an empty Cutout feature (or other Join feature, depending on mode passed). The properties Base and Tool must be assigned explicitly, afterwards.
-   Returns the newly created object.

Exempluː {{code|code=
import JoinFeatures
j = JoinFeatures.makePartJoinFeature(name = 'Cutout', mode = 'Cutout' )
j.Base = FreeCADGui.Selection.getSelection()[0]
j.Tool = FreeCADGui.Selection.getSelection()[1]
}}


<div class="mw-translate-fuzzy">

Instrumentul propriu-zis este implementat în Python, vezi /Mod/Part/JoinFeatures.py unde este instalat FreeCAD.


</div>

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part JoinCutout/ro

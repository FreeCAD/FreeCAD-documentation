# Part Section/ro
---
- GuiCommand:   Name:Part Section   MenuLocation:Part → Section   Workbenches:[SeeAlso:[[Part_SectionCross|Cross-sections](Part_Workbench___Part]].md)---


</div>

## Description


<div class="mw-translate-fuzzy">

## Introducere

Extrage o secțiune din intersecția a două forme selectate, cea de-a doua servind drept plan secțiune. Această operație este complet parametrică, iar componentele pot fi modificate și rezultatul recalculat.


</div>

-   An intersection of two solids/faces results in one or more section lines.
-   An intersection of two lines, or a line and a solid/face, results in one or more points.

![](images/PartSection1_it.png ) 
*A cube sectioned with a cylinder*




<div class="mw-translate-fuzzy">

## Utilizare


</div>


<div class="mw-translate-fuzzy">

1.  Select the base object
2.  Select the Section tool
3.  Click on **Part** → **<img src="images/Part_Section.png" width=24px>  Section** from the top menu.


</div>

## Properties

See also: [Property editor](Property_editor.md).

A PartDesign Section object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|Base}}

-    **Base|Link**: Link to the first object.

-    **Tool|Link**: Link to the second object.


{{Properties_Title|Boolean}}

-    **History|ShapeHistory|hidden**: \"Shape history\".

-    **Refine|Bool**: \"Refine shape (clean up redundant edges) after this boolean operation\". The default value is determined by the **Automatically refine model after sketch-based operation** preference. See [PartDesign Preferences](PartDesign_Preferences#General.md).


{{Properties_Title|Section}}

-    **Approximation|Bool**: Approximate the output edges.



## Legături


<div class="mw-translate-fuzzy">

To create sections with a section plane see [Cross-sections](Part_SectionCross.md).


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Section/ro

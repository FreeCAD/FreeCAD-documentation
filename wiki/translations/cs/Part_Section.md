# Part Section/cs
---
- GuiCommand:   Name: Part Chamfer   Name/cs: Díl Řez   MenuLocation: Díl -> Řez   Workbenches: Part_Workbench/cs   Díl, Kompletace|SeeAlso: ---


</div>

## Description

The <img alt="" src=images/Part_Section.svg  style="width:24px;"> **Part Section** command creates wire geometry at the intersections of two objects. The result is fully parametric.

-   An intersection of two solids/faces results in one or more section lines.
-   An intersection of two lines, or a line and a solid/face, results in one or more points.

![](images/PartSection1_it.png ) 
*A cube sectioned with a cylinder*

## Usage

1.  Select two objects.
2.  The first object will be the **Base** of the Section, but the selection order has no impact on the result.
3.  There are several ways to invoke the command:
    -   Press the **![](images/)_[Section](Part_Section.md)** button.
    -   Select the **Part → ![](images/)_Section**_option_from_the_menu.

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

## Links

To create sections with a section plane see <img alt="" src=images/Part_CrossSections.svg  style="width:16px;"> [Cross-sections](Part_CrossSections.md).



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Section/cs

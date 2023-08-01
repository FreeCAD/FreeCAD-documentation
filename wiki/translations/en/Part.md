# Part/en
## Introduction




In FreeCAD the word \"[Part](Part.md)\" is normally used to refer to a <img alt="" src=images/Std_Part.svg  style="width:24px;"> [Std Part](Std_Part.md) (`App::Part` class), a type of container object that is defined by the base system. This Part is used to manage the position of 3D shapes in order to create mechanical assemblies.

See <img alt="" src=images/Std_Part.svg  style="width:24px;"> [Std Part](Std_Part.md) for more information about this type of object.

## Usage

The Std Part tool is not defined by a particular workbench, but by the base system, thus it is found in the **structure toolbar**, which is available in all [workbenches](Workbenches.md).

1.  Press the **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part.md)** button. An empty Part is created and automatically becomes *[active](Std_Part#Active_status.md)*.

## Notes

In informal usage, a \"Part\" may be any geometrical figure that is visible in the [3D view](3D_view.md), and thus its concept may be confused with that of \"[Body](Body.md)\" or \"[Assembly](Assembly.md)\".

However, when more precision is required, the distinction must be made.

-   A \"[Body](Body.md)\" is used for single contiguous elements, usually created with the [Part](Part_Workbench.md) or [PartDesign Workbenches](PartDesign_Workbench.md).
-   A \"Part\" is used to group a single \"Body\", or several of them to form an \"Assembly\".
-   An \"Assembly\" is a collection of \"Parts\" arranged in some way, manually, or by using an assembly workbench.


{{Std Base navi

}} {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > Part/en

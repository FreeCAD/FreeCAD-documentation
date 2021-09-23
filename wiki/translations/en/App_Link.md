# App Link/en
{{TOCright}}

## Introduction

<img alt="" src=images/Link.svg  style="width:32px;">

An [App Link](App_Link.md), or formally an `App::Link`, is a type of object that references or links to another object, in the same document, or in another document. It is especially designed to efficiently duplicate a single object multiple times, which helps with the creation of complex [assemblies](assembly.md) from smaller subassemblies, and from multiple reusable components like screws, nuts, and similar fasteners.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">


*Simplified diagram of the relationships between the core objects in the program. The `App::Link* object is a core component of the system, it does not depend on any workbench, but it can be used with most objects created in all workbenches.`

## Usage

1.  Select an object in the [tree view](tree_view.md) or [3D view](3D_view.md) for which you wish to create a Link.
2.  Press the **<img src=images/Std_LinkMake.svg style="width:16px"> [Std LinkMake](Std_LinkMake.md)** button. The produced object has the same icon as the original object, but has an arrow overlay indicating it is a Link.

See the [Std LinkMake](Std_LinkMake.md) page for the complete information, including its use in [Scripting](Std_LinkMake#Scripting.md).

## Properties

An [App Link](App_Link.md) (`App::Link` class) is derived from the basic [App DocumentObject](App_DocumentObject.md) (`App::DocumentObject` class), therefore it shares most of the latter\'s properties.

See the full list of properties in the [Std LinkMake](Std_LinkMake.md) page.


{{Std Base navi

}} {{Document objects navi}}

---
[documentation index](../README.md) > App Link/en

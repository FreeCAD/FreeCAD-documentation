# App Part
 

## Introduction

 <img alt="" src=images/Geofeaturegroup.svg  style="width:32px;"> 

An [App Part](App_Part.md) object, or formally an `App::Part`, is an element that allows grouping objects in 3D space.

It was developed to be used in assemblies, as it has an **Origin** which serves as the positional reference for the grouped objects.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">


*Simplified diagram of the relationships between the core objects in the program. The `App::Part* class is a simple container that has a position in 3D space, and has an Origin to control the placement of the objects grouped under it.`

## Usage

1.  Press the **<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part.md)** button. An empty Part is created and automatically becomes *[active](Std_Part#Active_status.md)*.
2.  To add objects to a Part, drag and drop them over the Part in the [tree view](tree_view.md).
3.  To remove objects from a Part, drag them out of the Part, and onto the document label at the top of the [tree view](tree_view.md).

See the [Std Part](Std_Part.md) page for the complete information, including its use in [Scripting](Std_Part#Scripting.md).

## Properties

An [App Part](App_Part.md) (`App::Part` class) is derived from the basic [App GeoFeature](App_GeoFeature.md) (`App::GeoFeature` class), therefore it shares most of the latter\'s properties.

See the full list of properties in the [Std Part](Std_Part.md) page.

 {{Std Base navi}} {{Document objects navi}} 

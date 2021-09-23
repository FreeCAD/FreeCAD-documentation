# App DocumentObjectGroup/pl


## Introduction

<img alt="" src=images/Folder.svg  style="width:32px;">

An [App DocumentObjectGroup](App_DocumentObjectGroup.md) object, or formally an `App::DocumentObjectGroup`, is a simple element that allows grouping any type of [App DocumentObject](App_DocumentObject.md) in the [tree view](tree_view.md) no matter its type of data.

It was developed to organize the objects in the [tree view](tree_view.md) in a way that is logical for the user.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">


*Simplified diagram of the relationships between the core objects in the program. The `App::DocumentObjectGroup* class has an extension that allows it to group any type of object; the Group itself doesn't have many properties.`

## Usage

1.  Press the **<img src=images/Std_Group.svg style="width:16px"> [Std Group](Std_Group.md)** button in the structure toolbar. An empty Group is created.
2.  To add objects to a Group, select them in the [tree view](tree_view.md), and then drag and drop them over the Group.
3.  To remove objects from a Group, drag them out of the Group, and onto the document label at the top of the [tree view](tree_view.md).

See the [Std Group](Std_Group.md) page for the complete information, including its use in [Scripting](Std_Group#Scripting.md).

## Properties

An [App DocumentObjectGroup](App_DocumentObjectGroup.md) (`App::DocumentObjectGroup` class) is derived from the basic [App DocumentObject](App_DocumentObject.md) (`App::DocumentObject` class), therefore it shares all the latter\'s properties.

See the properties in the [Std Group](Std_Group.md) page.


{{Std Base navi

}} {{Document objects navi}} 

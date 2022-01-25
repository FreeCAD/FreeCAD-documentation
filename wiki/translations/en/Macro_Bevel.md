# Macro Bevel/en
{{Macro
|Name=Macro Bevel
|Icon=Bevel.svg
|Description=Bevel selected vertices of solid objects, parametric, compatible with Part Design
|Author=TheMarkster
|Version=0.2022.01.19
|Date=2022-01-19
|FCVersion=Python 3 versions
|Download=[https://wiki.freecadweb.org/File:bevel.svg ToolBar Icon]
|SeeAlso=
|Links=[https://github.com/mwganson/Bevel Full Documentation on Github]
}}

## Description

This macro is used to bevel the selected vertices of solid objects, it also works with faces. If the selected object is a Part Design feature the Bevel parametric object will place itself into the Part Design body and further modeling can be done on the same body. If the selected object is not a Part Design feature, then a new object is added to the tree as a standard, parametric feature python object.

Usage: Select vertices in the 3D view that you desire to bevel and run the macro. You can also select the entire object in the tree, in which case all the vertices will be beveled. This is very similar to other dressup tools in FreeCAD, such as Fillets and Chamfers, and behaves very similarly to those objects, except it is cross-compatible with both Part and Part Design workbenches.

Full documentation can be found on github: [Bevel](https://github.com/mwganson/Bevel).

<img alt="" src=images/bevel_scr.png  style="width:600px;"> 
*Macro Bevel screenshot‎*

## Legend


{{Codeextralink|https://gist.github.com/mwganson/25ee4dc925c8bcf1182bd9979025ed2d/raw/7b728b8821e2012546ab77bd9da8c31ee198ad1e/Bevel.FCMacro|Bevel.FCMacro}}

ToolBar Icon ![](images/Bevel.svg )

## Script

**Macro Bevel.FCMacro**


{{CodeDownload|https://gist.github.com/mwganson/25ee4dc925c8bcf1182bd9979025ed2d|Bevel.FCMacro}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Bevel/en

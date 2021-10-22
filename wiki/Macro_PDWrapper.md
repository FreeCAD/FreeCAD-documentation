# Macro PDWrapper
{{Macro
|Name=Macro Pdwrapper
|Icon=Workbench_PartDesign.svg
|Description=Encapsulate non-PartDesign solids to work in PartDesign
|Author=TheMarkster
|Version=0.2021.10.21.rev3
|Date=2021-10-21
|FCVersion=python 3 versions
|Download=[https://wiki.freecadweb.org/File:Workbench_PartDesign.svg ToolBar Icon]
|SeeAlso=
|Links=[https://github.com/mwganson/pdwrapper Full Documentation on Github]
}}

## Description

PDWrapper encapsulates solids created in other workbenches inside a PartDesign::FeaturePython object so that they behave as if they were native PartDesign features. In the screenshot below it shows a Part Workbench fillet of a PartDesign Additive Box encapsulated inside a PDWrapper object of type Common Additive. But PDWrapper can do more than just encapsulate non-PartDesign solids for use in a PartDesign Body. It can also encapsulate PartDesign features and change their nature. For example, you can encapsulate a PartDesign Hole inside a PDWrapper Additive type and turn the Hole into a threaded rod (presuming the Hole is threaded). With PDWrapper you can create types of Primitives that are not available, such as Common (Intersection) types and XOR types. It also allows to dynamically include/exclude some solid features from the Body\'s Tip shape.

Examples and full documentation can be found on github: [PDWrapper](https://github.com/mwganson/pdwrapper).

 <img alt="" src=images/Pdwrapper_scr.png  style="width:600px;">  
*Macro PDWrapper screenshot‎*

## Legend

 

ToolBar Icon  ![](images/Workbench_PartDesign.svg ) 

## Script

 **Macro Pdwrapper.FCMacro**


{{CodeDownload|https://gist.github.com/mwganson/4106e84eeaaf4d6e056cd286cbc39170|Pdwrapper.FCMacro}}

---
[documentation index](../README.md) > Macro PDWrapper
